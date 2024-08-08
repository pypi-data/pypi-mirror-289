import logging
from pathlib import Path
from threading import Event
from time import sleep

from ..log.trace import tracer
from ..process.thread import start_thread

HEALTHCHECK_PATH = Path("/tmp/healthcheck")
OLD_HEALTHCHECK_PATH = Path("/tmp/grader-healthcheck")  # REMOVE: once all using new code and probe changed in k8s


class Healthcheck:
    def __init__(self, debounce_interval: float = 1):
        self.debounce_interval = debounce_interval
        self.log = logging.getLogger(self.__class__.__name__)
        self._event = Event()
        start_thread(self.log, self._worker)

    def alive_poll(self):
        self._event.set()

    def _worker(self):
        while True:
            self._event.wait()
            self.log.debug("Triggered")
            self._event.clear()
            with tracer.trace("healthcheck_with_trigger"):
                self._notify_external()
            sleep(self.debounce_interval)

    def _notify_external(self):
        HEALTHCHECK_PATH.touch()
        OLD_HEALTHCHECK_PATH.touch()
