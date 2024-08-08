from .consumer import Consumer
from .data_vehicle import DataVehicle
from .queue_processor import QueueProcessorImpl


class InlineSerialConsumerProcessor[D](QueueProcessorImpl[D]):
    def __init__(self, *consumers: Consumer[D]) -> None:
        super().__init__(consumers[0].name)
        self.consumers = consumers

    def _process(self, dv: DataVehicle[D]) -> None:
        for consumer in self.consumers:
            with dv.wrap_execution(consumer.trace_name):
                consumer.process(dv)
