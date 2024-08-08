from abc import abstractmethod, ABC
from dataclasses import dataclass
from queue import Queue
from threading import Event, RLock

from ..log.metrics import metrics
from .consumer import Consumer
from .consumer_processor import ConsumerProcessor
from .data_vehicle import DataVehicle
from .pipeline_component import PipelineComponent
from .producer import CompletedCallback, Producer, ProducerImpl
from .thread import start_thread
from .transformer import Transformer
from .transformer_processor import TransformerProcessor


@dataclass
class QueueTask[D]:
    dv: DataVehicle[D]
    completed_callback: CompletedCallback | None = None

    def complete(self):
        if self.completed_callback:
            self.completed_callback()


class QueueProcessorImpl[D](PipelineComponent, ConsumerProcessor[D]):
    _global_task_count_lock = RLock()
    _processor_map_task_count: dict["QueueProcessorImpl", int] = {}

    def __init__(self, differentiator: str | None = None) -> None:
        super().__init__()
        self.__differentiator = differentiator
        self._queue: Queue[QueueTask | None] = Queue()
        self._stop = Event()
        self._was_warning = False
        self._have_upstream = False
        self.tags = [f"processor:{self.name}"]
        start_thread(self.log, self._run, self.stop)
        self._generate_metrics()

    @property
    def differentiator(self) -> str | None:
        return self.__differentiator

    def receive_from(self, producer: Producer[D]):
        producer.send_to(self._submit)
        self._have_upstream = True

    def _submit(self, dv: DataVehicle[D], completed_callback: CompletedCallback | None):
        dv.context.inc_reference()
        self._queue.put(QueueTask(dv, completed_callback))
        self._generate_metrics()

    def _run(self):
        sanity_check_done = False
        while True:
            item = self._queue.get()
            if sanity_check_done:
                self.sanity_check()
                sanity_check_done = True
            self._generate_metrics()
            if item is None or self._stop.is_set():
                return
            try:
                self._process(item.dv)
            finally:
                self._queue.task_done()
                item.complete()
                item.dv.context.dec_reference()

    @abstractmethod
    def _process(self, dv: DataVehicle[D]) -> None: ...

    @property
    def _backlog_warning_task_count(self) -> int:
        return 5

    def _generate_metrics(self):
        task_count = self._queue.unfinished_tasks
        excessive_task_count = task_count - (self._backlog_warning_task_count - 1)
        with QueueProcessorImpl._global_task_count_lock:
            QueueProcessorImpl._processor_map_task_count[self] = task_count
            global_task_count = sum(QueueProcessorImpl._processor_map_task_count.values())
        metrics.gauge("queue_processor.backlog", task_count, self.tags)
        metrics.gauge("queue_processor.backlog.excessive", excessive_task_count, self.tags)
        metrics.gauge("queue_processor.backlog.total", global_task_count)
        if excessive_task_count > 0:
            self.log.warning(f"Not keeping up, queue too long, items: {task_count}")
            self._was_warning = True
        else:
            if self._was_warning:
                self.log.info(f"Queue length ok, items: {task_count}")
            self._was_warning = False

    def sanity_check(self) -> None:
        super().sanity_check()
        if not self._have_upstream:
            raise RuntimeError(f"Not linked upstream: {self.name}")

    def stop(self):
        self._stop.set()
        self._queue.put(None)  # Ensure queue.get() returns


class QueueTransformerProcessorImpl[D, R](QueueProcessorImpl[D], ProducerImpl[R], TransformerProcessor[D, R], ABC):
    pass


class QueueConsumerProcessor[D](QueueProcessorImpl[D]):
    def __init__(self, consumer: Consumer[D]) -> None:
        super().__init__(differentiator=consumer.name)
        self.consumer = consumer

    @staticmethod
    def as_processor[D1](consumer: Consumer[D1] | ConsumerProcessor[D1]) -> ConsumerProcessor[D1]:
        if isinstance(consumer, ConsumerProcessor):
            return consumer
        return QueueConsumerProcessor(consumer)

    @staticmethod
    def _differentiator_is_entire_name() -> bool:
        return True

    def _process(self, dv: DataVehicle[D]) -> None:
        with dv.wrap_execution(self.consumer.trace_name):
            self.consumer.process(dv)


class QueueTransformerProcessor[D, R](QueueTransformerProcessorImpl[D, R]):
    def __init__(self, transformer: Transformer[D, R]) -> None:
        super().__init__(differentiator=transformer.name)
        self.transformer = transformer

    @staticmethod
    def as_processor[
        D1, R1
    ](transformer: Transformer[D1, R1] | TransformerProcessor[D1, R1],) -> TransformerProcessor[D1, R1]:
        if isinstance(transformer, TransformerProcessor):
            return transformer
        return QueueTransformerProcessor(transformer)

    @staticmethod
    def _differentiator_is_entire_name() -> bool:
        return True

    def _process(self, dv: DataVehicle[D]) -> None:
        with dv.wrap_execution(self.transformer.trace_name):
            self.transformer.process(dv, self._push)
