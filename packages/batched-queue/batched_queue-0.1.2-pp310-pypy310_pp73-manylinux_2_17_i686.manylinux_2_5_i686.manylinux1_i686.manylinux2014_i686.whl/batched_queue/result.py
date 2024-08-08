import logging
from threading import Event, Lock
from typing import Generic

from batched_queue.types import T

logger = logging.getLogger(__name__)


class QueueResult(Generic[T]):
    def __init__(self) -> None:
        super().__init__()
        self._result: T | list[T] | None = None
        self._event = Event()
        self._finished = False

    @property
    def finished(self) -> bool:
        return self._finished

    def set_result(self, result: T | list[T]) -> None:
        self._result = result
        self._finished = True
        self._event.set()

    def get_result(self, timeout: float | None = None) -> T | list[T] | None:
        r = self._event.wait(timeout)
        if not r:
            raise TimeoutError("Timed out waiting for result")
        return self._result

    def __del__(self):
        del self._result


class BatchedQueueResult(QueueResult[T]):
    def __init__(self, *, is_list: bool, _ids: list[int]):
        super().__init__()
        self._item_ids = _ids
        self._is_list = is_list
        self._er_lock = Lock()
        # we use ... to represent an unset value just in case a None is a valid result
        self._expected_results: dict[int, T | ...] = {k: ... for k in _ids}  # type: ignore[reportInvalidTypeForm]

    def set_partial_result(self, item_id: int, result: T) -> bool:
        if self._finished:
            raise ValueError("Already finished, shouldn't be setting partial result?")
        if item_id not in self._expected_results:
            raise ValueError(f"Invalid item id {item_id}")
        with self._er_lock:
            self._expected_results[item_id] = result
            return self.check_results_done()

    def check_results_done(self) -> bool:
        if any(v is ... for v in self._expected_results.values()):
            logger.debug("%s: %s", self, self._expected_results)
            return False
        items = [self._expected_results[k] for k in self._item_ids]
        if self._is_list:
            self.set_result(items)
        else:
            self.set_result(items[0])

        del self._expected_results
        return True
