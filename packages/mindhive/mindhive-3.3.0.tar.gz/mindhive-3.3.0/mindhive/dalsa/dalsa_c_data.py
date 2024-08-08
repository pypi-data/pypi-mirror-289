from ctypes import c_char, c_char_p, c_int, c_int32, c_uint32, c_uint64, c_uint8, POINTER, Structure
from ipaddress import IPv4Address

from _socket import if_indextoname


def decode_bytes(b: bytes) -> str:
    return b.decode("ascii")


def decode_pchar(pchar) -> str:
    return pchar.decode("ascii")


def encode_str(s: str | None) -> bytes | None:
    if s is None:
        return None
    return s.encode("ascii")


class BufferObject(Structure):
    """
     UINT32 payload_type; // Type of payload received (???list them ???)
     UINT32 state;        // Full/empty state for payload buffer (tag used for buffer cycling)
     INT32  status;       // Frame Status (success, error types)
     UINT32 timestamp_hi; // Most 32 significant bit of the timestamp (for legacy code) .
     UINT32 timestamp_lo; // Least 32 significant bit of the timestamp (for legacy code) .
     UINT64 timestamp;    // 64bit version of timestamp for payload (device level timestamp using device level timebase).
     UINT64 recv_size;    // Received size of entire payload (including all appended "chunk" (metadata) information) .
     UINT64 id;           // Block id for the payload (starts at 1, may wrap to 1 at 65535 - depending on the payload type).
                          // Image specific payload entries.
     UINT32 h;            // Received height (lines) for an image payload.
     UINT32 w;            // Received width (pixels) for an image payload.
     UINT32 x_offset;     // Received x offset for origin of ROI for an image payload_type.
     UINT32 y_offset;     // Received y offset for origin of ROI for an image payload_type.
     UINT32 x_padding;    // Received x padding bytes for an image payload_type (invalid data padding end of each line [horizontal invalid]).
     UINT32 y_padding;    // Received y padding bytes for an image payload_type ( invalid data padding end of image [vertical invalid]).
     UINT32 d;            // Received pixel depth (bytes per pixel) for an image payload with a Gige Vision defined pixel format.
     UINT32 format;       // Received Gige Vision pixel format for image or JPEG data types.
                          // (If the format value is not a valid Gige Vision pixel type and the payload_type is JPEG, then the format value
                          //  is to be interpreted as a color space value (EnumCS value for JPEG) to be used by a JPEG decoder).
                          //
     PUINT8 address;      // Address of the "payload_type" data, NULL if the payload has been sent to trash (no buffer available to receive it).
                          //
                          // New entries for non-image payload types
                          //
     PUINT8 chunk_data;   // Address of "chunk" data (metadata) associated with the received payload (NULL if no "chunk" data (metadata) is available).
                          // (The "chunk_data" address is provided here as a shortcut. It is the address immediatley following the end of "paylod_type" data)
     UINT32 chunk_size;   // The size of the chunk_data (uncompressed). Zero if no "chunk" data (metadata) is available.
                          // (The "chunk_size" is provided as a helper for decoding raw TurboDrive compressed data in passthru mode).
                          //
    char  filename[256];  // Name of file for payload type "file" (0 terminated string, 255 characters maximum system limit in Linux).
    """

    _fields_ = [
        ("payload_type", c_uint32),
        ("state", c_uint32),
        ("status", c_int32),
        ("timestamp_hi", c_uint32),
        ("timestamp_lo", c_uint32),
        ("timestamp", c_uint64),
        ("recv_size", c_uint64),
        ("id", c_uint64),
        ("h", c_uint32),
        ("w", c_uint32),
        ("x_offset", c_uint32),
        ("y_offset", c_uint32),
        ("x_padding", c_uint32),
        ("y_padding", c_uint32),
        ("d", c_uint32),
        ("format", c_uint32),
        ("address", POINTER(c_uint8)),
        ("chunk_data", POINTER(c_uint8)),
        ("chunk_size", c_uint32),
        ("filename", c_char * 256),
    ]


class CameraInfo(Structure):
    _fields_ = [
        ("index", c_int),
        ("ipAddr", c_uint32),
        ("serial", c_char_p),
        ("hostInterfaceIdx", c_uint32),
    ]

    @property
    def interface_name(self) -> str:
        return if_indextoname(self.hostInterfaceIdx)

    @property
    def address(self) -> IPv4Address:
        return IPv4Address(self.ipAddr)


class BufferStats(Structure):
    _fields_ = [
        ("total", c_uint32),
        ("used", c_uint32),
        ("free", c_uint32),
        ("trashed", c_uint32),
    ]
