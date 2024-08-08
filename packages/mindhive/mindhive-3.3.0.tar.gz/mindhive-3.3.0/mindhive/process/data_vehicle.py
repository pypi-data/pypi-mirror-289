import logging
from collections import Counter
from contextlib import contextmanager
from threading import local, RLock
from typing import Mapping, Self, Any

from ddtrace import Span

from ..log.metrics import metrics
from ..log.trace import tracer

_log = logging.getLogger("data_vehicle")


class _LongLivedSpan:
    def __init__(self, parent: Self | None, name: str, start_time: float | None = None) -> None:
        self._lock = RLock()
        self.parent = parent
        self._name = name
        self._start_time = start_time
        self._pending_tags: dict[str, str] = {}
        self._span: Span | None = None
        self._ref_count = 0

    @property
    def span(self) -> Span:
        with self._lock:
            if self._span is None:
                raise RuntimeError("Attempt to access span before incremented")
            return self._span

    def set_tags(self, tags: Mapping[str, str]):
        with self._lock:
            if self._span is not None:
                self._span.set_tags(tags)  # pyright: ignore [reportArgumentType]
            else:
                self._pending_tags.update(tags)
                self._pending_tags.clear()

    def _ensure_span(self):
        with self._lock:
            if self._span is None:
                if self.parent:
                    if not self.parent._span:
                        raise RuntimeError(f"Can't start: {self} when parent: {self.parent} has not been started")
                    child_of = self.parent.span
                else:
                    child_of = None
                if tracer.context_provider.active() is not None:
                    raise RuntimeError(f"Should not be in an execution context: {tracer.context_provider.active()}")
                self._span = tracer.start_span(
                    self._name, child_of=child_of, activate=False
                )  # pyright: ignore [reportCallIssue]
                if self._start_time:
                    self._span.start = self._start_time
                if self._pending_tags:
                    self._span.set_tags(self._pending_tags)  # pyright: ignore [reportArgumentType]
                self._ref_count = 0

    def inc_reference(self):
        if self.parent:
            self.parent.inc_reference()
        with self._lock:
            if self._span and self._span.finished:
                raise RuntimeError(f"Attempting to inc_reference() on finished span: {self}")
            self._ensure_span()
            self._ref_count += 1

    def dec_reference(self):
        with self._lock:
            if self._ref_count <= 0:
                raise RuntimeError(f"Reference count mismatch: {self}")
            self._ref_count -= 1
            if self._span and self._ref_count == 0:
                self._span.finish()
        if self.parent:
            self.parent.dec_reference()

    def __repr__(self):
        if self._span:
            return f"LLS({self._span})"
        return f"LLS({self._name}, ref={self._ref_count})"

    def __del__(self):
        if self._span and self._ref_count > 0:
            _log.error(f"Allocated span: {self} still has ref_count: {self._ref_count} when not referenced")


class DataContext:
    _global_lock = RLock()
    _global_ref_count = 0
    _thread_local = local()

    def __init__(self, span: _LongLivedSpan | None):
        self._ll_span: _LongLivedSpan | None = span

    @staticmethod
    def _update_global_ref_metric(delta: int):
        with DataContext._global_lock:
            DataContext._global_ref_count += delta
            log_value = DataContext._global_ref_count
        sample_rate = None if log_value == 0 else 0.1  # Ensure we always report zero
        metrics.gauge("data_vehicle.context.ref_count.total", log_value, sample_rate=sample_rate)

    @property
    def _thread_context_counter(self) -> Counter[Self]:
        try:
            return DataContext._thread_local.context_counter
        except AttributeError:
            result = Counter()
            DataContext._thread_local.context_counter = result
            return result

    def start_child_context(self, name: str, start_time: float | None = None) -> Self:
        return self.__class__(_LongLivedSpan(self._ll_span, name, start_time))

    def set_tags(self, tags: Mapping[str, str]):
        if not self._ll_span:
            raise RuntimeError("Can't set_tags when no span")
        self._ll_span.set_tags(tags)

    def inc_reference(self):
        if self._ll_span:
            self._ll_span.inc_reference()
            DataContext._update_global_ref_metric(+1)

    def dec_reference(self):
        if self._ll_span:
            self._ll_span.dec_reference()
            DataContext._update_global_ref_metric(-1)

    def ensure_started_from(self, parent_context: Self):
        if not self._ll_span:
            raise RuntimeError(f"Expected: {self} to have been started")
        if self._ll_span.parent != parent_context._ll_span:
            raise RuntimeError(f"Expected: {self._ll_span} to have been started from: {parent_context._ll_span}")

    def __enter__(self):
        if self not in self._thread_context_counter:
            if self._ll_span:
                tracer.context_provider.activate(self._ll_span.span)
            else:
                tracer.context_provider.activate(None)
        self._thread_context_counter[self] += 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._thread_context_counter[self] > 1:
            self._thread_context_counter[self] -= 1
        else:
            del self._thread_context_counter[self]
            tracer.context_provider.activate(None)


class DataVehicle[D]:
    def __init__(self, data: D, continue_context: "DataVehicle[Any] | DataContext | None" = None) -> None:
        self.data = data
        if continue_context is None:
            self.context = DataContext(None)
        else:
            if isinstance(continue_context, DataVehicle):
                self.context = continue_context.context
            else:
                self.context = continue_context

    @contextmanager
    def wrap_execution(self, trace_name: str):
        with self.context:
            with tracer.trace(trace_name):
                try:
                    yield self
                except:  # noqa
                    _log.exception(f"Error in: {trace_name} handling: {self}")
                    raise

    def __repr__(self) -> str:
        return f"DV({self.data.__repr__()})"
