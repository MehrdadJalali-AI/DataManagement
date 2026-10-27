"""Shop pipeline - Chapter 3: Reproducible & Validated Data Pipelines.

Run from this folder with:   python pipeline.py

Flow: load -> clean -> validate -> split -> enrich -> output
  data/raw/      read only, never written
  data/output/   fct_orders.csv, quarantine_orders.csv, revenue_by_city.csv
  logs/          run_log.txt (one block per run)
"""
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd
import pandera.pandas as pa

import rules

BASE = Path(__file__).parent
RAW = BASE / "data" / "raw"
OUT = BASE / "data" / "output"
LOG = BASE / "logs" / "run_log.txt"

log_lines = []


def log(msg):
    print(msg)
    log_lines.append(msg)


def write_log(status):
    LOG.parent.mkdir(exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"=== run {datetime.now():%Y-%m-%d %H:%M:%S} - {status} ===\n")
        f.write("\n".join(log_lines) + "\n\n")


# ---------- reusable cleaning functions ----------
def parse_mixed_date(col):
    """Dates arrive as YYYY-MM-DD or DD.MM.YYYY - accept both."""
    iso = pd.to_datetime(col, format="%Y-%m-%d", errors="coerce")
    de = pd.to_datetime(col, format="%d.%m.%Y", errors="coerce")
    return iso.fillna(de)


# ---------- steps: one function = one job ----------
def load_raw():
    """Read every orders_*.csv as text and record its source file (lineage)."""
    frames = []
    for f in sorted(RAW.glob("orders_*.csv")):
        df = pd.read_csv(f, dtype=str, keep_default_na=False)
        df["source_file"] = f.name
        frames.append(df)
    orders = pd.concat(frames, ignore_index=True)
    customers = pd.read_csv(RAW / "customers.csv", dtype=str, keep_default_na=False)
    log(f"Loaded {len(orders)} order rows from {len(frames)} files, {len(customers)} customers")
    return orders, customers


def clean_orders(orders):
    """Remove exact duplicates, trim text, convert types on purpose."""
    before = len(orders)
    df = orders.drop_duplicates().copy()
    log(f"Removed {before - len(df)} exact duplicate(s): {before} -> {len(df)} rows")
    for c in ["order_id", "customer_id", "category"]:
        df[c] = df[c].str.strip()
    df["order_date"] = parse_mixed_date(df["order_date"])
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").astype(float)
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce").astype(float)
    return df


def clean_customers(customers):
    df = customers.copy()
    for c in df.columns:
        df[c] = df[c].str.strip()
    return df


def validate(orders, customers):
    """Critical rules: if any fails, STOP and write nothing."""
    try:
        rules.clean_orders_rules.validate(orders, lazy=True)
        rules.clean_customers_rules.validate(customers, lazy=True)
    except pa.errors.SchemaErrors as err:
        log("VALIDATION FAILED - pipeline stopped, no outputs written:")
        cases = err.failure_cases[["column", "check", "failure_case", "index"]]
        log(cases.to_string(index=False))
        write_log("FAILED")
        sys.exit(1)
    log("Validation passed: all critical rules OK")


def split(orders, customers):
    """Row-level problems go to quarantine with a reason; the rest is trusted."""
    df = orders.copy()
    # price correction: the March export stores prices in cents
    df.loc[df["source_file"] == "orders_2026_03.csv", "unit_price"] /= 100

    reason = pd.Series("", index=df.index)
    reason[df["order_date"].isna()] = "missing order_date"
    reason[df["unit_price"].isna()] = "missing unit_price"
    reason[~df["customer_id"].isin(customers["customer_id"])] = "unknown customer"
    reason[df["quantity"] <= 0] = "quantity <= 0"
    df["reason"] = reason

    quarantine = df[df["reason"] != ""]
    trusted = df[df["reason"] == ""].drop(columns="reason")
    log(f"Split: {len(trusted)} trusted, {len(quarantine)} quarantined")
    return trusted, quarantine


def enrich_orders(trusted, customers):
    """Add line_total and the customer's city."""
    df = trusted.merge(customers[["customer_id", "city"]], on="customer_id", how="left")
    df["line_total"] = (df["quantity"] * df["unit_price"]).round(2)
    return df


def output(fct, quarantine):
    OUT.mkdir(parents=True, exist_ok=True)
    fct.to_csv(OUT / "fct_orders.csv", index=False)
    quarantine.to_csv(OUT / "quarantine_orders.csv", index=False)
    revenue = (fct.groupby("city", as_index=False)["line_total"].sum().round(2)
                  .sort_values("line_total", ascending=False))
    revenue.to_csv(OUT / "revenue_by_city.csv", index=False)
    log(f"Revenue: EUR {fct['line_total'].sum():,.0f}")
    log("Wrote fct_orders.csv, quarantine_orders.csv, revenue_by_city.csv")


def main():
    raw_orders, raw_customers = load_raw()
    orders = clean_orders(raw_orders)
    customers = clean_customers(raw_customers)
    validate(orders, customers)
    trusted, quarantine = split(orders, customers)
    fct = enrich_orders(trusted, customers)
    output(fct, quarantine)
    write_log("SUCCESS")


if __name__ == "__main__":
    main()
