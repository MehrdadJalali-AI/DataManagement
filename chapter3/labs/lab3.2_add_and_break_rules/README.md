# Lab 3.2 — Add & Break Validation Rules

**Goal:** extend `rules.py`, then break the pipeline on purpose.
**Format:** in pairs · ~15–20 min · project: [`../../shop_pipeline/`](../../shop_pipeline/)

## Tasks

1. Add **email** and **country** rules to `clean_customers_rules` in `rules.py`.
2. Run the pipeline, read which customers break your new rules, and decide: **stop or quarantine?**
3. Copy `extras/orders_2026_04.csv` into `data/raw/` and run the pipeline again.
4. Read the failure output: **which rule, which value, which row** — and why were **no outputs written**?

## Focus of this lab
- Writing quality rules as code, one line each
- Reading a failure report to find exactly which rows are bad
- Why stopping early protects every dashboard and model downstream

## Hints
- Useful checks: `Check.str_matches(...)`, `Check.isin([...])`, `nullable=False`.
- `lazy=True` reports every failure at once, not only the first one.
- When you are done, remove `orders_2026_04.csv` from `data/raw/` again.

[← Back to Chapter 3](../../README.md)
