# Lab 2.4 — Transformation & Integration

**Tool:** Python (pandas) · groups of 3–5 · start in class, finish before the next session

**Goal:** Make the data analysis-ready: one currency, new features, both months, and the customer segment.

**Scenario:** The manager asks: revenue in EUR by city and by customer segment, for March and April.

## Your tasks
| # | Step | How | Time |
|---|---|---|---|
| 1 | Convert currency | `map()` the given rates: 1 CHF = 1.04 EUR, 1 USD = 0.92 EUR | 5 min |
| 2 | Create features | `line_total_eur = quantity × unit_price_eur` · `pd.cut` → order_size | 6 min |
| 3 | Union April | compare columns first! `rename(price → unit_price)` · `pd.concat` | 7 min |
| 4 | Join customers | `merge(how="left")` · print `len()` before and after — explain! | 8 min |
| 5 | Encode and scale | `pd.get_dummies(category)` · min-max scale line_total_eur | 6 min |
| 6 | Aggregate | groupby city / segment · sum · top 3 cities | 6 min |

## Files
- `Lab2.4_Transformation.ipynb` — notebook template (fill in the `# TODO` cells)
- `Lab2.4_TransformationLog.pptx` — editable worksheet
- `../lab2.3_data_cleaning/` · orders_2024_03_clean.csv — your output of Lab 2.3
- `../../data/` · orders_2024_04.csv — 6 April orders
- `../../data/` · customers.csv — segment per customer

## How to work
Open the notebook in Jupyter or VS Code from inside this folder, so the relative path `../../data/` works.

**Run Lab 2.3 first** — this lab loads `../lab2.3_data_cleaning/orders_2024_03_clean.csv`, the file your Lab 2.3 notebook writes.

**Rule: never overwrite the raw files** — every result goes into a new file.

## What to submit (Moodle)
- ZIP: notebook + final CSV + transformation log PDF
- One representative uploads **one file per group**: `Lab2.4_Group<Nr>.zip`
- Deadline: before the next session

**Progress check (end of session):** Show your row counts after the union and the join — and explain the difference.

[← Back to Chapter 2](../../README.md)
