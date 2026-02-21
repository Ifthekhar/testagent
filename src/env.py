"""Environment loading helpers."""

from __future__ import annotations

import os
from pathlib import Path


def load_env(
    path: str | Path = ".env",
    key: str = "",
) -> dict[str, str]:
    """Load KEY=VALUE lines from a .env file into os.environ if not already set.

    If `key` is provided, only that key is loaded/returned.
    """
    env_path = Path(path)
    if not env_path.exists():
        return {}

    key_filter = key.strip() or None
    loaded: dict[str, str] = {}

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        if key_filter is not None and key != key_filter:
            continue
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value
            loaded[key] = value
        elif key:
            loaded[key] = os.environ[key]

    return loaded
