# Chapter 3 — Reproducible & Validated Data Pipelines · Lab Exercises

**Data Management** — Prof. Dr. Mehrdad Jalali, SRH University of Applied Sciences Heidelberg

In Chapter 2 we cleaned the data once, by hand. Next month new files arrive — so the cleaning must run **the same way again, with one command**, and **prove** that the result is right.

Interactive study guide: [Chapter 3 page](https://mehrdadjalali-ai.github.io/DataManagement/interactive/Chapter3_Reproducible_Pipelines.html)

## The labs

| Lab | Topic | Format | Files |
|---|---|---|---|
| [3.1](labs/lab3.1_run_and_read/) | Run & read a validated pipeline | pairs · ~25–30 min | `shop_pipeline/` |
| [3.2](labs/lab3.2_add_and_break_rules/) | Add & break validation rules | pairs · ~15–20 min | `shop_pipeline/`, `extras/orders_2026_04.csv` |
| [3.3](labs/lab3.3_extend_document_version/) | Extend, document & version (home) | groups · deadline next Friday | your own GitHub repository |

## The starter project — [`shop_pipeline/`](shop_pipeline/)

A small online-shop pipeline: three monthly order files and a customer list go in; trusted orders, a quarantine file with reasons, revenue by city and a run log come out. Setup and data dictionary: [shop_pipeline/README.md](shop_pipeline/README.md).

```bash
cd chapter3/shop_pipeline
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python pipeline.py
```

## Requirements
- Python ≥ 3.10
- pandas, pandera (installed from `shop_pipeline/requirements.txt`)
- Git and a GitHub account (Lab 3.3)
