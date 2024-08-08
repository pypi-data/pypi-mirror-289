import logging
from contextlib import contextmanager
from dataclasses import dataclass
from threading import RLock, Event
from unittest.mock import MagicMock

from . import some

DEFAULT_TIMEOUT = 0.5


class MockTime:
    def __init__(self) -> None:
        self.log = logging.getLogger(self.__class__.__name__)
        self.time_value = some.positive_int()
        self.monotonic_value = some.positive_int()

    def time(self) -> float:
        return self.time_value

    def monotonic(self) -> float:
        return self.monotonic_value

    def set_time(self, time: float):
        self.time_value = time

    def set_monotonic(self, monotonic: float):
        self.monotonic_value = monotonic

    def time_passes(self, time: float):
        self.log.debug(f"Time passing: {time}s")
        self.time_value += time
        self.monotonic_value += time

    @contextmanager
    def time_in_the_past(self, time: float):
        self.time_passes(-time)
        try:
            yield self
        finally:
            self.time_passes(time)


class SleepPassesTimeMockTime(MockTime):
    def __init__(self) -> None:
        super().__init__()
        self.sleep = MagicMock(side_effect=self.time_passes)


@dataclass
class Sleep:
    end_monotonic_ts: float
    event: Event


class TestPassesSleepTimeMockTime(MockTime):
    def __init__(self) -> None:
        super().__init__()
        self._lock = RLock()
        self._sleeping: list[Sleep] = []
        self._teardown = False
        self._any_sleeping = Event()

    def given_sleeping(self, timeout=DEFAULT_TIMEOUT):
        is_sleeping = self._any_sleeping.wait(timeout)
        assert is_sleeping

    def mock_teardown(self):
        self._teardown = True
        self._lock = RLock()
        for sleep in self._sleeping:
            if sleep.event.is_set():
                self.log.warning("Ending sleep wait in teardown")
                sleep.event.set()

    def sleep(self, time: float):
        if time < 0:
            raise ValueError("sleep length must be non-negative")
        sleep = Sleep(self.monotonic() + time, Event())
        with self._lock:
            self._sleeping.append(sleep)
            self._any_sleeping.set()
        self.log.debug(f"Starting sleep wait")
        sleep.event.wait()
        with self._lock:
            self._sleeping.remove(sleep)
            if not self._sleeping:
                self._any_sleeping.clear()
        if self._teardown:
            raise RuntimeError("Still sleeping when test teardown")

    def time_passes(self, time: float):
        super().time_passes(time)
        with self._lock:
            for sleep in self._sleeping:
                if self.monotonic() >= sleep.end_monotonic_ts:
                    self.log.debug(f"Sleep complete")
                    sleep.event.set()
                else:
                    self.log.debug(f"Sleep not complete")
