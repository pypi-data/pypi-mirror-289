import json
from enum import IntEnum

from time import time
from typing import Self

from ..log.timestamp import timestamp_to_iso


class IssuePriority(IntEnum):
    P1_CRITICAL = 1
    P2_ERROR = 2
    P3_WARNING = 3
    P4_WARNING = 4
    P5_INFO = 5


class Issue:
    def __init__(
        self,
        title: str,
        msg: str,
        priority: IssuePriority,
        timestamp: str | None = None,
    ):
        self.title = title
        self.msg = msg
        self.priority = priority
        self.timestamp = timestamp or timestamp_to_iso(time())

    def to_json(self) -> str:
        return json.dumps(
            {
                "title": self.title,
                "msg": self.msg,
                "priority": self.priority.value,
                "timestamp": self.timestamp,
            }
        )

    @classmethod
    def from_json(cls, val: bytes | str) -> Self:
        data = json.loads(val)
        return cls(data["title"], data["msg"], IssuePriority(data["priority"]), data["timestamp"])
