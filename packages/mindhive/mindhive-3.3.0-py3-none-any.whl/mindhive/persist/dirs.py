import os
from pathlib import Path


DEFAULT_VAR_DIR = "/var"
VAR_DIR = Path(os.getenv("VAR_DIR", DEFAULT_VAR_DIR))
STORE_DIR = VAR_DIR / "mindhive/store"
