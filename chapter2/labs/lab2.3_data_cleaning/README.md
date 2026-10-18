# Lab 2.3 — Data Cleaning

**Tool:** Python (pandas) · groups of 3–5 · start in class, finish before the next session

**Goal:** Turn your cleaning plan into a clean dataset — and document every decision.

**Scenario:** Use your plan from Lab 2.2. The raw file stays untouched: you always work on a copy.

## Your tasks
| # | Step | How | Time |
|---|---|---|---|
| 1 | Protect the raw data | `df = raw.copy()` — results only ever go to NEW files | 3 min |
| 2 | Remove duplicates | `drop_duplicates()` · log rows before → after | 4 min |
| 3 | Standardize formats | dates → YYYY-MM-DD · `str.strip()` · `replace()` for city, country, currency | 10 min |
| 4 | Handle missing values | `map()` names from customers.csv · flag column · or quarantine | 8 min |
| 5 | Invalid values and outliers | a reason column → quarantine DataFrame (−1, 500, no price, Gadgets) | 8 min |
| 6 | Validate and write | re-run the Lab 2.1 checks · `to_csv`: clean + quarantine | 5 min |

## Files
- `Lab2.3_DataCleaning.ipynb` — notebook template (fill in the `# TODO` cells)
- `Lab2.3_CleaningLog.pptx` — editable worksheet
- `../../data/` · orders_2024_03.csv — raw, never overwrite
- `../../data/` · customers.csv — to fill missing names

## How to work
Open the notebook in Jupyter or VS Code from inside this folder, so the relative path `../../data/` works.

The last step writes `orders_2024_03_clean.csv` and `orders_2024_03_quarantine.csv` into this folder. Lab 2.4 needs the clean file. (Generated files are not committed to the repo.)

**Rule: never overwrite the raw files** — every result goes into a new file.

## What to submit (Moodle)
- ZIP: notebook + clean CSV + quarantine CSV + log PDF
- One representative uploads **one file per group**: `Lab2.3_Group<Nr>.zip`
- Deadline: before the next session

**Progress check (end of session):** Show your cleaning log and ONE decision your group discussed — what else could you have done?

[← Back to Chapter 2](../../README.md)
