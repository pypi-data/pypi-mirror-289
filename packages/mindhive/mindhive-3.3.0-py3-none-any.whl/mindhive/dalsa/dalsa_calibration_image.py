import cv2 as cv
import numpy as np

from .dalsa_c_data import encode_str

# - DALSA use TIFF format to store calibration image
# - Camera correction calc:
#       newPixelValue[x] = (sensorPixelValue[x] - FFCOffset[x]) * (FFCGain[x] / CALIBRATION_GAIN_MULTIPLIER)
# - Image is 2048x4
# - Rows 0 and 1 are Offset per pixel in Bayer format (generally all zero)
# - Rows 2 and 3 are Gain per pixel in Bayer format

CALIBRATION_GAIN_MULTIPLIER = 2**12
MAX_CALIBRATION_GAIN = 8


def encode_dalsa_calibration_image(img: np.ndarray) -> bytes:
    success, encoded_array = cv.imencode(".tiff", img)
    if not success:
        raise IOError(f"Failed to encode tiff image")
    return encoded_array.tobytes()


def decode_dalsa_calibration_image(data: bytes) -> np.ndarray:
    img_encoded = np.frombuffer(data, np.uint8)
    img = cv.imdecode(img_encoded, cv.IMREAD_UNCHANGED)
    if img is None:
        raise IOError(f"Failed to decode image")
    return img


def dalsa_calibration_offset_rgb_views(img: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    return img[1, 0::2], img[0], img[1, 1::2]


def dalsa_calibration_gain_rgb_views(img: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    return img[3, 0::2], img[2], img[3, 1::2]


def calibration_set_filename(calibration_set: int) -> bytes:
    result = encode_str(f"FlatFieldCoefficients{calibration_set}")
    assert result
    return result
