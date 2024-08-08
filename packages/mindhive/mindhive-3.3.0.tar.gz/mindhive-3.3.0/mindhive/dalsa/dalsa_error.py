GEVLIB_ERROR_DEVICE_NOT_FOUND = -16
GEV_STATUS_MSG_MISMATCH = 0x8009
GEV_FRAME_STATUS_TIMEOUT = 2
GEVLIB_ERROR_TIME_OUT = -6
GEV_COMMS_ERRORS = {GEV_FRAME_STATUS_TIMEOUT, GEVLIB_ERROR_TIME_OUT, GEV_STATUS_MSG_MISMATCH}

GEV_STATUS_MAP_CODE = {
    GEV_FRAME_STATUS_TIMEOUT: "GEV_FRAME_STATUS_TIMEOUT",
    -1: "GEVLIB_ERROR_GENERIC",
    GEVLIB_ERROR_TIME_OUT: "GEVLIB_ERROR_TIME_OUT",
    -11: "GEVLIB_ERROR_NO_CAMERA",
    GEVLIB_ERROR_DEVICE_NOT_FOUND: "GEVLIB_ERROR_DEVICE_NOT_FOUND",
    -17: "GEVLIB_ERROR_ACCESS_DENIED (feature currently not writable?)",
    0x8006: "GEV_STATUS_ACCESS_DENIED (camera not released?)",
    GEV_STATUS_MSG_MISMATCH: "GEV_STATUS_MSG_MISMATCH",
    0x8FFF: "GEV_STATUS_ERROR (generic error)",
}


def format_dalsa_status(status: int) -> str:
    result = f"0x{status:x}" if status >= 0x8000 else str(status)
    status_const = GEV_STATUS_MAP_CODE.get(status)
    if status_const:
        result += "/" + status_const
    return result


class DalsaException(Exception):
    def __init__(self, status: int, api_call: str) -> None:
        super().__init__(f"From {api_call}: {format_dalsa_status(status)}")
        self.status = status


def check_status(driver, status: int):
    if status != 0:
        raise DalsaException(status, driver.get_last_failed_func().decode())  # noqa
