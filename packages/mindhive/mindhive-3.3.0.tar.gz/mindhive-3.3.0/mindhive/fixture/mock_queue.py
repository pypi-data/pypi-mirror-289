from queue import Queue, Empty
from typing import Self

TIMEOUT = object()


class MockQueue(Queue):
    instances: list[Self] = []

    def __init__(self):
        super().__init__()
        MockQueue.instances.append(self)

    def mock_timeout(self):
        self.put(TIMEOUT)

    def get(self, block=True, timeout=None):
        result = super().get(block, timeout)
        if result is TIMEOUT:
            assert timeout is not None
            raise Empty()
        return result

    @staticmethod
    def mock_clear():
        MockQueue.instances.clear()
