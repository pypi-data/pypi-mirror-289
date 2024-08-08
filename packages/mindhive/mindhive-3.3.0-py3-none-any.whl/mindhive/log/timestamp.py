import re
from datetime import datetime, timezone
from pathlib import Path

TIMESPEC = "microseconds"


def as_datatime(timestamp: str | float | datetime) -> datetime:
    """Will always return an aware datetime"""
    if isinstance(timestamp, datetime):
        if timestamp.tzinfo is None:
            # What to do here is ambiguous, assume naive objects are in local timezone
            return timestamp.astimezone()
        return timestamp
    if isinstance(timestamp, str):
        # REVISIT: replace "Z" not needed from Python 3.11
        return datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    return datetime.fromtimestamp(timestamp, tz=timezone.utc)


def timestamp_to_iso(timestamp: datetime | float) -> str:
    return as_datatime(timestamp).isoformat(timespec=TIMESPEC).replace("+00:00", "Z")


def timestamp_from_iso(iso_ts: str) -> float:
    return as_datatime(iso_ts).timestamp()


def timestamp_for_filename(timestamp: datetime | float) -> str:
    return (
        as_datatime(timestamp)
        .astimezone(timezone.utc)
        .replace(tzinfo=None)  # We don't want timezone data in the output
        .isoformat(".", timespec=TIMESPEC)
        .replace(":", "-")
    )


def timestamp_for_log(timestamp: datetime | float, strftime_format_with_microseconds: str = "%H:%M:%S.%f"):
    return as_datatime(timestamp).strftime(strftime_format_with_microseconds)[:-5]


def time_range_for_log(start: float, end: float) -> str:
    start_dt = as_datatime(start)
    end_dt = as_datatime(end)
    if start_dt.hour != end_dt.hour:
        end_format = "%H:%M:%S.%f"
    elif start_dt.minute != end_dt.minute:
        end_format = ":%M:%S.%f"
    else:
        end_format = ":%S.%f"
    diff_s = (end_dt - start_dt).total_seconds()
    return f"{timestamp_for_log(start)} +{diff_s:.1f}s ->{timestamp_for_log(end, end_format)}"


PATH_TIMESTAMP = re.compile(r"\d{4}-\d{2}-\d{2}\.\d{2}-\d{2}-\d{2}\.\d{6}")


def parse_path_timestamp(path: str | Path) -> float:
    path = str(path)
    timestamps = PATH_TIMESTAMP.findall(path)
    if not timestamps:
        raise ValueError(f"No timestamp found in path {path}")
    return datetime.strptime(timestamps[-1], "%Y-%m-%d.%H-%M-%S.%f").replace(tzinfo=timezone.utc).timestamp()
