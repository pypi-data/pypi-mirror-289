import logging
from abc import abstractmethod
from dataclasses import dataclass
from threading import RLock
from typing import Callable, Collection

from ..log.metrics import metrics
from .consumer import Consumer
from .data_vehicle import DataVehicle
from .producer import Producer, ProducerImpl
from .queue_processor import QueueConsumerProcessor

type PopCallback = Callable[[DataVehicle], None]
type QueueSizeListener = Callable[[int], None]


@dataclass
class _QueueTask:
    dv: DataVehicle
    on_pop: PopCallback


class SourceQueue:
    def __init__(self, producer: Producer, differentiator: str, max_backlog=5):
        self.producer = producer
        self.differentiator = differentiator
        self.log = logging.getLogger(f"{self.__class__.__name__}.{differentiator}")
        self.max_backlog = max_backlog
        self._tasks: list[_QueueTask] = []
        self._queue_size_listeners: list[QueueSizeListener] = []

    def _add(self, dv: DataVehicle, on_pop: PopCallback):
        self._tasks.append(_QueueTask(dv, on_pop))
        while len(self._tasks) > self.max_backlog:
            self._tasks.pop(0)
            self.log.info(f"Dropping one task as task queue has reached backlog limit: {self.max_backlog}")
        self._handle_queue_change()

    @property
    def has_data(self) -> bool:
        return bool(self._tasks)

    def __bool__(self):
        return self.has_data

    @property
    def head(self) -> DataVehicle:
        try:
            return self._tasks[0].dv
        except IndexError:
            raise RuntimeError("Empty")

    def pop(self) -> None:
        try:
            task = self._tasks.pop(0)
        except IndexError:
            raise RuntimeError("Empty")
        task.on_pop(task.dv)
        self._handle_queue_change()

    def add_queue_size_listener(self, listener: QueueSizeListener):
        self._queue_size_listeners.append(listener)

    def _handle_queue_change(self):
        queue_size = len(self._tasks)
        for listener in self._queue_size_listeners:
            listener(queue_size)


class ConvergenceProcessor[R](ProducerImpl[R]):
    def __init__(self, sources: Collection[SourceQueue]):
        super().__init__()
        self._lock = RLock()
        self._popped_dvs: list[DataVehicle] | None = None
        for source in sources:
            consumer = _SourceConsumer(self, source, f"{self.name}.{source.differentiator}")
            QueueConsumerProcessor(consumer).receive_from(source.producer)

    def converge(self):
        with self._lock:
            self._popped_dvs = []
            try:
                self._converge()
            finally:
                for dv in self._popped_dvs:
                    dv.context.dec_reference()
                self._popped_dvs = None

    @abstractmethod
    def _converge(self): ...

    def _pop_listener(self, dv: DataVehicle):
        if self._popped_dvs is None:
            raise RuntimeError("Don't pop() outside of _converge()")
        self._popped_dvs.append(dv)


class _SourceConsumer(Consumer):
    def __init__(self, convergence: ConvergenceProcessor, source: SourceQueue, differentiator: str) -> None:
        def report_metric(queue_size: int):
            metrics.gauge(f"convergence.source.queue_size", queue_size, tags=[f"convergence_source:{differentiator}"])

        super().__init__(differentiator)
        self.convergence = convergence
        self.source = source
        self.source.add_queue_size_listener(report_metric)

    def process(self, dv: DataVehicle) -> None:
        # noinspection PyProtectedMember
        with self.convergence._lock:
            dv.context.inc_reference()
            # noinspection PyProtectedMember
            self.source._add(dv, self.convergence._pop_listener)
            self.convergence.converge()
