from .data_vehicle import DataVehicle
from .inline_processor import InlineTransformerProcessorImpl


class PassthroughProcessor[D](InlineTransformerProcessorImpl[D, D]):
    def _process(self, dv: DataVehicle[D]) -> None:
        self._push(dv)
