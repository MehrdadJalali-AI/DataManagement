# Chapter 2 — Data Quality, Profiling & Preparation · Lab Exercises

**Data Management** — Prof. Dr. Mehrdad Jalali, SRH University of Applied Sciences Heidelberg

One messy online-shop dataset travels through five labs: first in Python (pandas, Jupyter), then again as a Tableau Prep flow.
Your manager asks: *"I need revenue by city and by customer segment for March and April. Can we trust these files?"*

Slides with all task descriptions: [`slides/C2_Labs.pptx`](slides/C2_Labs.pptx) · Interactive study guide: [Chapter 2 page](https://mehrdadjalali-ai.github.io/DataManagement/interactive/Chapter2_Data_Quality_Preparation.html)

## The five labs

| Lab | Topic | Tool | Files | Deliverable (ZIP) |
|---|---|---|---|---|
| [2.1](labs/lab2.1_data_quality/) | Data Quality Audit | Python (pandas) | `Lab2.1_QualityAudit.ipynb` · `Lab2.1_QualityAudit.pptx` | worksheet PDF + your notebook (.ipynb) |
| [2.2](labs/lab2.2_data_profiling/) | Data Profiling | Python (pandas) | `Lab2.2_DataProfiling.ipynb` · `Lab2.2_ProfileReport.pptx` | profile report PDF + your notebook |
| [2.3](labs/lab2.3_data_cleaning/) | Data Cleaning | Python (pandas) | `Lab2.3_DataCleaning.ipynb` · `Lab2.3_CleaningLog.pptx` | notebook + clean CSV + quarantine CSV + log PDF |
| [2.4](labs/lab2.4_transformation/) | Transformation & Integration | Python (pandas) | `Lab2.4_Transformation.ipynb` · `Lab2.4_TransformationLog.pptx` | notebook + final CSV + transformation log PDF |
| [2.5](labs/lab2.5_tableau_prep/) | All Labs Again — in Tableau Prep | Tableau Prep Builder | `Lab2.5_FlowReport.pptx` | packaged flow (.tflx) + output CSV + report PDF |

Labs build on each other: **Lab 2.4 loads the clean file written by your Lab 2.3 notebook**, and Lab 2.5 rebuilds Labs 2.1–2.4 in Tableau Prep so you can compare row counts and revenue.

## The dataset — [`data/`](data/)

| File | Rows · columns | Contents |
|---|---|---|
| `orders_2024_03.csv` | 32 · 12 | The March export from the shop system — the messy one (used in all labs) |
| `customers.csv` | 27 · 5 | Customer master list: customer_id, name, city, segment, signup date |
| `orders_2024_04.csv` | 6 · 11 | The April export — arrives in Lab 2.4 (note: its columns are not the same as March!) |

Some problems are already visible in the first rows. Most are not.

## How to work
1. Download or clone the repository and **keep the folder structure** — the notebooks load the data with relative paths (`../../data/…`).
2. Open the notebook of the lab in **Jupyter** or **VS Code** from inside its lab folder.
3. Fill in every cell marked `# TODO`; at the end *Kernel › Restart & Run All* must work.
4. Write your numbers and decisions into the lab's worksheet (`.pptx`) and export it as PDF.
5. **Never overwrite the raw files** in `data/` — every result goes into a new file.

## Submission rules
- Work in **groups of 3–5**; start in class, finish before the next session.
- **One representative uploads ONE ZIP per group on Moodle.**
- File name: `Lab2.x_Group<Nr>.zip` (e.g. `Lab2.3_Group4.zip`).
- Deadline: **before the next session**.
- A short progress check takes place at the end of each session.

## Requirements
- Python ≥ 3.10 with pandas, numpy and jupyter: `pip install -r requirements.txt` (from the repository root)
- Lab 2.5: Tableau Prep Builder (course licence)
