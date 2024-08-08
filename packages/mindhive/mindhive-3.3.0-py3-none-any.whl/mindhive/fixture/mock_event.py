from threading import Event
from typing import Self

DEFAULT_TIMEOUT = 0.5


class MockEvent(Event):
    instances: list[Self] = []

    def __init__(self):
        super().__init__()
        MockEvent.instances.append(self)
        self._waiting_event = Event()

    def wait(self, timeout: float | None = None) -> bool:
        self._waiting_event.set()
        try:
            return super().wait(timeout)
        finally:
            self._waiting_event.clear()

    def given_waiting(self, timeout=DEFAULT_TIMEOUT):
        is_waiting = self._waiting_event.wait(timeout)
        assert is_waiting

    @staticmethod
    def mock_teardown():
        MockEvent.instances.clear()
