# Lab 3.1 — Run & Read a Validated Pipeline

**Goal:** run the starter pipeline and connect every rule to Chapter 2.
**Format:** in pairs · ~25–30 min · project: [`../../shop_pipeline/`](../../shop_pipeline/)

## Tasks

1. Go to `chapter3/shop_pipeline`, create a virtual environment and run `pip install -r requirements.txt` (see the project README).
2. Run `python pipeline.py` and check the log: **12 trusted orders, 4 quarantined, EUR 4,015**.
3. Open `rules.py` and match each rule to a **Chapter 2 quality dimension**. Then read `data/output/quarantine_orders.csv`.
4. Remove the **price-correction line** in `split()`, rerun, and explain why revenue jumps to **EUR 12,565**. Put the line back afterwards.

## Focus of this lab
- The pipeline flow: load → clean → validate → split → output
- Reading the run log and the quarantine file
- Linking every rule to a Chapter 2 quality dimension

## Questions to answer
- Which rule checks uniqueness, which completeness, which validity?
- For each quarantined row: what is the reason, and from which raw file does it come?
- Why does the log say 17 rows but the split adds up to 16?
- What exactly did the price-correction line fix, and how could you have spotted the problem without it?

[← Back to Chapter 3](../../README.md)
