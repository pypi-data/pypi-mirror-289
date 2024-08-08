import logging
from collections import Counter
from threading import RLock
from typing import Callable, Collection, Sequence

import cv2 as cv
import numpy as np
from time import time

from .frame import Frame
from ..log.metrics import metrics
from ..process.data_vehicle import DataVehicle
from ..process.transformer import DataPush, Transformer
from ..strip.rendering import Rendering
from ..strip.strip import Strip

MAX_WAIT_FOR_STRIP_COMPLETE_TIME = 5
EXCESSIVE_STRIPS_IN_PROGRESS = 2
ALLOW_EXCESSIVE_STRIPS_OVER_TIME = 60

_EMPTY = object()


class StripBuilder:
    def __init__(self, cam_count: int, frame: Frame):
        self.cam_count = cam_count
        self.id = frame.id
        self.timestamp = frame.timestamp
        self.images: list = [_EMPTY for _ in range(cam_count)]
        self.rendering: Rendering | None = frame.rendering
        self.add_frame(frame)

    def add_frame(self, frame: Frame):
        assert frame.id == self.id
        assert self.images[frame.cam_idx] is _EMPTY
        if self.rendering != frame.rendering:
            self.rendering = None
        self.images[frame.cam_idx] = frame.img

    @property
    def is_complete(self) -> bool:
        return all(img is not _EMPTY for img in self.images)

    @property
    def is_filled(self) -> bool:
        return all(img is not _EMPTY and img is not None for img in self.images) and self.rendering is not None

    @property
    def complete_cam_indexes(self) -> Collection[int]:
        return [i for i, img in enumerate(self.images) if img is not _EMPTY]

    @property
    def missing_cam_indexes(self) -> Collection[int]:
        return [i for i, img in enumerate(self.images) if img is _EMPTY]


