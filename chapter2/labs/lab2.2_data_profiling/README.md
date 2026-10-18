# Lab 2.2 — Data Profiling

**Tool:** Python (pandas) · groups of 3–5 · start in class, finish before the next session

**Goal:** Profile before you fix — describe every column and every relationship, then write a cleaning plan.

**Scenario:** Same orders file, now together with customers.csv, the customer master list.

## Your tasks
| # | Step | How | Time |
|---|---|---|---|
| 1 | Column profile | write `profile()`: type, missing, `nunique()`, min/max or top → table A | 12 min |
| 2 | Patterns and domains | reuse the Lab 2.1 masks: which order_ids break a rule? | 6 min |
| 3 | Distribution and outliers | `quantile(.25 / .75)` → IQR rule on quantity | 7 min |
| 4 | Functional dependency | `groupby("customer_id").customer_name.nunique() > 1` ? | 5 min |
| 5 | Keys and inclusion | `is_unique` on both tables · `~isin()` for orphan orders | 6 min |
| 6 | Cleaning plan | Top 5 issues, ranked by impact on revenue → table C | 6 min |

## Files
- `Lab2.2_DataProfiling.ipynb` — notebook template (fill in the `# TODO` cells)
- `Lab2.2_ProfileReport.pptx` — editable worksheet
- `../../data/` · orders_2024_03.csv — the March orders
- `../../data/` · customers.csv — 27 rows · customer master

## How to work
Open the notebook in Jupyter or VS Code from inside this folder, so the relative path `../../data/` works.

**Rule: never overwrite the raw files** — every result goes into a new file.

## What to submit (Moodle)
- ZIP: profile report PDF + your notebook
- One representative uploads **one file per group**: `Lab2.2_Group<Nr>.zip`
- Deadline: before the next session

**Progress check (end of session):** Show your column profile and ONE relationship problem (structure analysis) you found.

[← Back to Chapter 2](../../README.md)
