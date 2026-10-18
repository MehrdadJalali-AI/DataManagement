# Lab 2.1 — Data Quality Audit

**Tool:** Python (pandas) · groups of 3–5 · start in class, finish before the next session

**Goal:** Measure how good the shop data is — dimension by dimension, in numbers.

**Scenario:** Your manager wants revenue by city for March. Before anyone builds a dashboard: can we trust this file?

## Your tasks
| # | Step | How | Time |
|---|---|---|---|
| 1 | Load and look | `pd.read_csv(…, dtype=str)` · `df.shape` · `df.head(10)` | 5 min |
| 2 | One issue per dimension | `value_counts()`, `sort_values()` → one example per dimension → table A | 12 min |
| 3 | Completeness | `(df == "").sum()` per column → completeness rate | 6 min |
| 4 | Uniqueness | `df.duplicated()` · `order_id.duplicated()` → duplication rate | 4 min |
| 5 | Validity | one boolean mask per rule: `str.match` · `isin` · `> 0` → validity rate | 8 min |
| 6 | Timeliness + verdict | `pd.to_datetime` · delay in days ≤ 2? · fit for purpose? | 5 min |

## Files
- `Lab2.1_QualityAudit.ipynb` — notebook template (fill in the `# TODO` cells)
- `Lab2.1_QualityAudit.pptx` — editable worksheet
- `../../data/` · orders_2024_03.csv — 32 rows · 12 columns
- `../../data/` · customers.csv — reference for accuracy

## How to work
Open the notebook in Jupyter or VS Code from inside this folder, so the relative path `../../data/` works.

**Rule: never overwrite the raw files** — every result goes into a new file.

## What to submit (Moodle)
- ZIP: worksheet PDF + your notebook (.ipynb)
- One representative uploads **one file per group**: `Lab2.1_Group<Nr>.zip`
- Deadline: before the next session

**Progress check (end of session):** Show your KPI table and the ONE issue you would fix first — and why.

[← Back to Chapter 2](../../README.md)
