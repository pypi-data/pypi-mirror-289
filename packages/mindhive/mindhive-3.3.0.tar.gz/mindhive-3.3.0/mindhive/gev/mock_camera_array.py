import os
from ctypes import CDLL
from pathlib import Path
from typing import Iterable

from ..frame.load_frames_producer import LoadFramesProducer, RepeatStrategy
from ..gev.camera_array_config import CameraArrayConfig
from ..process.pipeline_component import PipelineComponent
from ..process.producer import DataListener, Producer
from ..strip.rendering import Rendering


class MockCameraProducer(PipelineComponent, Producer):
    def __init__(
        self,
        cam_idx: int,
        config: CameraArrayConfig,
        candidate_paths: Iterable[Path],
        repeat: RepeatStrategy | None = None,
        rendering=Rendering.color,
    ):
        super().__init__()
        self.producer = LoadFramesProducer(
            candidate_paths,
            rendering,
            cam_idx,
            config.time_per_frame,
            repeat,
        )
        self.on_pulse_frequency = self.on_poll_pulse_counter

    def send_to(self, listener: DataListener):
        self.producer.send_to(listener)

    def start(self, _):
        self.producer.start()

    def on_poll_pulse_counter(self, listener, *_, **__):
        if not hasattr(listener, "__self__"):
            raise NotImplementedError(f"Can't handle bare listener functions: {listener}")
        if not hasattr(listener.__self__, "full_speed"):
            raise NotImplementedError(f"Can't handle class: {listener.__self__.__class__.__name__}")
        listener(listener.__self__.full_speed * 0.95)

    def on_error(self, *_, **__):
        pass

    def wait_for_started(self):
        pass


def open_mock_camera_array(
    config: CameraArrayConfig,
    candidate_paths: Iterable[Path],
    repeat: RepeatStrategy | None = None,
):
    if not os.getenv("SKIP_SO_CHECK"):
        # Ensure we can load the drivers
        CDLL("/opt/GigeV/dalsa.so")
        CDLL("/opt/MVS/lib/hik.so")
    return [MockCameraProducer(i, config, candidate_paths, repeat) for i in range(config.cam_count)]
