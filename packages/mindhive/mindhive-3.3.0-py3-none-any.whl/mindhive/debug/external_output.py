import os


def block_external_output() -> bool:
    return bool(os.getenv("BLOCK_EXTERNAL_OUTPUT"))
