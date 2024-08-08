import string as _string
from enum import Enum
from random import choice, choices, randint, random, sample
from typing import Callable, Collection, Sequence, Type


def positive_int(high=100) -> int:
    return randint(1, high)


def int_between(low, high) -> int:
    return randint(low, high)


def positive_fraction() -> float:
    result = None
    while not result:
        result = random()
    return result


def float_between(low, high_exclusive) -> float:
    return random() * (high_exclusive - low) + low


def string(length=5) -> str:
    return "".join(choices(_string.ascii_letters + _string.digits, k=length))


def boolean() -> bool:
    return randint(0, 1) == 1


def sequence_of[T](value_func: Callable[[], T], min_num=1, max_num=3) -> Sequence[T]:
    return [value_func() for _ in range(int_between(min_num, max_num))]


def one[T](collection: Collection[T]) -> T:
    return choice(tuple(collection))


def of[T](collection: Collection[T], min_num=0, max_num: int | None = None) -> list[T]:
    k = int_between(min_num, len(collection) if max_num is None else max_num)
    if k == 0:
        return []
    return sample(tuple(collection), k)


def enum[E: Enum](collection: Type[E]) -> E:
    return choice(tuple(collection))
