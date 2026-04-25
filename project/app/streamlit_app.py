"""Streamlit entrypoint for Lifecycle Intelligence Engine dashboards."""

from __future__ import annotations

from pathlib import Path
import sys

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from src.execution import run_pipeline
from src.logging_config import get_logger

logger = get_logger(__name__)


st.set_page_config(page_title="Lifecycle Intelligence Engine", layout="wide")
st.title("Lifecycle Intelligence Engine")
st.write(
    "This scaffold provides a modular foundation for large-scale CSV processing "
    "with DuckDB and interactive monitoring through Streamlit."
)

project_root = PROJECT_ROOT
if st.button("Run Placeholder Pipeline"):
    logger.info("User triggered placeholder pipeline from Streamlit UI")
    try:
        run_pipeline(project_root)
    except NotImplementedError as exc:
        st.warning(str(exc))