class FrameArrayStripComposer(Transformer[Frame, Strip]):
    def __init__(
        self,
        cam_count: int,
        time_per_frame: float,
        y_offsets: Sequence[int] | None = None,
        y_scale: float = 1.0,
        edge_crop_pxs: Sequence[int] | None = None,
        *,
        initial_speed_proportion: float = 0,
        missing_frames_fatal=True,
        adjust_timestamps=True,
        differentiator: str | None = None,
    ):
        def x_slice(cam_idx: int) -> slice:
            if edge_crop_pxs is None:
                return slice(None)
            left_crop = edge_crop_pxs[cam_idx]
            left_px = left_crop if cam_idx == 0 else left_crop // 2
            right_crop = edge_crop_pxs[cam_idx + 1]
            last_idx = self.cam_count - 1
            right_px = right_crop if cam_idx == last_idx else right_crop - right_crop // 2
            return slice(None if left_px == 0 else left_px, None if right_px == 0 else -right_px)

        assert edge_crop_pxs is None or len(edge_crop_pxs) == cam_count + 1
        super().__init__(differentiator)
        self.cam_count = cam_count
        self.tags = [f"differentiator:${differentiator}"] if differentiator else []
        self.time_per_frame = time_per_frame
        if y_offsets is None:
            self.y_offsets = [0 for _ in range(cam_count)]
        else:
            self.y_offsets = y_offsets
        assert len(self.y_offsets) == cam_count
        self.y_scale = y_scale
        self.x_slices = [x_slice(i) for i in range(self.cam_count)]
        self.strip_listeners: list[Callable[[], None]] = []
        self.lock = RLock()
        self.speed_proportion = initial_speed_proportion
        self.missing_frames_fatal = missing_frames_fatal
        self.adjust_timestamps = adjust_timestamps
        self.last_builder: StripBuilder | None = None
        self.first_strip = True
        self.last_pushed_id: int | None = None
        self.frame_id_map_builder: dict[int, StripBuilder] = {}
        self.start_timestamp: float | None = None
        self.last_timestamp: float | None = None
        self.excessive_in_progress_start_timestamp: float | None = None

    def on_strip_completed(self, listener: Callable[[], None]):
        self.strip_listeners.append(listener)

    def process(self, dv: DataVehicle[Frame], push: DataPush[Strip]) -> None:
        frame: Frame = dv.data
        with self.lock:
            builder = self.frame_id_map_builder.get(frame.id)
            if builder:
                builder.add_frame(frame)
            else:
                builder = StripBuilder(self.cam_count, frame)
                if self.first_strip and not self.frame_id_map_builder and frame.id != 0:
                    self.log.warning(f"Frame id not zero as required for dead reckoning: {frame}")
                self.frame_id_map_builder[frame.id] = builder
            self._check_completed_strips(frame.timestamp, push)
            self._check_excessive_strips(frame.timestamp)

    def restart(self, start_epoch_timestamp: float | None = None):
        with self.lock:
            self.last_builder = None
            self.first_strip = True
            self.last_pushed_id = None
            self.start_timestamp = start_epoch_timestamp
            self.last_timestamp = None
            self.frame_id_map_builder.clear()

    def _check_completed_strips(self, now: float, push: DataPush):
        while self.frame_id_map_builder:
            head_id = min(self.frame_id_map_builder.keys())
            builder = self.frame_id_map_builder[head_id]
            expected_id = self.last_builder and self.last_builder.id + 1
            consecutive = self.last_builder is None or builder.id == expected_id
            if consecutive and builder.is_complete:
                del self.frame_id_map_builder[builder.id]
                if self.first_strip:
                    self.log.info("Built first strip")
                    self.first_strip = False
                for listener in self.strip_listeners:
                    listener()
                timestamp = self._calc_timestamp(builder)
                if not self.speed_proportion:
                    self.log.debug(f"Dropping frames id: {builder.id} due to low speed")
                    metrics.increment("strip_composer.dropped_stopped_frame.count", 1, self.tags)
                elif not builder.is_filled:
                    self.log.debug(f"Dropping frames id: {builder.id} as not filled")
                    metrics.increment("strip_composer.unfilled_frame.count", 1, self.tags)
                else:
                    assert builder.rendering
                    imgs = self._build_imgs(builder.images)
                    contiguous = (
                        self.last_pushed_id is not None
                        and self.last_builder is not None
                        and self.last_pushed_id == self.last_builder.id
                    )
                    frame_widths = [img.shape[1] for img in imgs]
                    strip = Strip(timestamp, np.hstack(imgs), contiguous, builder.rendering, frame_widths)
                    push(DataVehicle(strip))
                    self.last_pushed_id = builder.id
                self.last_builder = builder
            else:
                strip_age = now - builder.timestamp
                if strip_age < MAX_WAIT_FOR_STRIP_COMPLETE_TIME:
                    break
                if expected_id is not None:
                    missing_count = builder.id - expected_id
                    if missing_count > 0:
                        self.log.error(
                            f"Missing all frames for {missing_count} strips: {expected_id} -> {builder.id - 1}"
                        )
                if not builder.is_complete:
                    self.log.error(f"Strip: {builder.id} is missing frames: {builder.missing_cam_indexes}")
                if self.missing_frames_fatal:
                    raise RuntimeError(f"Giving up after {strip_age:.3f}s waiting to complete next strip")
                while self.frame_id_map_builder:
                    head_id = min(self.frame_id_map_builder.keys())
                    if self.frame_id_map_builder[head_id].is_complete:
                        break
                    self.log.warning(f"Dropping strip: {head_id}")
                    del self.frame_id_map_builder[head_id]
                    metrics.increment("strip_composer.skipped_frame.count", 1, self.tags)
                self.last_builder = None

    def _calc_timestamp(self, builder: StripBuilder) -> float:
        timestamp = builder.timestamp
        if self.adjust_timestamps and self.last_timestamp is not None and self.last_builder is not None:
            frame_count = builder.id - self.last_builder.id
            max_timestamp = self.last_timestamp + frame_count * self.time_per_frame * 1.01
            if timestamp > max_timestamp:
                delta = timestamp - max_timestamp
                if delta < 0.1:
                    level = logging.DEBUG
                else:
                    level = logging.INFO
                self.log.log(level, f"Shifting strip timestamp {delta:.3f}s earlier to be within 1% of expected")
                metrics.increment("strip_composer.dead_reckoning_restriction.time", delta, self.tags)
                timestamp = max_timestamp
        self.last_timestamp = timestamp
        if self.start_timestamp is None:
            self.start_timestamp = time() - self.time_per_frame
        dead_reckoning_timestamp = self.start_timestamp + (self.time_per_frame * builder.id)
        metrics.gauge("strip_composer.dead_reckoning_offset.time", timestamp - dead_reckoning_timestamp, self.tags)
        return timestamp

    def _build_imgs(self, imgs: Sequence[np.ndarray]) -> Sequence[np.ndarray]:
        max_holdover_h = max(self.y_offsets)
        imgs = list(imgs)
        img_hs = [img.shape[0] for img in imgs]
        if len(set(img_hs)) > 1:
            raise RuntimeError(f"Image heights don't match: {img_hs}")
        for i, img in enumerate(imgs):
            y_offset = self.y_offsets[i]
            slice_end = -y_offset or None
            if self.last_builder is None or not self.last_builder.is_filled:
                slice_start = max_holdover_h - y_offset
                imgs[i] = img[slice_start:slice_end]
            else:
                if y_offset:
                    last_frame_img = self.last_builder.images[i]
                    imgs[i] = np.vstack([last_frame_img[slice_end:], img[:slice_end]])
                else:
                    imgs[i] = img
        imgs = [img[:, x_slice] for img, x_slice in zip(imgs, self.x_slices)]
        y_scale = self.speed_proportion * self.y_scale
        if y_scale != 1:
            imgs = [cv.resize(img, None, fx=1, fy=y_scale, interpolation=cv.INTER_AREA) for img in imgs]
        return imgs

    def set_speed_proportion(self, proportion: float):
        with self.lock:
            if self.speed_proportion != proportion:
                self.log.info(f"Setting speed: {proportion:.3f}")
                self.speed_proportion = proportion

    def _check_excessive_strips(self, timestamp: float):
        cam_idx_counts: Counter[int] = Counter()
        for builder in self.frame_id_map_builder.values():
            cam_idx_counts.update(builder.complete_cam_indexes)
        for cam_idx in range(self.cam_count):
            metrics.gauge("strip_composer.cam_frame_backlog", cam_idx_counts[cam_idx], [*self.tags, f"index:{cam_idx}"])
        strips_in_progress = len(self.frame_id_map_builder)
        metrics.gauge("strip_composer.strips_in_progress", strips_in_progress, self.tags)
        if strips_in_progress >= EXCESSIVE_STRIPS_IN_PROGRESS:
            if self.excessive_in_progress_start_timestamp:
                if (timestamp - self.excessive_in_progress_start_timestamp) > ALLOW_EXCESSIVE_STRIPS_OVER_TIME:
                    missing_desc = [builder.missing_cam_indexes for builder in self.frame_id_map_builder.values()]
                    raise RuntimeError(
                        "Excessive strips: "
                        f"{EXCESSIVE_STRIPS_IN_PROGRESS} or more for {ALLOW_EXCESSIVE_STRIPS_OVER_TIME}s\n"
                        f"Current missing indexes: {[missing_desc]}"
                    )
            else:
                self.excessive_in_progress_start_timestamp = timestamp
        else:
            self.excessive_in_progress_start_timestamp = None
