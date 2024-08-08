from datetime import datetime


# noinspection PyPep8Naming
class anything:
    def __eq__(self, o: object) -> bool:
        return True

    __hash__ = None  # type: ignore

    def __repr__(self) -> str:
        return "<anything>"


# noinspection PyPep8Naming
class is_iso_timestamp:
    def __eq__(self, o: object) -> bool:
        if not isinstance(o, str):
            return False
        if not o.endswith("Z"):
            return False
        try:
            datetime.fromisoformat(o.replace("Z", "+00:00"))
        except ValueError:
            return False
        else:
            return True

    __hash__ = None  # type: ignore

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"


# noinspection PyPep8Naming
class unordered:
    def __init__(self, *values) -> None:
        self.collection = set(values)

    def __eq__(self, o: object) -> bool:
        return set(o) == self.collection  # pyright: ignore [reportArgumentType]

    __hash__ = None  # type: ignore

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.collection}>"


# noinspection PyPep8Naming
class non_empty_string:
    def __eq__(self, o: object) -> bool:
        return isinstance(o, str) and o != ""

    __hash__ = None  # type: ignore

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"


# noinspection PyPep8Naming
class contains:
    def __init__(self, value) -> None:
        self.value = value

    def __eq__(self, o: object) -> bool:
        return self.value in o

    __hash__ = None  # type: ignore

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.value!r}>"
