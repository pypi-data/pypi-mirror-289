from threading import Event, RLock

from .consumer import Consumer
from .consumer_processor import ConsumerProcessor
from .data_vehicle import DataVehicle
from .producer import CompletedCallback, DataListener, Producer, ProducerImpl
from .queue_processor import (
    QueueConsumerProcessor,
    QueueProcessorImpl,
)
from .transformer_processor import TransformerProcessor


class _ChildrenSource[R](Producer[R]):
    def __init__(self):
        super().__init__()
        self._listeners: list[DataListener[R]] = []

    @property
    def name(self) -> str:
        return self.__class__.__name__

    @property
    def child_count(self) -> int:
        return len(self._listeners)

    def send_to(self, listener: DataListener[R]):
        self._listeners.append(listener)

    def process_all(self, dv: DataVehicle[R], completed: CompletedCallback):
        for listener in self._listeners:
            listener(dv, completed)


class ParallelConsumersProcessor[D](QueueProcessorImpl):
    def __init__(self, *consumers: Consumer[D] | ConsumerProcessor[D]) -> None:
        super().__init__(consumers[0].name)
        self._children_source = _ChildrenSource[D]()
        for consumer in consumers:
            child = QueueConsumerProcessor.as_processor(consumer)
            child.receive_from(self._children_source)

    def _process(self, dv: DataVehicle[D]) -> None:
        def completed():
            nonlocal remaining
            with lock:
                remaining -= 1
                if not remaining:
                    done.set()

        done = Event()
        lock = RLock()
        remaining = self._children_source.child_count
        self._children_source.process_all(dv, completed)
        done.wait()


class ParallelConsumersIdentityTransformerProcessor[D](
    ParallelConsumersProcessor[D], ProducerImpl[D], TransformerProcessor[D, D]
):
    def _process(self, dv: DataVehicle[D]) -> None:
        super()._process(dv)
        self._push(dv)
