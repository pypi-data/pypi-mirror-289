import numpy as np

CALIBRATION_GAIN_MULTIPLIER = 2**12
MAX_CALIBRATION_GAIN_VALUE = 2**16 - 1


def decode_hik_calibration_data(data: bytes) -> np.ndarray:
    header_len = 0x278
    buffer_data = data[header_len:]
    footer_len = len(buffer_data) % 1024
    if footer_len:
        buffer_data = buffer_data[:-footer_len]
    return np.frombuffer(buffer_data, "<I").reshape(2, -1)


def hik_calibration_gain_rgb_views(img: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    return img[0, 0::2], img[1], img[0, 1::2]


def calibration_set_filename(calibration_set: int) -> str:
    return f"UserPRNUC{calibration_set}"
