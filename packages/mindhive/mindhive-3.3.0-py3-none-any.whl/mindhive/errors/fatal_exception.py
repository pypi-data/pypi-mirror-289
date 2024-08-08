from typing import Sequence


def resolve_msg(msg: Sequence[str] | str = ""):
    return msg if isinstance(msg, str) else "\n".join(msg)


class FatalException(RuntimeError):
    def __init__(self, title: str, msg: Sequence[str] | str = "") -> None:
        super().__init__(title)
        self.title = title
        self.msg = resolve_msg(msg)
