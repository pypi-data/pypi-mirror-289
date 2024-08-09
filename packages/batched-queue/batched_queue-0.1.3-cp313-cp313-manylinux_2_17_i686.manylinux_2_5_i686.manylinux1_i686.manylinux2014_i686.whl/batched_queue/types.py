from typing import Protocol, TypeVar

T = TypeVar("T")
U = TypeVar("U")
T_co = TypeVar("T_co", covariant=True)
T_cat = TypeVar("T_cat", contravariant=True)
List_T_co = list[T_co]
List_T_cat = list[T_cat]
U_co = TypeVar("U_co", covariant=True)
U_cat = TypeVar("U_cat", contravariant=True)
List_U_co = list[U_co]
List_U_cat = list[U_cat]


class BatchedQueueWorkerMultiple(Protocol[T, U]):
    def __call__(self, items: list[T], *args, **kwargs) -> list[U]: ...  # pragma: no cover


class BatchedQueueWorkerSingle(Protocol[T_cat, U_co]):
    def __call__(self, item: T_cat, *args, **kwargs) -> U_co: ...  # pragma: no cover


BQWorkerType = BatchedQueueWorkerMultiple | BatchedQueueWorkerSingle
