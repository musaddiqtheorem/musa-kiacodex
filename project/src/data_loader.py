"""Data ingestion utilities for loading large CSV files into DuckDB."""

from __future__ import annotations

import logging
from pathlib import Path

import duckdb

from logging_utils import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


DEFAULT_DB_PATH = Path("project/data/db/lifecycle.duckdb")


def get_connection(db_path: Path = DEFAULT_DB_PATH) -> duckdb.DuckDBPyConnection:
    """Create and return a reusable DuckDB connection.

    Parameters
    ----------
    db_path:
        Path to the DuckDB database file.

    Returns
    -------
    duckdb.DuckDBPyConnection
        Active DuckDB connection for downstream modules.
    """
    logger.info("Opening DuckDB connection at %s", db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return duckdb.connect(str(db_path))


def load_raw_csv_to_duckdb(csv_path: Path, table_name: str) -> None:
    """Placeholder to stream-load a raw CSV file into DuckDB.

    Intended to handle multi-GB CSV files with chunked or SQL-native ingestion.
    """
    logger.info("Requested CSV load for %s into table %s", csv_path, table_name)
    raise NotImplementedError("CSV ingestion logic will be implemented in a later phase.")
