"""Streamlit entry point for the Lifecycle Intelligence Engine UI."""

from __future__ import annotations

import logging
import sys
from pathlib import Path

import streamlit as st

# Allow imports from project/src when running the app directly.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.append(str(SRC_PATH))

from data_loader import get_connection  # noqa: E402
from logging_utils import setup_logging  # noqa: E402

setup_logging()
logger = logging.getLogger(__name__)


def main() -> None:
    """Render a lightweight placeholder UI for the lifecycle app."""
    st.set_page_config(page_title="Lifecycle Intelligence Engine", layout="wide")
    st.title("Lifecycle Intelligence Engine")
    st.write(
        "This Streamlit app is scaffolded for large-scale lifecycle analytics "
        "powered by DuckDB."
    )

    if st.button("Test DuckDB Connection"):
        try:
            conn = get_connection()
            conn.close()
            st.success("DuckDB connection established successfully.")
            logger.info("DuckDB connectivity check passed.")
        except Exception as exc:  # pragma: no cover
            st.error(f"Connection failed: {exc}")
            logger.exception("DuckDB connectivity check failed.")


if __name__ == "__main__":
    main()
