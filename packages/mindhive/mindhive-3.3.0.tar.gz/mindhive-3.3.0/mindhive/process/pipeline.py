import logging
from abc import ABC
from collections import Counter
from threading import RLock
from typing import Any, overload

from .consumer import Consumer
from .consumer_processor import ConsumerProcessor
from .data_vehicle import DataContext, DataVehicle
from .pipeline_component import PipelineComponent
from .producer import DataListener, Producer, CompletedCallback
from .queue_processor import QueueConsumerProcessor, QueueTransformerProcessor
from .transformer import Transformer
from .transformer_processor import TransformerProcessor
from .worker import Worker
from ..log.metrics import metrics

type ConsumerOrProcessor[D] = Consumer[D] | ConsumerProcessor[D]
type TransformerOrProcessor[D, R] = Transformer[D, R] | TransformerProcessor[D, R]
type PipelineArg[D] = ConsumerOrProcessor[D] | TransformerOrProcessor[D, Any]


class _ContextTracker:
    def __init__(self, differentiator: str):
        self.log = logging.getLogger(f"{self.__class__.__name__}.{differentiator}")
        self.tags = [f"pipeline:{differentiator}"]
        self.context_ref_counter = Counter()
        self.context_map_completed: dict[DataContext, CompletedCallback] = {}
        self._lock = RLock()

    def add_reference(self, context: DataContext, completed: CompletedCallback | None):
        if self.log.isEnabledFor(logging.DEBUG):
            self.log.debug(f"Adding reference: {id(context)}")
        with self._lock:
            assert context not in self.context_ref_counter
            self.context_ref_counter[context] = 1
            if completed is not None:
                self.context_map_completed[context] = completed
            total_ref_count = self.context_ref_counter.total()
        self._record_ref_count_metrics(total_ref_count)

    def inc_reference(self, context: DataContext):
        with self._lock:
            is_adding = context not in self.context_ref_counter
            self.context_ref_counter[context] += 1
            total_ref_count = self.context_ref_counter.total()
        if self.log.isEnabledFor(logging.DEBUG):
            if is_adding:
                self.log.debug(f"Adding reference assumed generated part way through pipeline: {id(context)}")
            else:
                self.log.debug(f"Incrementing reference: {id(context)}")
        self._record_ref_count_metrics(total_ref_count)

    def dec_reference(self, context: DataContext):
        if self.log.isEnabledFor(logging.DEBUG):
            self.log.debug(f"Decrementing reference: {id(context)}")
        with self._lock:
            assert context in self.context_ref_counter
            if self.context_ref_counter[context] == 1:
                is_complete = True
                completed = self.context_map_completed.pop(context, None)
                del self.context_ref_counter[context]
            else:
                is_complete = False
                completed = None
                self.context_ref_counter[context] -= 1
            total_ref_count = self.context_ref_counter.total()
        if is_complete:
            if self.log.isEnabledFor(logging.DEBUG):
                self.log.debug(f"Completed reference: {id(context)}, {'with' if completed else 'without'} callback")
            if completed:
                completed()
        self._record_ref_count_metrics(total_ref_count)

    def _record_ref_count_metrics(self, total_ref_count: float):
        sample_rate = None if total_ref_count == 0 else 0.1  # Ensure we always report zero
        metrics.gauge("process.pipeline.context_tracker.total_ref_count", total_ref_count, self.tags, sample_rate)


class _TrackingProducerWrapper(Producer, ABC):
    def __init__(self, wrapped: Producer, tracker: _ContextTracker):
        self.wrapped_producer = wrapped
        self.tracker = tracker

    @property
    def name(self) -> str:
        return f"{self.wrapped_producer.name}.{self.__class__.__name__}"


class _CaptureContextProducerWrapper(_TrackingProducerWrapper):
    def send_to(self, listener: DataListener):
        def wrapped_listener(dv: DataVehicle, completed: CompletedCallback | None):
            def dec_reference():
                # Don't call original completed, that is job of tracker
                self.tracker.dec_reference(dv.context)

            self.tracker.add_reference(dv.context, completed)
            listener(dv, dec_reference)

        return self.wrapped_producer.send_to(wrapped_listener)


class _LinkContextProducerWrapper(_TrackingProducerWrapper):
    def send_to(self, listener: DataListener):
        def wrapped_listener(dv: DataVehicle, completed: CompletedCallback | None):
            def wrapped_completed():
                if completed:
                    completed()
                self.tracker.dec_reference(dv.context)

            self.tracker.inc_reference(dv.context)
            listener(dv, wrapped_completed)

        return self.wrapped_producer.send_to(wrapped_listener)


