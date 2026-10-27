# shop_pipeline — a reproducible, validated data pipeline

Starter project for **Chapter 3: Reproducible & Validated Data Pipelines** (Labs 3.1–3.3).
It turns raw online-shop order files into trusted, documented outputs with **one command**.

## Setup and run

```bash
cd chapter3/shop_pipeline
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python pipeline.py
```

Every run appends a block to `logs/run_log.txt`. Run it again — you get the same result.

## Project structure

```
shop_pipeline/
├── README.md            this file: how to run, data dictionary, cleaning rules
├── requirements.txt     pandas, pandera
├── pipeline.py          the steps: load → clean → validate → split → enrich → output
├── rules.py             validation rules (pandera), one line each
├── data/
│   ├── raw/             files exactly as received — read, never written
│   └── output/          trusted outputs (created by the pipeline)
├── logs/
│   └── run_log.txt      what happened on every run (created by the pipeline)
└── extras/
    └── orders_2026_04.csv   a new month of data — used in Lab 3.2
```

Data flows one way: **raw → clean → output**. Never backwards, never overwriting raw.

## Inputs (`data/raw/`)

| File | Contents |
|---|---|
| `orders_2026_01.csv`, `orders_2026_02.csv`, `orders_2026_03.csv` | Monthly order exports: order_id, order_date, customer_id, category, quantity, unit_price |
| `customers.csv` | Customer master: customer_id, customer_name, city, country, email, segment |

## Steps (`pipeline.py`)

| Step | Function | What it does |
|---|---|---|
| Load | `load_raw()` | Reads every `orders_*.csv` as text and adds `source_file` (start of lineage) |
| Clean | `clean_orders()`, `clean_customers()` | Removes exact duplicates, trims text, parses mixed date formats, converts numbers |
| Validate | `validate()` | Runs the rules in `rules.py`. **Critical rule broken → stop, write nothing** |
| Split | `split()` | Corrects known price issues; row-level problems → **quarantine with a reason** |
| Enrich | `enrich_orders()` | Adds the customer's city and `line_total` |
| Output | `output()` | Writes the three output files and the revenue to the run log |

**Stop or quarantine?** Stop for problems that break the whole table (e.g. a duplicate ID); quarantine problems that affect single rows (e.g. an unknown customer).

## Outputs (`data/output/`) — data dictionary

**`fct_orders.csv`** — trusted orders, ready for analysis

| Column | Meaning | Unit / rule |
|---|---|---|
| order_id | Order identifier | one capital letter + 3 digits, unique |
| order_date | Date of the order | YYYY-MM-DD |
| customer_id | Customer identifier | must exist in customers.csv |
| category | Product category | Accessories or Electronics |
| quantity | Items ordered | > 0 |
| unit_price | Price per item | EUR, ≥ 0 |
| source_file | Raw file the row came from | lineage |
| city | Customer's city | from customers.csv |
| line_total | Revenue of the order line | quantity × unit_price, EUR |

**`quarantine_orders.csv`** — rows held back: same columns as the cleaned orders plus `reason`.

**`revenue_by_city.csv`** — business summary: `city`, `line_total` (sum, EUR).

## Cleaning rules

| Rule | Where | Action |
|---|---|---|
| Exact duplicate rows | `clean_orders()` | removed |
| Dates as YYYY-MM-DD or DD.MM.YYYY | `parse_mixed_date()` | unified |
| order_id unique, not empty, pattern `^[A-Z]\d{3}$` | `rules.py` | stop |
| category in the allowed list | `rules.py` | stop |
| unit_price ≥ 0 | `rules.py` | stop |
| March export has prices in cents | `split()` | divided by 100 |
| quantity ≤ 0, missing price, missing date, unknown customer | `split()` | quarantine |
