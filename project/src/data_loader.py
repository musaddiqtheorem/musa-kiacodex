"""Data loading entry points for large CSV ingestion into DuckDB."""

from __future__ import annotations

from pathlib import Path

import duckdb

from .logging_config import get_logger

logger = get_logger(__name__)


def get_duckdb_connection(db_path: Path) -> duckdb.DuckDBPyConnection:
    """Create and return a reusable DuckDB connection.

    Args:
        db_path: Location of the DuckDB database file.

    Returns:
        Active DuckDB connection object.
    """
    logger.info("Opening DuckDB connection at %s", db_path)
    return duckdb.connect(str(db_path))


def ingest_raw_csvs(raw_data_dir: Path, db_path: Path) -> None:
    """Placeholder for streaming raw CSV ingestion into DuckDB.

    This function is intended to read potentially multi-gigabyte files from
    ``raw_data_dir`` and load them into staging tables in DuckDB.

    Args:
        raw_data_dir: Directory containing source CSV files.
        db_path: Location of the DuckDB database file.
    """
    logger.info("Ingestion placeholder called for %s", raw_data_dir)
    _ = get_duckdb_connection(db_path)
    raise NotImplementedError("CSV ingestion logic will be added in a future iteration.")
