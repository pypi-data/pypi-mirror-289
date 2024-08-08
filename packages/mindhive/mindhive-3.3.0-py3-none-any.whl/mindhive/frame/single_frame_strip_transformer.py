import cv2 as cv

from .frame import Frame
from ..log.metrics import metrics
from ..process.data_vehicle import DataVehicle
from ..process.transformer import Transformer, DataPush
from ..strip.strip import Strip


class SingleFrameStripTransformer(Transformer[Frame, Strip]):
    def __init__(
        self, y_scale: float = 1, initial_speed_proportion: float = 0, differentiator: str | None = None
    ) -> None:
        super().__init__(differentiator)
        self.y_scale = y_scale
        self.speed_proportion = initial_speed_proportion
        self.last_frame_id: int | None = None
        self.tags = [f"differentiator:${differentiator}"] if differentiator else []

    def set_speed_proportion(self, proportion: float):
        self.speed_proportion = proportion

    def restart(self):
        self.last_frame_id = None

    def process(self, dv: DataVehicle[Frame], push: DataPush[Strip]) -> None:
        if not self.speed_proportion:
            metrics.increment("strip_transformer.dropped_stopped_frame.count", 1, self.tags)
            return
        frame: Frame = dv.data
        if not frame.is_filled:
            metrics.increment("strip_transformer.unfilled_frame.count", 1, self.tags)
            return
        assert frame.img
        img = frame.img
        contiguous = self.last_frame_id is not None and (self.last_frame_id + 1) == frame.id
        y_scale = self.speed_proportion * self.y_scale
        if y_scale != 1:
            img = cv.resize(img, None, fx=1, fy=y_scale, interpolation=cv.INTER_AREA)
        strip = Strip(frame.timestamp, img, contiguous, frame.rendering, [img.shape[1]])
        self.last_frame_id = frame.id
        return push(DataVehicle(strip, dv))