class PipelineConsumerProcessor[D](PipelineComponent, ConsumerProcessor[D]):
    @overload
    def __init__(
        self,
        worker1: ConsumerOrProcessor[D],
        /,
    ) -> None: ...

    @overload
    def __init__[D2](self, worker1: TransformerOrProcessor[D, D2], worker2: ConsumerOrProcessor[D2], /) -> None: ...

    @overload
    def __init__[
        D2, D3
    ](
        self,
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: ConsumerOrProcessor[D3],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4
    ](
        self,
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: ConsumerOrProcessor[D4],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4, D5
    ](
        self,
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: TransformerOrProcessor[D4, D5],
        worker5: ConsumerOrProcessor[D5],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4, D5, D6
    ](
        self,
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: TransformerOrProcessor[D4, D5],
        worker5: TransformerOrProcessor[D5, D6],
        worker6: ConsumerOrProcessor[D6],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4, D5, D6, D7
    ](
        self,
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: TransformerOrProcessor[D4, D5],
        worker5: TransformerOrProcessor[D5, D6],
        worker6: TransformerOrProcessor[D6, D7],
        worker7: ConsumerOrProcessor[D7],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4, D5, D6, D7, D8
    ](
        self,
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: TransformerOrProcessor[D4, D5],
        worker5: TransformerOrProcessor[D5, D6],
        worker6: TransformerOrProcessor[D6, D7],
        worker7: TransformerOrProcessor[D7, D8],
        worker8: ConsumerOrProcessor[D8],
        /,
    ) -> None: ...

    @overload
    def __init__(
        self,
        first_worker: PipelineArg[D],
        /,
        *tail_workers: PipelineArg,
    ) -> None: ...

    def __init__(
        self,
        first_worker: PipelineArg[D],
        *tail_workers: PipelineArg,
    ) -> None:
        super().__init__()
        workers: list[PipelineArg] = [first_worker, *tail_workers]
        self.__differentiator = workers[0].name
        self._tracker = _ContextTracker(self.name)
        self._processors: list[ConsumerProcessor | TransformerProcessor] = []
        for i, worker in enumerate(workers):
            if isinstance(worker, ConsumerProcessor):
                processor = worker
            else:
                if i < len(workers) - 1:
                    if not isinstance(worker, Transformer):
                        raise RuntimeError(f"Worker index: {i} of type {type(worker)} is not a {Transformer}")
                    processor = QueueTransformerProcessor(worker)
                else:
                    processor = self._create_tail_processor(worker)
            self._processors.append(processor)
        for producer, consumer in zip(self._processors[:-1], self._processors[1:]):
            assert isinstance(producer, Producer)
            consumer.receive_from(_LinkContextProducerWrapper(producer, self._tracker))

    @property
    def differentiator(self) -> str | None:
        return self.__differentiator

    def receive_from(self, producer: Producer[D]):
        self._processors[0].receive_from(_CaptureContextProducerWrapper(producer, self._tracker))

    def _create_tail_processor(self, worker: Worker) -> ConsumerProcessor:
        if not isinstance(worker, Consumer):
            raise RuntimeError(f"Tail worker of type {type(worker)} is not a {Consumer}")
        return QueueConsumerProcessor(worker)


class PipelineTransformerProcessor[D, R](PipelineConsumerProcessor[D], TransformerProcessor[D, R]):
    @overload
    def __init__(
        self,
        worker1: TransformerOrProcessor[D, R],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2
    ](self, worker1: TransformerOrProcessor[D, D2], worker2: TransformerOrProcessor[D2, R], /) -> None: ...

    @overload
    def __init__[
        D2, D3
    ](
        self,
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, R],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4
    ](
        self,
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: TransformerOrProcessor[D4, R],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4, D5
    ](
        self,
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: TransformerOrProcessor[D4, D5],
        worker5: TransformerOrProcessor[D5, R],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4, D5, D6
    ](
        self,
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: TransformerOrProcessor[D4, D5],
        worker5: TransformerOrProcessor[D5, D6],
        worker6: TransformerOrProcessor[D6, R],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4, D5, D6, D7
    ](
        self,
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: TransformerOrProcessor[D4, D5],
        worker5: TransformerOrProcessor[D5, D6],
        worker6: TransformerOrProcessor[D6, D7],
        worker7: TransformerOrProcessor[D7, R],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4, D5, D6, D7, D8
    ](
        self,
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: TransformerOrProcessor[D4, D5],
        worker5: TransformerOrProcessor[D5, D6],
        worker6: TransformerOrProcessor[D6, D7],
        worker7: TransformerOrProcessor[D7, D8],
        worker8: TransformerOrProcessor[D8, R],
        /,
    ) -> None: ...

    @overload
    def __init__(
        self,
        first_worker: PipelineArg[D],
        /,
        *tail_workers: PipelineArg,
    ) -> None: ...

    def __init__(
        self,
        first_worker: PipelineArg[D],
        /,
        *tail_workers: PipelineArg,
    ) -> None:
        super().__init__(first_worker, *tail_workers)

    def _create_tail_processor(self, worker: Worker) -> ConsumerProcessor:
        if not isinstance(worker, Transformer):
            raise RuntimeError(f"Tail worker of type {type(worker)} is not a {Transformer}")
        return QueueTransformerProcessor(worker)

    def send_to(self, listener: DataListener[R]):
        tail_processor = self._processors[-1]
        assert isinstance(tail_processor, TransformerProcessor)
        tail_processor.send_to(listener)


