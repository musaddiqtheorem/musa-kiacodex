"""Pipeline orchestration entry points for end-to-end execution."""

from __future__ import annotations

from pathlib import Path

from .features import generate_features
from .insights import build_insights
from .logging_config import get_logger
from .scoring import score_entities
from .segmentation import segment_population
from .staging import build_staging_tables

logger = get_logger(__name__)


def run_pipeline(project_root: Path) -> None:
    """Placeholder orchestrator for the full lifecycle intelligence pipeline.

    Args:
        project_root: Root directory containing data, SQL, and output folders.
    """
    db_path = project_root / "data" / "db" / "lifecycle.duckdb"
    staging_sql = project_root / "sql" / "staging.sql"
    features_sql = project_root / "sql" / "features.sql"
    output_dir = project_root / "outputs"

    logger.info("Pipeline placeholder started for %s", project_root)
    build_staging_tables(db_path=db_path, sql_path=staging_sql)
    generate_features(db_path=db_path, sql_path=features_sql)
    score_entities(db_path=db_path)
    segment_population(db_path=db_path)
    build_insights(db_path=db_path, output_dir=output_dir)
