import dataclasses
import logging
from collections import deque
from concurrent.futures import (
    FIRST_COMPLETED,
    Future,
    ProcessPoolExecutor,
    ThreadPoolExecutor,
    wait,
)
from threading import Event, Lock, Thread
from typing import Any, Collection, Generic, Iterable, cast, overload

from batched_queue.incrementer import Incrementer
from batched_queue.result import BatchedQueueResult
from batched_queue.types import (
    BatchedQueueWorkerMultiple,
    BatchedQueueWorkerSingle,
    BQWorkerType,
    T,
    U,
)

PoolExecutor = ThreadPoolExecutor | ProcessPoolExecutor

ResultT = BatchedQueueResult[U]

logger = logging.getLogger(__name__)

_multiprocessing_initialized = False


def _init_multiprocessing():
    global _multiprocessing_initialized
    if not _multiprocessing_initialized:
        import multiprocessing as mp

        try:
            mp.set_start_method("forkserver")
        except ValueError:
            # not all platforms support forkserver, just ignore
            pass
        _multiprocessing_initialized = True


@dataclasses.dataclass
class WorkerFunc(Generic[T, U]):
    func: BQWorkerType
    kwargs: dict[str, Any]
    multiple_form: bool

    def __call__(self, to_proc: list[T]) -> list[U]:
        if self.multiple_form:
            self.func = cast(BatchedQueueWorkerMultiple, self.func)
            return self.func(to_proc, **self.kwargs)
        self.func = cast(BatchedQueueWorkerSingle, self.func)
        return [self.func(item, **self.kwargs) for item in to_proc]


