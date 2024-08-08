import logging
from multiprocessing.dummy import RLock
from threading import Event
from typing import Callable

from time import sleep

from .thread import start_thread


class DelayedCallback:
    def __init__(
        self, callback: Callable[[], None], time_source: Callable[[], float], log: logging.Logger | None = None
    ) -> None:
        self.callback = callback
        self.time_source = time_source
        self.name = f"{self.__class__.__name__}.{log.name}" if log else self.__class__.__name__
        self.log = log or logging.getLogger(self.__class__.__name__)
        self.lock = RLock()
        self.scheduled = Event()
        self.end_time: float | None = None
        start_thread(self.log, self._worker)

    @property
    def is_scheduled(self) -> bool:
        return self.scheduled.is_set()

    def schedule_at(self, timestamp: float) -> None:
        with self.lock:
            if self.end_time is None or timestamp > self.end_time:
                self.end_time = timestamp
            self.scheduled.set()

    def schedule_in(self, time: float) -> None:
        self.schedule_at(self.time_source() + time)

    def _worker(self):
        while True:
            self.scheduled.wait()
            with self.lock:
                assert self.end_time is not None
                wait_time = self.end_time - self.time_source()
                if wait_time <= 0:
                    self.end_time = None
                    self.scheduled.clear()
                    self.log.debug("Firing callback")
                    self.callback()
                    continue
            sleep(wait_time)
