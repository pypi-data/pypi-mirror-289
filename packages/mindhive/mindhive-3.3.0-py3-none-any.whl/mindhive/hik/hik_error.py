from .hik_c_data import CameraInfo

MV_E_HANDLE = 0x80000000
MV_E_CALL_ORDER = 0x80000003
MV_E_PARAMETER = 0x80000004
MV_E_NO_DATA = 0x80000007
MV_E_ABNORMAL_IMAGE = 0x8000000B
MV_E_GC_TIMEOUT = 0x80000107
MV_E_BUSY = 0x80000204
MV_E_PACKET = 0x80000205
MV_E_NETER = 0x80000206
GEV_COMMS_ERRORS = {MV_E_ABNORMAL_IMAGE, MV_E_GC_TIMEOUT, MV_E_BUSY, MV_E_PACKET, MV_E_NETER}

GEV_STATUS_MAP_CODE = {
    MV_E_HANDLE: "Invalid handle",
    MV_E_CALL_ORDER: "Function calling order error",
    MV_E_PARAMETER: "Incorrect parameter",
    MV_E_NO_DATA: "No data",
    MV_E_ABNORMAL_IMAGE: "Abnormal image, maybe incomplete image because of lost packet",
    MV_E_GC_TIMEOUT: "Time out",
    0x80000203: "Access denied (exclusive access not released?)",
    MV_E_BUSY: "Device is busy, or network disconnected",
    MV_E_PACKET: "Network packet error",
    MV_E_NETER: "Network error - restart switches",
    0x80000102: "The value is out of range",
}


def normalize_hik_status(status):
    if status < 0:
        status += 2**32
    return status


def format_hik_status(status: int) -> str:
    status = normalize_hik_status(status)
    result = f"0x{status:x}" if status >= 0x8000 else str(status)
    status_const = GEV_STATUS_MAP_CODE.get(status)
    if status_const:
        result = f"{status_const} ({result})"
    return result


class HikException(Exception):
    def __init__(self, status: int, api_call: str, serial: str | None) -> None:
        status_str = format_hik_status(status)
        message = f"From {api_call} to {serial}: {status_str}" if serial else f"From {api_call}: {status_str}"
        super().__init__(message)
        self.status = normalize_hik_status(status)
        self.serial = serial


class HikLinkLocalAddressException(RuntimeError):
    def __init__(self, addr: str) -> None:
        super().__init__(f"Camera has link local address: {addr}, must have failed to get DHCP address")
        self.addr = addr


def check_status(driver, status: int, cam: CameraInfo | None):
    if status != 0:
        raise HikException(status, driver.get_last_failed_func().decode(), cam and cam.serial)  # noqa
