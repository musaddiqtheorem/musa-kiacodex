"""Staging-layer transformations for normalizing source data."""

from __future__ import annotations

from pathlib import Path

from .logging_config import get_logger

logger = get_logger(__name__)


def build_staging_tables(db_path: Path, sql_path: Path) -> None:
    """Placeholder for executing staging SQL against DuckDB.

    Args:
        db_path: Location of the DuckDB database file.
        sql_path: SQL file defining staging transformations.
    """
    logger.info("Staging placeholder called with SQL file %s", sql_path)
    raise NotImplementedError("Staging logic will be implemented later.")
