# Lifecycle Intelligence Engine (Scaffold)

## Purpose

This project scaffold defines a modular, scalable structure for a **Lifecycle Intelligence Engine** built with **DuckDB** and **Streamlit**. It is designed for data-intensive workloads where raw CSV inputs can reach **5-10GB** and therefore separates ingestion, staging, feature engineering, scoring, segmentation, and insight generation into dedicated modules.

## Project Layout

```text
project/
├── data/
│   ├── raw/               # Place incoming CSV files here
│   └── db/                # DuckDB database files
├── src/
│   ├── data_loader.py     # DuckDB connection + CSV ingestion placeholders
│   ├── staging.py         # Staging transformation placeholders
│   ├── features.py        # Feature engineering placeholders
│   ├── scoring.py         # Scoring placeholders
│   ├── segmentation.py    # Segmentation placeholders
│   ├── insights.py        # Insights/output placeholders
│   ├── execution.py       # Pipeline orchestration placeholder
│   └── logging_config.py  # Shared logging setup
├── app/
│   └── streamlit_app.py   # Streamlit UI entrypoint
├── sql/
│   ├── staging.sql        # SQL template for staging layer
│   └── features.sql       # SQL template for feature layer
├── outputs/               # Generated artifacts/reports
├── requirements.txt
└── README.md
```

## Expected Input Files

Put source CSV files into:

- `project/data/raw/`

The current scaffold does not enforce a fixed schema yet; schema contracts can be added when business logic is implemented.

## How to Run

1. Create and activate a virtual environment (recommended).
2. Install dependencies:

   ```bash
   pip install -r project/requirements.txt
   ```

3. Launch the Streamlit app:

   ```bash
   streamlit run project/app/streamlit_app.py
   ```

4. Open the local URL shown by Streamlit (typically `http://localhost:8501`).

## Notes

- The code intentionally includes placeholders with `NotImplementedError` so you can fill in business logic incrementally.
- Logging is centralized in `src/logging_config.py` for consistent observability across modules.
