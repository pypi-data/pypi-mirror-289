from concurrent.futures.thread import ThreadPoolExecutor
from time import time

from .dalsa_camera_array import open_dalsa_camera_producer_array
from ..frame.frame import Frame
from ..frame.frame_array_strip_composer import FrameArrayStripComposer
from ..gev.camera_array_config import CameraArrayConfig
from ..log.trace import tracer
from ..process.consumer import Consumer
from ..process.consumer_processor import ConsumerProcessor
from ..process.pipeline_component import PipelineComponent
from ..process.producer import DataListener, Producer
from ..process.queue_processor import QueueConsumerProcessor, QueueTransformerProcessor
from ..process.thread import exec_all
from ..strip.strip import Strip


class DalsaCameraArrayStripProducer(PipelineComponent, Producer[Strip]):
    def __init__(
        self,
        config: CameraArrayConfig,
        always_running: bool,
        frame_consumer: Consumer[Frame] | ConsumerProcessor[Frame] | None = None,
        missing_frames_fatal=True,
    ) -> None:
        super().__init__()
        self.cam_producers = open_dalsa_camera_producer_array(config, missing_frames_fatal)
        self.composer = FrameArrayStripComposer(
            config.cam_count,
            config.time_per_frame,
            y_offsets=config.y_offset_pxs,
            edge_crop_pxs=config.edge_crop_pxs,
            initial_speed_proportion=1 if always_running else 0,
            missing_frames_fatal=missing_frames_fatal,
            differentiator="color",
        )
        composer_processor = QueueTransformerProcessor(self.composer)
        frame_processor = frame_consumer and QueueConsumerProcessor.as_processor(frame_consumer)
        for cam in self.cam_producers:
            composer_processor.receive_from(cam)
            if frame_processor is not None:
                frame_processor.receive_from(cam)
        self.config = config
        self._tail = composer_processor

    def send_to(self, listener: DataListener[Strip]):
        self._tail.send_to(listener)

    def set_speed_proportion(self, proportion: float):
        self.composer.set_speed_proportion(proportion)

    @tracer.wrap()
    def start(self, wait_for_started=False):
        start_time = time() + 1
        self.composer.restart(start_time)
        for i, cam in enumerate(self.cam_producers):
            is_master = i == 0
            offset = 0.005 if self.config.sync and is_master else 0
            cam.start(start_time + offset)
        self.log.debug(f"Camera start in {start_time - time():.3f}s")
        if wait_for_started:
            for cam in self.cam_producers:
                cam.wait_for_started()
            self.log.info("All cameras started")

    @tracer.wrap()
    def reboot(self):
        # Run in a thread pool because each camera reset takes 8 seconds to return
        with ThreadPoolExecutor(max_workers=len(self.cam_producers)) as executor:
            exec_all(executor.submit(cam.reboot) for cam in self.cam_producers)
        self.log.info("Camera reset complete")
