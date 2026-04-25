"""Segmentation module for grouping entities by lifecycle behavior."""

from __future__ import annotations

import logging

from logging_utils import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


def segment_entities() -> None:
    """Placeholder for cohort and segment assignment.

    Segments should combine engineered features and scores to define
    actionable groups such as retention risk or growth potential.
    """
    logger.info("Segmenting entities placeholder")
    raise NotImplementedError("Segmentation logic will be implemented later.")
