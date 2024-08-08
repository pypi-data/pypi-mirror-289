import cython

cdef class Incrementer:  # noqa: E999
    """
    implements a simple incrementer that wraps around at 2**32 - 1
    Uint32 overflow effectively
    """
    cdef unsigned int _value

    def __init__(self, initial_value: cython.uint = 0):
        self._value = initial_value

    def increment(self) -> cython.uint:
        self._value += 1
        return self._value

    @property
    def value(self) -> cython.uint:
        return self._value
