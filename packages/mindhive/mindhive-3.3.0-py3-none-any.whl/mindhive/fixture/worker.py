from typing import Any, Sequence

from ..process.data_vehicle import DataVehicle


class TransformerAccumulator:
    def __init__(self):
        self.data_vehicles: list[DataVehicle] = []

    def submit(self, dv: DataVehicle):
        self.data_vehicles.append(dv)

    def drain(self):
        self.data_vehicles.clear()

    @property
    def data(self) -> Sequence[Any]:
        return [dv.data for dv in self.data_vehicles]
