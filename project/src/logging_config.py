"""Shared logging configuration for the Lifecycle Intelligence Engine."""

from __future__ import annotations

import logging
from typing import Optional

_LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"


def configure_logging(level: int = logging.INFO) -> None:
    """Configure global logging once for all project modules.

    Args:
        level: Standard Python logging level.
    """
    root_logger = logging.getLogger()
    if not root_logger.handlers:
        logging.basicConfig(level=level, format=_LOG_FORMAT)


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """Return a module-level logger configured by ``configure_logging``.

    Args:
        name: Logger name. If ``None``, uses the root logger.

    Returns:
        Configured ``logging.Logger`` instance.
    """
    configure_logging()
    return logging.getLogger(name)
