from time import monotonic

from threading import RLock


class TimeTracker:
    def __init__(self) -> None:
        self.lock = RLock()
        self.time = 0
        self.from_timestamp = None

    def increment(self, time: float):
        with self.lock:
            self.time += time

    def start(self):
        with self.lock:
            if not self.from_timestamp:
                self.from_timestamp = monotonic()

    def stop(self):
        with self.lock:
            if self.from_timestamp:
                self.increment(monotonic() - self.from_timestamp)
                self.from_timestamp = None

    def poll(self) -> float:
        with self.lock:
            if self.from_timestamp:
                now = monotonic()
                self.increment(now - self.from_timestamp)
                self.from_timestamp = now
            result = self.time
            self.time = 0
            return result
