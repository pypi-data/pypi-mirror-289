import logging
from contextlib import AbstractContextManager
from time import monotonic
from typing import Callable


class TimingContextManager(AbstractContextManager):
    def __init__(self, log: logging.Logger, label: str) -> None:
        super().__init__()
        self.log = log
        self.label = label

    def __enter__(self):
        self.start = monotonic()
        if self.log.isEnabledFor(logging.DEBUG):
            self.log.debug(f"Starting {self.label}")
        return super().__enter__()

    def __exit__(self, exc_type, exc_value, traceback):
        if self.log.isEnabledFor(logging.DEBUG):
            elapsed = monotonic() - self.start
            if exc_type is None:
                prefix = "Finished"
            else:
                prefix = f"Finished (with {exc_type})"
            elapsed_nanos = elapsed * 1_000_000_000
            datadog_standard_duration = {"duration": int(elapsed_nanos)}
            self.log.debug(f"{prefix} {self.label} in {elapsed*1000:,.0f}ms", extra=datadog_standard_duration)


def timing_factory(log: logging.Logger) -> Callable[[str], TimingContextManager]:
    def timing(label: str):
        return TimingContextManager(log, label)

    return timing
