from typing import Any

from ..process.data_vehicle import DataVehicle
from ..process.producer import ProducerImpl


class MockProducer(ProducerImpl):
    def push_data(self, data: Any):
        self._push(DataVehicle(data))
