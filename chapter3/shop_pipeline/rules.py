"""Validation rules for the shop pipeline - one line per rule.

Each rule is a Chapter 2 data-quality check, written once and run on every run.
If a rule here fails, the pipeline STOPS and writes nothing (see pipeline.validate).
Row-level problems (bad quantity, unknown customer, ...) are handled in
pipeline.split() and go to the quarantine file instead.
"""
import pandera.pandas as pa
from pandera.pandas import Column, Check

clean_orders_rules = pa.DataFrameSchema({
    "order_id":    Column(str, unique=True, nullable=False,
                          checks=Check.str_matches(r"^[A-Z]\d{3}$")),
    "customer_id": Column(str, nullable=False),
    "category":    Column(str, Check.isin(["Accessories", "Electronics"])),
    "quantity":    Column(float, nullable=True),
    "unit_price":  Column(float, Check.ge(0), nullable=True),
})

clean_customers_rules = pa.DataFrameSchema({
    "customer_id":   Column(str, unique=True, nullable=False,
                            checks=Check.str_matches(r"^C\d{3}$")),
    "customer_name": Column(str, nullable=False),
    "city":          Column(str, nullable=False),
    # Lab 3.2: add rules for 'email' and 'country' here
})
