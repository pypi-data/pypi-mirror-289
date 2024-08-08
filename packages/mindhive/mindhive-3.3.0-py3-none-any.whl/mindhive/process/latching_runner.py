import logging
from datetime import timedelta
from typing import Callable

from time import monotonic

from .delayed_callback import DelayedCallback


class LatchingRunner:
    def __init__(self, set_on: Callable[[bool], None], run_time: timedelta) -> None:
        self.set_on = set_on
        self.run_time = run_time.total_seconds()
        self.log = logging.getLogger(self.__class__.__name__)
        self.stop_callback = DelayedCallback(self._stop, monotonic, self.log)

    @property
    def running(self):
        return self.stop_callback.is_scheduled

    def pulse(self) -> None:
        if not self.running:
            self.log.info("Starting")
            self.set_on(True)
        self.stop_callback.schedule_in(self.run_time)

    def _stop(self):
        self.log.info("Stopping")
        self.set_on(False)
