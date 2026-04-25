"""Shared logging utilities for Lifecycle Intelligence Engine modules."""

from __future__ import annotations

import logging


def setup_logging(level: int = logging.INFO) -> None:
    """Configure application-wide logging once.

    Parameters
    ----------
    level:
        Logging level applied to the root logger.
    """
    if not logging.getLogger().handlers:
        logging.basicConfig(
            level=level,
            format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        )
