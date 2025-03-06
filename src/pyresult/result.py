from typing import Generic, TypeVar, Callable, cast

T = TypeVar("T")
E = TypeVar("E")
U = TypeVar("U")

class Result(Generic[T, E]):
    def is_ok(self) -> bool:
        return isinstance(self, Ok)

    def is_err(self) -> bool:
        return isinstance(self, Err)

    def unwrap(self) -> T:
        if self.is_ok():
            return cast(T, self.value)
        raise ValueError(f"Called unwrap() on an Err: {self.error}")

    def unwrap_or(self, default: T) -> T:
        if self.is_ok():
            return cast(T, self.value)
        return default

    def unwrap_err(self) -> E:
        if self.is_err():
            return cast(E, self.error)
        raise ValueError(f"Called unwrap_err() on an Ok: {self.value}")

    def map(self, f: Callable[[T], U]) -> "Result[U, E]":
        if self.is_ok():
            return Ok(f(cast(T, self.value)))
        return cast("Result[U, E]", self)

    def map_error(self, f: Callable[[E], U]) -> "Result[T, U]":
        if self.is_err():
            return Err(f(cast(E, self.error)))
        return cast("Result[T, U]", self)

    def and_then(self, f: Callable[[T], "Result[U, E]"]) -> "Result[U, E]":
        if self.is_ok():
            return f(cast(T, self.value))
        return cast("Result[U, E]", self)

    def or_else(self, f: Callable[[E], "Result[T, U]"]) -> "Result[T, U]":
        if self.is_err():
            return f(cast(E, self.error))
        return cast("Result[T, U]", self)

class Ok(Result[T, E]):
    __match_args__ = ("value",)

    def __init__(self, value: T):
        self.value = value

    def __repr__(self) -> str:
        return f"Ok({self.value!r})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Ok):
            return self.value == other.value
        return False

class Err(Result[T, E]):
    __match_args__ = ("error",)

    def __init__(self, error: E):
        self.error = error

    def __repr__(self) -> str:
        return f"Err({self.error!r})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Err):
            return self.error == other.error
        return False