class ProducerPipelineConsumerProcessor[D](PipelineComponent):
    @overload
    def __init__(
        self,
        producer: Producer[D],
        worker1: ConsumerOrProcessor[D],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2
    ](
        self,
        producer: Producer[D],
        worker1: TransformerOrProcessor[D, D2],
        worker2: ConsumerOrProcessor[D2],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3
    ](
        self,
        producer: Producer[D],
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: ConsumerOrProcessor[D3],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4
    ](
        self,
        producer: Producer[D],
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: ConsumerOrProcessor[D4],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4, D5
    ](
        self,
        producer: Producer[D],
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: TransformerOrProcessor[D4, D5],
        worker5: ConsumerOrProcessor[D5],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4, D5, D6
    ](
        self,
        producer: Producer[D],
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: TransformerOrProcessor[D4, D5],
        worker5: TransformerOrProcessor[D5, D6],
        worker6: ConsumerOrProcessor[D6],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4, D5, D6, D7
    ](
        self,
        producer: Producer[D],
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: TransformerOrProcessor[D4, D5],
        worker5: TransformerOrProcessor[D5, D6],
        worker6: TransformerOrProcessor[D6, D7],
        worker7: ConsumerOrProcessor[D7],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4, D5, D6, D7, D8
    ](
        self,
        producer: Producer[D],
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: TransformerOrProcessor[D4, D5],
        worker5: TransformerOrProcessor[D5, D6],
        worker6: TransformerOrProcessor[D6, D7],
        worker7: TransformerOrProcessor[D7, D8],
        worker8: ConsumerOrProcessor[D8],
        /,
    ) -> None: ...

    @overload
    def __init__(
        self,
        producer: Producer[D],
        first_worker: PipelineArg[D],
        /,
        *tail_workers: PipelineArg,
    ) -> None: ...

    def __init__(
        self,
        producer: Producer[D],
        first_worker: PipelineArg[D],
        /,
        *tail_workers: PipelineArg,
    ) -> None:
        super().__init__()
        self.producer = producer
        self.pipeline = PipelineConsumerProcessor(first_worker, *tail_workers)
        self.pipeline.receive_from(producer)

    @property
    def differentiator(self) -> str | None:
        return self.producer.name


class ProducerPipelineTransformerProcessor[D, R](PipelineComponent, Producer[R]):
    @overload
    def __init__(
        self,
        producer: Producer[D],
        worker1: TransformerOrProcessor[D, R],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2
    ](
        self,
        producer: Producer[D],
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, R],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3
    ](
        self,
        producer: Producer[D],
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, R],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4
    ](
        self,
        producer: Producer[D],
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: TransformerOrProcessor[D4, R],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4, D5
    ](
        self,
        producer: Producer[D],
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: TransformerOrProcessor[D4, D5],
        worker5: TransformerOrProcessor[D5, R],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4, D5, D6
    ](
        self,
        producer: Producer[D],
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: TransformerOrProcessor[D4, D5],
        worker5: TransformerOrProcessor[D5, D6],
        worker6: TransformerOrProcessor[D6, R],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4, D5, D6, D7
    ](
        self,
        producer: Producer[D],
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: TransformerOrProcessor[D4, D5],
        worker5: TransformerOrProcessor[D5, D6],
        worker6: TransformerOrProcessor[D6, D7],
        worker7: TransformerOrProcessor[D7, R],
        /,
    ) -> None: ...

    @overload
    def __init__[
        D2, D3, D4, D5, D6, D7, D8
    ](
        self,
        producer: Producer[D],
        worker1: TransformerOrProcessor[D, D2],
        worker2: TransformerOrProcessor[D2, D3],
        worker3: TransformerOrProcessor[D3, D4],
        worker4: TransformerOrProcessor[D4, D5],
        worker5: TransformerOrProcessor[D5, D6],
        worker6: TransformerOrProcessor[D6, D7],
        worker7: TransformerOrProcessor[D7, D8],
        worker8: TransformerOrProcessor[D8, R],
        /,
    ) -> None: ...

    @overload
    def __init__(
        self,
        producer: Producer[D],
        first_worker: PipelineArg[D],
        /,
        *tail_workers: PipelineArg,
    ) -> None: ...

    def __init__(
        self,
        producer: Producer[D],
        first_worker: PipelineArg[D],
        /,
        *tail_workers: PipelineArg,
    ) -> None:
        super().__init__()
        self.producer = producer
        self.pipeline = PipelineTransformerProcessor(first_worker, *tail_workers)
        self.pipeline.receive_from(producer)

    @property
    def differentiator(self) -> str | None:
        return self.producer.name

    def send_to(self, listener: DataListener[R]):
        self.pipeline.send_to(listener)
