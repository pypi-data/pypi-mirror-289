from time import time

from .hik_camera_array import open_hik_camera_producer_array, HikCameraProducer
from ..frame.frame import Frame
from ..frame.frame_array_strip_composer import FrameArrayStripComposer
from ..gev.camera_array_config import CameraArrayConfig
from ..process.consumer import Consumer
from ..process.consumer_processor import ConsumerProcessor
from ..process.pipeline_component import PipelineComponent
from ..process.producer import DataListener, Producer
from ..process.queue_processor import QueueConsumerProcessor, QueueTransformerProcessor
from ..strip.strip import Strip

MOCK_CAMERA_FRAMES_GLOB_ENV_VAR = "MOCK_CAMERA_FRAMES_GLOB"


class HikCameraArrayStripProducer(PipelineComponent, Producer[Strip]):
    def __init__(
        self,
        config: CameraArrayConfig,
        always_running: bool,
        frame_consumer: Consumer[Frame] | ConsumerProcessor[Frame] | None = None,
        *,
        differentiator: str | None = None,
        missing_frames_fatal=True,
        adjust_timestamps=True,
        report_metrics=True,
    ) -> None:
        self._differentiator = differentiator
        super().__init__()
        self.cam_producers = open_hik_camera_producer_array(
            config, missing_frames_fatal, report_metrics, differentiator
        )
        self.composer = FrameArrayStripComposer(
            config.cam_count,
            config.time_per_frame,
            y_offsets=config.y_offset_pxs,
            edge_crop_pxs=config.edge_crop_pxs,
            initial_speed_proportion=1 if always_running else 0,
            missing_frames_fatal=missing_frames_fatal,
            adjust_timestamps=adjust_timestamps,
            differentiator=differentiator or "color",
        )
        composer_processor = QueueTransformerProcessor(self.composer)
        for cam in self.cam_producers:
            composer_processor.receive_from(cam)
        if frame_consumer:
            frame_processor = QueueConsumerProcessor.as_processor(frame_consumer)
            for cam in self.cam_producers:
                frame_processor.receive_from(cam)
        self.config = config
        self._tail = composer_processor

    @property
    def differentiator(self) -> str | None:
        return self._differentiator

    def send_to(self, listener: DataListener[Strip]):
        self._tail.send_to(listener)

    def set_speed_proportion(self, proportion: float):
        self.composer.set_speed_proportion(proportion)

    def update_camera_exposure(self, gain_proportion: float):
        for producer in self.cam_producers:
            producer.update_exposure(gain_proportion)

    def get_camera_from_index(self, index: int) -> HikCameraProducer:
        try:
            return self.cam_producers[index]
        except IndexError:
            raise RuntimeError(f"No Camera Producer index: {index}")

    def get_camera_from_serial(self, serial: str) -> HikCameraProducer:
        for cam_gen in self.cam_producers:
            if cam_gen.serial == serial:
                return cam_gen

        raise RuntimeError(f"No Camera with serial: {serial}")

    def config_dual_line_trigger(self, input_line: int):
        for cam in self.cam_producers:
            cam.config_dual_line_trigger(input_line)

    def start(self, wait_for_started=False):
        start_time = time() + 0.5
        self.composer.restart(start_time)
        for i, cam in enumerate(self.cam_producers):
            cam.start(start_time)
        self.log.debug(f"Camera start in {start_time - time():.3f}s")
        if wait_for_started:
            for cam in self.cam_producers:
                cam.wait_for_started()
            self.log.info("All cameras started")

    def reboot(self):
        for cam in self.cam_producers:
            cam.reboot()
