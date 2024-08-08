from logging import Logger
from typing import Collection

from ..gev.cam_error import CamError
from ..log.metrics import metrics


class FrameIdTracking:
    MIN_FRAME_ID = 1
    MAX_FRAME_ID = 65535

    def __init__(self, missing_frames_fatal: bool, log: Logger, metric_tags: Collection[str]):
        self.missing_frames_fatal = missing_frames_fatal
        self.log = log
        self.metric_tags = metric_tags
        self._frame_id_offset = -self.MIN_FRAME_ID  # So our frame_ids start at zero
        self.last_snapshot_id: int | None = None

    def calc_frame_id(self, snapshot_id: int) -> int:
        if self.last_snapshot_id is not None and self.last_snapshot_id + 1 != snapshot_id:
            if self.last_snapshot_id == self.MAX_FRAME_ID and snapshot_id == self.MIN_FRAME_ID:
                self.log.debug("Frame id looped")
                self._frame_id_offset += (self.MAX_FRAME_ID - self.MIN_FRAME_ID) + 1
            else:
                if self.missing_frames_fatal:
                    raise CamError(f"Frames out of order: {self.last_snapshot_id} -> {snapshot_id}")
                # TODO: handle frames out of order (id looping is difficult)
                self.log.warning(f"Ignoring frame jump: {self.last_snapshot_id} -> {snapshot_id}")
                metrics.increment(
                    "camera.skipped_frame.count", snapshot_id - self.last_snapshot_id - 1, self.metric_tags
                )
        self.last_snapshot_id = snapshot_id
        return snapshot_id + self._frame_id_offset
