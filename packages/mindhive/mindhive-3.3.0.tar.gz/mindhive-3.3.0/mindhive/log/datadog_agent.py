import os


def has_datadog_agent() -> bool:
    return bool(os.getenv("DATADOG_AGENT"))
