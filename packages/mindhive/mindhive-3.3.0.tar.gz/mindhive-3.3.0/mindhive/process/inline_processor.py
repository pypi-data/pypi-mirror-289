from abc import abstractmethod

from .consumer import Consumer
from .consumer_processor import ConsumerProcessor
from .data_vehicle import DataVehicle
from .producer import Producer, ProducerImpl, CompletedCallback
from .transformer import Transformer
from .transformer_processor import TransformerProcessor


class InlineConsumerProcessorImpl[D](ConsumerProcessor[D]):
    def __init__(self, differentiator: str):
        super().__init__()
        self.__differentiator = differentiator

    @property
    def name(self) -> str:
        return f"{self.__class__.__name__}.{self.__differentiator}"

    def receive_from(self, producer: Producer[D]):
        producer.send_to(self._submit)

    def _submit(self, dv: DataVehicle[D], completed: CompletedCallback | None):
        dv.context.inc_reference()
        try:
            self._process(dv)
        finally:
            dv.context.dec_reference()
            if completed:
                completed()

    @abstractmethod
    def _process(self, dv: DataVehicle[D]) -> None: ...


class InlineConsumerProcessor[D](InlineConsumerProcessorImpl[D]):
    def __init__(self, consumer: Consumer[D]):
        super().__init__(differentiator=consumer.name)
        self.consumer = consumer

    @staticmethod
    def as_processor(consumer: Consumer[D] | ConsumerProcessor[D]) -> ConsumerProcessor[D]:
        if isinstance(consumer, ConsumerProcessor):
            return consumer
        return InlineConsumerProcessor(consumer)

    @staticmethod
    def _differentiator_is_entire_name() -> bool:
        return True

    def _process(self, dv: DataVehicle[D]) -> None:
        with dv.wrap_execution(self.consumer.trace_name):
            self.consumer.process(dv)


class InlineTransformerProcessorImpl[D, R](ProducerImpl[R], TransformerProcessor[D, R]):
    def __init__(self, differentiator: str | None = None) -> None:
        super().__init__()
        self.__differentiator = differentiator

    @property
    def differentiator(self) -> str | None:
        return self.__differentiator

    def _submit(self, dv: DataVehicle[D], completed: CompletedCallback | None):
        dv.context.inc_reference()
        try:
            self._process(dv)
        finally:
            dv.context.dec_reference()
            if completed:
                completed()

    def receive_from(self, producer: Producer[D]):
        producer.send_to(self._submit)

    @abstractmethod
    def _process(self, dv: DataVehicle[D]) -> None: ...


class InlineTransformerProcessor[D, R](InlineTransformerProcessorImpl[D, R]):
    def __init__(self, transformer: Transformer[D, R]):
        super().__init__(differentiator=transformer.name)
        self.transformer = transformer

    @staticmethod
    def as_processor(transformer: Transformer[D, R] | TransformerProcessor[D, R]) -> TransformerProcessor[D, R]:
        if isinstance(transformer, TransformerProcessor):
            return transformer
        return InlineTransformerProcessor(transformer)

    @staticmethod
    def _differentiator_is_entire_name() -> bool:
        return True

    def _process(self, dv: DataVehicle[D]) -> None:
        with dv.wrap_execution(self.transformer.trace_name):
            self.transformer.process(dv, self._push)


class InlineConsumerIdentityTransformerProcessor[D](InlineTransformerProcessorImpl[D, D]):
    def __init__(self, consumer: Consumer[D]):
        super().__init__(differentiator=consumer.name)
        self.consumer = consumer

    @staticmethod
    def _differentiator_is_entire_name() -> bool:
        return True

    def _process(self, dv: DataVehicle[D]) -> None:
        with dv.wrap_execution(self.consumer.trace_name):
            self.consumer.process(dv)
        self._push(dv)
