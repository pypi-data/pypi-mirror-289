from typing import Sequence, SupportsFloat
from enum import Enum
from ..gev.px_layout import PxLayout

DEFAULT_FRAME_HEIGHT = 300
DEFAULT_CALIBRATION_SET = 1
FACTORY_CALIBRATION_SET = 0


class CameraNetworkType(str, Enum):
    DHCP = "dhcp"
    STATIC = "static"


def max_exposure_micros_for_line_rate(line_rate: float) -> float:
    line_micros = 1_000_000 / line_rate
    # Experimentally seems to be ~2.5 micros gap between exposures
    # Increase it slightly so when synced can handle a bit of variance
    result = line_micros - 4
    if result < 4:
        raise ValueError(f"Line rate is too high: {line_rate}Hz")
    if result > 3000:
        return 3000
    return result


class CameraArrayConfig:
    # noinspection PyShadowingBuiltins
    def __init__(
        self,
        serials: Sequence[str],
        line_rate: float = 1000,
        edge_crop_pxs: Sequence[int] | None = None,
        y_offset_pxs: Sequence[int] | None = None,
        px_layout: PxLayout = PxLayout.BGR_8,
        sync: bool = False,
        reversed: Sequence[bool] | bool = False,
        reverse_scan_direction: Sequence[bool] | bool | None = None,
        gains: float | Sequence[float] = 1,
        exposure_micros: float | None = None,
        frame_height: int = DEFAULT_FRAME_HEIGHT,
        calibration_set: int | None = DEFAULT_CALIBRATION_SET,
        white_balance_rgb_factors: Sequence[tuple[float, float, float] | None] | None = None,
        network_type: CameraNetworkType = CameraNetworkType.DHCP,
    ):
        self.serials: Sequence[str] = tuple(serials)
        self.cam_count = len(serials)
        self.line_rate = line_rate
        self.edge_crop_pxs: Sequence[int] = tuple(edge_crop_pxs or (0 for _ in range(self.cam_count + 1)))
        self.y_offset_pxs: Sequence[int] = tuple(y_offset_pxs or (0 for _ in range(self.cam_count)))
        self.px_layout = px_layout
        self.sync = sync
        if isinstance(reversed, bool):
            self.reversed = tuple(reversed for _ in range(self.cam_count))
        else:
            self.reversed = tuple(reversed)
        if len(self.reversed) != self.cam_count:
            raise ValueError(
                f"Have {self.cam_count} serials, expected {self.cam_count} reversed, got {len(self.reversed)}"
            )
        if reverse_scan_direction is None:
            self.reverse_scan_direction = self.reversed
        elif isinstance(reverse_scan_direction, bool):
            self.reverse_scan_direction = tuple(reverse_scan_direction for _ in range(self.cam_count))
        else:
            self.reverse_scan_direction = tuple(reverse_scan_direction)
        if len(self.reverse_scan_direction) != self.cam_count:
            raise ValueError(
                f"Have {self.cam_count} serials, expected {self.cam_count} reverse_scan_direction, "
                f"got {len(self.reverse_scan_direction)}"
            )
        self.network_type = network_type
        if isinstance(gains, SupportsFloat):
            self.gain = tuple(float(gains) for _ in range(self.cam_count))
        else:
            self.gain = gains
        self.exposure_micros = exposure_micros or max_exposure_micros_for_line_rate(line_rate)
        self.frame_height = frame_height
        self.calibration_set = calibration_set
        if white_balance_rgb_factors is None:
            white_balance_rgb_factors = [None] * self.cam_count
        self.white_balance_rgb_factors = tuple(factors or (1, 1, 1) for factors in white_balance_rgb_factors)
        if len(self.white_balance_rgb_factors) != self.cam_count:
            raise ValueError(
                f"Have {self.cam_count} serials, expected {self.cam_count} white_balance_rgb_factors, "
                f"got {len(self.white_balance_rgb_factors)}"
            )
        self.time_per_frame = frame_height / line_rate
        if len(self.edge_crop_pxs) != self.cam_count + 1:
            raise ValueError(
                f"Have {self.cam_count} serials, expected {self.cam_count + 1} edge_crop_pxs, "
                f"got {len(self.edge_crop_pxs)}"
            )
        if len(self.y_offset_pxs) != self.cam_count:
            raise ValueError(f"Have {self.cam_count} serials, got {len(self.y_offset_pxs)} y_offset_pxs")
        if len(self.gain) != self.cam_count:
            raise ValueError(f"Have {self.cam_count} serials, got {len(self.gain)} gains")