class BatchedQueue(Generic[T, U]):
    multiple_form: WorkerFunc | None
    single_form: WorkerFunc | None
    _proc_thread: Thread | None
    _worker_pool: PoolExecutor | None

    def __init__(
        self,
        worker_func_multiple: BatchedQueueWorkerMultiple[T, U] | None = None,
        worker_func_single: BatchedQueueWorkerSingle[T, U] | None = None,
        *,
        batch_max_size: int | None = None,
        worker_func_single_cost: int = 1000,
        worker_func_multiple_fixed_cost: int = 5000,
        worker_func_multiple_cost: int = 100,
        worker_func_single_kwargs: dict[str, Any] | None = None,
        worker_func_multiple_kwargs: dict[str, Any] | None = None,
        num_workers: int = 1,
        worker_pool_executor: type[PoolExecutor] = ThreadPoolExecutor,
    ):
        super().__init__()
        if worker_func_multiple is None and worker_func_single is None:
            raise ValueError("Either worker_func_multiple or worker_func_single must be provided")
        self.multiple_form = self.single_form = None
        if worker_func_multiple is not None:
            self.multiple_form = WorkerFunc(
                func=worker_func_multiple,
                kwargs=worker_func_multiple_kwargs or {},
                multiple_form=True,
            )
        if worker_func_single is not None:
            self.single_form = WorkerFunc(
                func=worker_func_single,
                kwargs=worker_func_single_kwargs or {},
                multiple_form=False,
            )

        self.worker_func_single_cost = worker_func_single_cost
        self.worker_func_multiple_fixed_cost = worker_func_multiple_fixed_cost
        self.worker_func_multiple_cost = worker_func_multiple_cost
        if worker_pool_executor == ProcessPoolExecutor:
            _init_multiprocessing()
        self.worker_pool_executor = worker_pool_executor
        self.num_workers = num_workers

        self._worker_pool = None
        self._futures: list[Future] = []

        self.to_process_q: deque[tuple[int, T]] = deque()
        self._process_q_lock = Lock()

        self._q_ready = Event()

        # maps item id to result object
        self.items_map: dict[int, ResultT] = {}
        self._cur_item_id = Incrementer()
        self.batch_max_size = batch_max_size
        self._stop = False
        self._proc_thread = None

    def start(self):
        self._proc_thread = Thread(target=self._processor_loop)
        self._proc_thread.start()

    def stop(self):
        self._stop = True
        self._q_ready.set()
        if self._proc_thread is not None:
            self._proc_thread.join()

    def kill(self, timeout=5):
        self._stop = True
        self._q_ready.set()
        if self._proc_thread is not None:
            self._proc_thread.join(timeout=timeout)
        if self._worker_pool is not None:
            self._worker_pool.shutdown(wait=False, cancel_futures=True)
            self._worker_pool = None

    def put(self, item: T | Iterable[T]) -> BatchedQueueResult[U]:
        is_list = True
        if not isinstance(item, Iterable):
            is_list = False
            item = [item]
        item = cast(Iterable[T], item)
        item_ids = []
        for i in item:
            item_id = self._cur_item_id.increment()
            self.to_process_q.append((item_id, i))
            item_ids.append(item_id)
        result: BatchedQueueResult[U] = BatchedQueueResult(_ids=item_ids, is_list=is_list)
        self.items_map.update({i: result for i in item_ids})
        with self._process_q_lock:
            if len(self.to_process_q) != 0:
                self._q_ready.set()
        return result

    def _wait_for_futures(self):
        if self.num_workers == 1:
            return
        while len(self._futures) > self.num_workers:
            logger.debug("Waiting for workers to finish processing: %s", len(self._futures))
            _, running_futures = wait(self._futures, return_when=FIRST_COMPLETED)
            self._futures = list(running_futures)
            logger.debug("Workers finished processing: %s", len(self._futures))
        logger.debug("Workers available: %s", self.num_workers - len(self._futures))

    def _processor_process(self):
        with self._process_q_lock:
            if len(self.to_process_q) == 0:
                self._q_ready.clear()
                return
            to_proc_ids, to_proc = self._get_for_processing()
        worker_func = self._select_func(len(to_proc_ids))
        logger.info(
            "Processing %s items with Worker func type: %s",
            len(to_proc_ids),
            "Multiple" if worker_func.multiple_form else "Single",
        )

        self._run_worker(worker_func, to_proc_ids, to_proc)

    def _processor_loop(self):
        if self.num_workers > 1:
            self._worker_pool = self.worker_pool_executor(max_workers=self.num_workers)
        while not self._stop:
            self._q_ready.wait(timeout=5)
            self._wait_for_futures()
            self._processor_process()

        if self._worker_pool is not None:
            self._worker_pool.shutdown()
            self._worker_pool = None

    def _run_worker(self, func: WorkerFunc, ids: list[int], to_proc: list[T]):
        if self._worker_pool is not None:
            logger.debug("Running worker with %s items", len(to_proc))
            results_future: Future = self._worker_pool.submit(func, to_proc)
            results_future.add_done_callback(self._process_future_result(ids))
            self._futures.append(results_future)
        else:
            results = func(to_proc)
            self._process_results(ids, results)

    def _process_future_result(self, ids: list[int]):
        def process_future(fut: Future):
            results: list[BaseException | None | U]
            if fut.exception() is not None:
                logger.exception(fut.exception(), exc_info=fut.exception())
                e = fut.exception()
                results = [e] * len(ids)
            else:
                results = fut.result()
            self._process_results(ids, results)

        return process_future

    def _process_results(self, ids: list[int], results: list[BaseException | None | U]):
        for item_id, result in zip(ids, results):
            r = self.items_map[item_id].set_partial_result(item_id=item_id, result=result)
            logger.debug("Set result for result %s: %s", self.items_map[item_id], r)

    def _select_func(self, q_len) -> WorkerFunc[T, U]:
        if self.single_form is None:
            self.multiple_form = cast(WorkerFunc, self.multiple_form)
            return self.multiple_form
        if self.multiple_form is None:
            self.single_form = cast(WorkerFunc, self.single_form)
            return self.single_form
        self.single_form = cast(WorkerFunc, self.single_form)
        self.multiple_form = cast(WorkerFunc, self.multiple_form)
        if self.batch_max_size is not None:
            q_len = min(q_len, self.batch_max_size)
        cost_multiple = (
            self.worker_func_multiple_fixed_cost + self.worker_func_multiple_cost * q_len
        )
        cost_single = self.worker_func_single_cost * q_len
        if cost_multiple < cost_single:
            return self.multiple_form
        else:
            return self.single_form

    @overload
    def process(self, item: Collection[T], timeout: float | None = None) -> list[U]: ...

    @overload
    def process(self, item: T, timeout: float | None = None) -> U: ...

    def process(self, item, timeout: float | None = None) -> U | list[U] | None:
        if isinstance(item, Collection) and hasattr(item, "__len__") and len(item) == 0:
            return []
        if item is None:
            return None

        r: BatchedQueueResult[U] = self.put(item)
        logger.debug(
            "Process result  %s from %s",
            r,
            f"len: {len(item)}" if isinstance(item, Collection) else item,
        )
        result: U | list[U] | None
        try:
            result = r.get_result(timeout=timeout)
        except TimeoutError:
            logger.warning(
                "%s, %s, %s, %s, %s,%s",
                self._q_ready.is_set(),
                len(self.to_process_q),
                len(self._futures),
                [f.done() for f in self._futures],
                r.finished,
                self._process_q_lock.locked(),
            )
            logger.error("Timed out waiting for result from %s", r)
            raise

        result_list: list[U | None]
        if not isinstance(result, list):
            result_list = [result]
        else:
            result_list = cast(list[U | None], result)
        for res in result_list:
            if isinstance(res, Exception):
                logger.exception(res, exc_info=res)
        if all(isinstance(res, BaseException) for res in result_list):
            rl = cast(BaseException, result_list[0])
            raise rl
        logger.debug("Got result from %s", r)
        self._delete_result(r)
        return result

    def _delete_result(self, result: BatchedQueueResult[U]):
        # noinspection PyProtectedMember
        for i in result._item_ids:
            if i in self.items_map:
                del self.items_map[i]
        del result

    def _get_for_processing(self) -> tuple[list[int], list[T]]:
        to_process = []
        to_process_ids = []
        while True:
            try:
                item_id, item = self.to_process_q.popleft()
            except IndexError:
                break
            to_process.append(item)
            to_process_ids.append(item_id)
            if self.batch_max_size is not None and len(to_process) >= self.batch_max_size:
                break

        return to_process_ids, to_process
