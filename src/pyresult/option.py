from typing import Generic, TypeVar, Callable, cast

T = TypeVar("T")
U = TypeVar("U")

class Option(Generic[T]):
    def is_some(self) -> bool:
        return isinstance(self, Some)

    def is_none(self) -> bool:
        return isinstance(self, None_)

    def unwrap(self) -> T:
        if self.is_some():
            return cast(T, self.value)
        raise ValueError("Called unwrap() on a None")

    def unwrap_or(self, default: T) -> T:
        if self.is_some():
            return cast(T, self.value)
        return default

    def map(self, f: Callable[[T], U]) -> "Option[U]":
        if self.is_some():
            return Some(f(cast(T, self.value)))
        return cast("Option[U]", self)

    def and_then(self, f: Callable[[T], "Option[U]"]) -> "Option[U]":
        if self.is_some():
            return f(cast(T, self.value))
        return cast("Option[U]", self)

    def filter(self, predicate: Callable[[T], bool]) -> "Option[T]":
        if self.is_some() and predicate(cast(T, self.value)):
            return self
        return None_()

    def map_or(self, default: U, f: Callable[[T], U]) -> U:
        if self.is_some():
            return f(cast(T, self.value))
        return default

    def expect(self, msg: str) -> T:
        if self.is_some():
            return cast(T, self.value)
        raise ValueError(msg)

class Some(Option[T]):
    __match_args__ = ("value",)

    def __init__(self, value: T):
        self.value = value

    def __repr__(self) -> str:
        return f"Some({self.value!r})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Some):
            return self.value == other.value
        return False

class None_(Option[T]):
    def __repr__(self) -> str:
        return "None"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, None_)
