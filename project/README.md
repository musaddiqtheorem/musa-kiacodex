# Lifecycle Intelligence Engine

A modular, scalable Python scaffold for a **Lifecycle Intelligence Engine** using **DuckDB** and **Streamlit**.  
The project is designed for data-intensive workflows and large CSV inputs (5–10GB), with clear module boundaries for ingestion, transformation, feature engineering, scoring, segmentation, insights, and execution orchestration.

## Project Purpose

This repository provides a clean starting structure for building lifecycle analytics pipelines that:
- ingest large raw CSV files,
- process and stage data in DuckDB,
- build lifecycle features,
- score and segment entities,
- surface insights through a Streamlit application.

> Business logic is intentionally not implemented yet.

## Project Structure

```text
project/
├── data/
│   ├── raw/
│   └── db/
├── src/
│   ├── data_loader.py
│   ├── staging.py
│   ├── features.py
│   ├── scoring.py
│   ├── segmentation.py
│   ├── insights.py
│   ├── execution.py
│   └── logging_utils.py
├── app/
│   └── streamlit_app.py
├── sql/
│   ├── staging.sql
│   └── features.sql
├── outputs/
├── requirements.txt
└── README.md
```

## Expected Input Files

Place source CSV files in:

- `project/data/raw/`

Example expected file types:
- customer master records
- event/activity logs
- transactions/subscriptions

The app and pipeline are intended to support very large CSV files (5–10GB) with DuckDB-backed processing patterns.

## Setup

```bash
cd project
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the Streamlit App

From the repository root:

```bash
streamlit run project/app/streamlit_app.py
```

## Notes

- Module functions are placeholders with docstrings for future implementation.
- Logging is configured consistently through `src/logging_utils.py`.
- SQL files are stubs for staged and feature-level transformations.
