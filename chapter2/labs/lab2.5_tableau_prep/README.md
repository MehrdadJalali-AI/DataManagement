# Lab 2.5 — All Labs Again — in Tableau Prep

**Tool:** Tableau Prep Builder · groups of 3–5 · start in class, finish before the next session

**Goal:** Rebuild Labs 2.1–2.4 as one visual, repeatable Tableau Prep flow — and compare it with your Python result.

**Scenario:** Same three files. If next month's data arrives, your flow should do everything again with one click.

## Your tasks
| # | Step | How | Time |
|---|---|---|---|
| 1 | Input and profile | Connect orders_2024_03.csv · Clean step: find 3 issues from Lab 2.2 in the profile pane | 8 min |
| 2 | Clean | Remove duplicates · fix types and dates · group city variants · filter quarantine rows | 12 min |
| 3 | Transform | Calculated fields: unit_price_eur, line_total_eur, order_size | 6 min |
| 4 | Union and join | Union April (rename price) · deduplicate customers · left join | 10 min |
| 5 | Aggregate and output | Aggregate step: revenue by city · Output: CSV | 5 min |
| 6 | Compare | Row counts and revenue: same as your Python result? If not — why? | 5 min |

## Files
- `Lab2.5_FlowReport.pptx` — editable worksheet
- `../../data/` · orders_2024_03.csv + orders_2024_04.csv
- `../../data/` · customers.csv — segment

## How to work
Open Tableau Prep Builder and connect the CSV files in `../../data/` (Text file input).

**Rule: never overwrite the raw files** — every result goes into a new file.

## What to submit (Moodle)
- ZIP: packaged flow (.tflx) + output CSV + report PDF
- One representative uploads **one file per group**: `Lab2.5_Group<Nr>.zip`
- Deadline: before the next session

**Progress check (end of session):** Run your flow live: show the Changes pane and the final row count.

[← Back to Chapter 2](../../README.md)
