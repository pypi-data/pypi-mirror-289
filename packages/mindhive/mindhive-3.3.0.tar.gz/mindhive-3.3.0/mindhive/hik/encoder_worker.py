from typing import Callable

from mindhive.hik.hik_camera_producer import HikCameraProducer
from mindhive.hik.hik_api import HikCamera
from ..log.metrics import metrics
import logging
from logging import Logger
from ..log.trace import tracer
from time import monotonic
from abc import ABC, abstractmethod

EncoderListener = Callable[[float], None]
FrequencyListener = Callable[[float], None]


class PersistentWorker(ABC):
    @abstractmethod
    def call_worker(self) -> bool:
        pass


class EncoderWorker(PersistentWorker):
    """Example setup:
    belt_speed = BeltSpeed(BELT_PROX_FULL_SPEED_HZ)
    encoder_prod = cam_array.get_camera_from_serial("DA3259066")
    encoder = EncoderWorker(encoder_prod,belt_speed.set_speed,3,mult=5)
    """

    def __init__(
        self,
        camera_producer: HikCameraProducer,
        listener: EncoderListener,
        poll_time: float,
        line_num: int = 0,
        mult: int = 32,
    ) -> None:
        self.encoder_listener: EncoderListener | None = None
        self.poll_time: float | None = None
        self.metric_tags: list[str] = []
        self.cam_idx: int | None = None
        self.encoder_fetch_value: Callable[[], int] | None = None
        self._log: Logger | None = None
        self.first_call: bool = True

        if self.encoder_listener is not None:
            raise NotImplementedError("Can only have one counter/timer listener")
        camera: HikCamera = camera_producer.cam
        camera.encoder_setup(line_num, mult)
        self.metric_tags = [f"index:{camera.index}"]
        self.encoder_listener = listener
        self.poll_time = poll_time
        self.encoder_fetch_value = camera.get_encoder_value
        self.counter_start_ts = monotonic()
        self.log.info("Setup counter")
        camera_producer._add_persistent_worker_task(self.call_worker)

    @property
    def name(self) -> str:
        return self.__class__.__name__

    @property
    def log(self) -> Logger:
        if self._log is None:
            self._log = logging.getLogger(self.name)
        return self._log

    def call_worker(self) -> bool:
        return self._maybe_read_line()

    def _maybe_read_line(self) -> bool:
        if self.encoder_listener is None:
            return False
        assert self.counter_start_ts
        assert self.poll_time
        assert self.encoder_fetch_value

        # Camera setup may take some time some time, so always do read on first camera producer loop
        if self.first_call:
            self.first_call = False
            self.log.debug(f"First encoder read for camera {self.cam_idx}")
        elif monotonic() < (self.counter_start_ts + self.poll_time + 0.01):
            return False
        self.log.debug(f"Reading encoder for camera {self.cam_idx}")
        encoder_value = self.encoder_fetch_value()
        # Reset counter
        self.counter_start_ts = monotonic()
        self.log.debug(f"Read encoder: {encoder_value}")
        metrics.gauge("camera.encoder.value", encoder_value, self.metric_tags)
        # Propagate value to listener
        self.encoder_listener(float(encoder_value))
        return True
