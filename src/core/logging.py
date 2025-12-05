# logging/format helpers

import logging
import logging.config
import os
from typing import Optional

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

DEFAULT_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        },
        "short": {
            "format": "%(levelname)s | %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": LOG_LEVEL,
        }
    },
    "root": {
        "handlers": ["console"],
        "level": LOG_LEVEL,
    },
    "loggers": {
        # Keep uvicorn logs readable
        "uvicorn": {"handlers": ["console"], "level": LOG_LEVEL, "propagate": False},
        "uvicorn.error": {"handlers": ["console"], "level": LOG_LEVEL, "propagate": False},
        "uvicorn.access": {"handlers": ["console"], "level": "INFO", "propagate": False},
    },
}

def init_logging(config: Optional[dict] = None) -> None:
    """
    Initialize logging with the provided config or DEFAULT_CONFIG.
    Call this once at app startup (e.g., in src/app/main.py).
    """
    cfg = config or DEFAULT_CONFIG
    logging.config.dictConfig(cfg)
