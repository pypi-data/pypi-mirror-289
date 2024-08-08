import logging

import gc
from time import monotonic

from .metrics import metrics

log = logging.getLogger("gc_metrics")


class GcMonitoring:
    def __init__(self) -> None:
        self.start_ts: float | None = None
        self.generations = len(gc.get_count())

    def callback(self, phase, info):
        generation = info["generation"]
        if log.isEnabledFor(logging.DEBUG):
            log.debug(f"Phase {phase}, generation {generation}")
        if phase == "start":
            self.start_ts = monotonic()
        elif phase == "stop":
            if self.start_ts is None:
                log.error("No start / out of sequence")
                return
            elapsed = monotonic() - self.start_ts
            tags = [f"generation:{generation}"]
            metrics.increment("gc.count")
            metrics.increment("gc.time", elapsed, tags)
            metrics.increment("gc.collected_objs", info["collected"], tags)
            if generation >= (self.generations - 2):
                for gen, count in enumerate(gc.get_count()):
                    metrics.gauge(f"gc.generation_{gen}.objs", count)
            self.start_ts = None


_gc_monitoring = GcMonitoring()


def init_gc_metrics():
    if _gc_monitoring.callback not in gc.callbacks:
        gc.callbacks.append(_gc_monitoring.callback)
