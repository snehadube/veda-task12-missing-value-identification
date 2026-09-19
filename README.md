# Task 12 – Missing Value Identification
**Veda Technology Internship | Data Analytics Track | Level 1, Day 12**
**Intern:** Sneha Dubey

## 📌 Description
Identify missing values in the dataset and summarize where they occur.

## 🎯 Objective
Learn basic missing-data inspection using Excel, Python, and Pandas.

## 🛠️ Tools Used
- Python 3
- Pandas
- Matplotlib (visualization)
- Microsoft Excel (openpyxl / formulas)

## 📂 Repository Structure
```
├── train_data.csv                        # Dataset used (Titanic, pre-processed)
├── missing_value_identification.py       # Python script: full analysis
├── missing_value_summary.csv             # Missing value counts & % per column
├── missing_value_chart.png               # Bar chart of missing values per column
├── Task12_Missing_Value_Analysis.xlsx    # Excel workbook (Data, Summary, Findings sheets)
├── findings.md                           # Short findings (also below)
└── README.md
```

## 🔍 Methodology
1. Loaded `train_data.csv` with Pandas.
2. Used `df.isnull().sum()` to count missing values per column and converted to a percentage.
3. Cross-checked with Excel's `COUNTBLANK()` formula for the same result.
4. Ran extra data-quality checks: duplicate rows, duplicate `PassengerId`, and a `Fare == 0` check to catch possible hidden/placeholder missing values.
5. Visualized missing counts per column with a bar chart.

## ✅ Short Findings
- Dataset: **792 rows × 16 columns** (pre-processed/normalized Titanic dataset).
- **0 missing (null) values** found in any column — overall missing % = **0.00%**.
- **0 duplicate rows** and **0 duplicate `PassengerId`** values.
- **12 rows** have `Fare == 0` — not a null, but flagged as a possible hidden/placeholder missing value inherited from the raw dataset.
- **Conclusion:** The dataset is already clean/normalized. In the raw Titanic dataset, `Age`, `Cabin`, and `Embarked` are the columns that typically hold missing values and would need imputation before this stage.

## ❓ Interview Questions

**What is a missing value?**
A missing value is an empty, null, or undefined entry in a dataset where a value should exist — e.g., a blank cell, `NaN`, or `None`. It can occur due to data entry errors, non-response, or system/collection issues, and must be identified before analysis or modeling.

**Why can blindly deleting rows be risky?**
- It can **remove valid, useful information**, shrinking the dataset and reducing statistical power.
- If missing values aren't random (e.g., missing mainly for one group), deleting rows can **introduce bias** and skew results.
- On a small dataset, dropping rows can **discard a large share of the data**, hurting model accuracy.
- It's usually safer to first understand *why* the value is missing and consider imputation (mean/median/mode, forward-fill, or model-based) instead of automatically dropping rows.

## 🚀 How to Run
```bash
pip install pandas matplotlib openpyxl
python missing_value_identification.py
```
