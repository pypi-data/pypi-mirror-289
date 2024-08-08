import logging
import re
from enum import Enum
from pathlib import Path
from typing import Iterable

import cv2 as cv
import numpy as np
from time import monotonic, sleep, time

from .frame import Frame
from ..log.timestamp import timestamp_for_log
from ..process.data_vehicle import DataVehicle
from ..process.producer import ProducerImpl
from ..process.thread import start_thread
from ..strip.rendering import Rendering

# TODO: Once we update Tasman Whanganui to newer images:
#   parse the timestamps in filenames and use them as the timing between frames

FRAME_FILE_FORMAT = re.compile(r"-(\d+)-(\d+)-\w+.\w+$")


def path_match(path: Path) -> re.Match:
    match = FRAME_FILE_FORMAT.search(str(path))
    if not match:
        raise RuntimeError(f"File does not match expected format: {path}")
    return match


def path_frame_id(path: Path) -> int:
    return int(path_match(path)[1])


def path_cam_idx(path: Path) -> int:
    return int(path_match(path)[2])


class RepeatStrategy(Enum):
    NO = "NO"
    ONE = "ONE"
    ALL = "ALL"


class LoadFramesProducer(ProducerImpl):
    def __init__(
        self,
        candidate_paths: Iterable[Path],
        rendering: Rendering,
        idx: int,
        time_per_frame: float,
        repeat: RepeatStrategy | None = None,
    ) -> None:
        super().__init__()
        candidate_paths = sorted(candidate_paths)
        if not candidate_paths:
            raise RuntimeError("Didn't find any candidate_paths")
        self.rendering = rendering
        self.idx = idx
        self.time_per_frame = time_per_frame
        if repeat is None:
            repeat = RepeatStrategy.NO
        self.repeat = repeat
        self.first_frame_id = min(path_frame_id(path) for path in candidate_paths)
        self.paths = sorted(
            (path for path in candidate_paths if path_cam_idx(path) == idx),
            key=path_frame_id,
        )
        if not self.paths:
            raise RuntimeError(f"Could not find any images for cam_idx {idx}")
        self.log.info(f"Processing {len(self.paths)} frames")

    @property
    def differentiator(self) -> str | None:
        return f"{self.rendering.name}.{self.idx}"

    def start(self):
        self.log.info("Starting")
        start_thread(self.log, self._worker)

    def _worker(self):
        last_frame: Frame | None = None
        frame_id_offset = 0
        path_iter = iter(self.paths)
        start_monotonic_ts = monotonic()
        start_time_ts = time()
        while True:
            try:
                path = next(path_iter)
            except StopIteration:
                if last_frame is None:
                    raise RuntimeError(f"No paths found for cam_idx {self.idx}")
                if self.repeat is RepeatStrategy.NO:
                    self.log.info("All done")
                    return
                elif self.repeat is RepeatStrategy.ONE:
                    img = last_frame.img
                    frame_id = last_frame.id + 1
                elif self.repeat is RepeatStrategy.ALL:
                    path_iter = iter(self.paths)
                    frame_id_offset = last_frame.id + 1
                    self.log.info(f"Looping around, {frame_id_offset=}")
                    continue
                else:
                    raise NotImplementedError()
            else:
                self.log.debug(f"Loading {path}")
                success, imgs = cv.imreadmulti(str(path), None, cv.IMREAD_UNCHANGED)
                if not success:
                    raise RuntimeError(f"Failed to load image: {path}")
                if len(imgs) == 1:
                    img = imgs[0]
                else:
                    img = np.dstack(imgs)
                img = self.preprocess_image(img)
                frame_id = path_frame_id(path) - self.first_frame_id + frame_id_offset
            frame_time = frame_id * self.time_per_frame
            elapsed_time = monotonic() - start_monotonic_ts
            sleep_time = frame_time - elapsed_time
            if sleep_time > 0:
                if sleep_time > 0.5:
                    self.log.warning(f"Sleep seems too far into the future: {sleep_time:.1f}s")
                sleep(sleep_time)
            elif sleep_time < -0.5:
                self.log.warning(f"Getting behind, should have sent frame {frame_id} {-sleep_time:.1f}s ago")
            timestamp = start_time_ts + frame_time
            if last_frame is None:
                self.log.info(f"First timestamp: {timestamp_for_log(timestamp)}")
            elif self.log.isEnabledFor(logging.DEBUG):
                self.log.debug(f"Frame {frame_id} timestamp: {timestamp_for_log(timestamp)}")
            frame = Frame(self.idx, frame_id, timestamp, img, self.rendering)
            self._push(DataVehicle(frame))
            last_frame = frame

    def preprocess_image(self, img: np.ndarray) -> np.ndarray:
        return img
