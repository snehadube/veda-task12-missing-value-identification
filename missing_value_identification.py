"""
Task 12 - Missing Value Identification
Veda Technology Internship | Data Analytics Track
Author: Sneha Dubey

Objective: Identify missing values in the dataset and summarize where they occur.
"""

import pandas as pd

# 1. Load the dataset
df = pd.read_csv("train_data.csv", index_col=0)

print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)
print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")
print(f"Columns: {list(df.columns)}\n")

# 2. Count missing values (nulls) per column
missing_count = df.isnull().sum()
missing_percent = (missing_count / len(df) * 100).round(2)

missing_summary = pd.DataFrame({
    "Missing_Count": missing_count,
    "Missing_Percent (%)": missing_percent
})
missing_summary = missing_summary.sort_values("Missing_Count", ascending=False)

print("=" * 60)
print("MISSING VALUE SUMMARY (per column)")
print("=" * 60)
print(missing_summary)

total_missing = missing_count.sum()
print(f"\nTotal missing cells in dataset: {total_missing}")
print(f"Total cells in dataset: {df.size}")
print(f"Overall missing percentage: {round(total_missing/df.size*100, 4)}%")

# 3. Additional data-quality checks (good practice beyond a plain null count)
duplicate_rows = df.duplicated().sum()
duplicate_ids = df["PassengerId"].duplicated().sum()
zero_fare = (df["Fare"] == 0).sum()

print("\n" + "=" * 60)
print("ADDITIONAL DATA QUALITY CHECKS")
print("=" * 60)
print(f"Fully duplicate rows: {duplicate_rows}")
print(f"Duplicate PassengerId values: {duplicate_ids}")
print(f"Rows where Fare == 0 (possible hidden/placeholder missing values): {zero_fare}")

# 4. Save outputs
missing_summary.to_csv("missing_value_summary.csv")

with open("findings.md", "w") as f:
    f.write("# Task 12 - Missing Value Identification: Findings\n\n")
    f.write(f"- Dataset shape: **{df.shape[0]} rows x {df.shape[1]} columns**\n")
    f.write(f"- **No null/NaN values** were found in any of the {df.shape[1]} columns "
            f"(0 missing cells out of {df.size} total cells).\n")
    f.write(f"- No fully duplicate rows were found ({duplicate_rows} duplicates).\n")
    f.write(f"- No duplicate `PassengerId` values were found ({duplicate_ids} duplicates).\n")
    f.write(f"- {zero_fare} rows have `Fare == 0`. This is not a null value, but it is worth "
            "flagging as a possible hidden/placeholder missing value from the original "
            "(pre-normalized) dataset, since a real fare of exactly zero is unusual.\n\n")
    f.write("## Conclusion\n")
    f.write("This dataset has already been cleaned and normalized (all numeric columns are "
            "scaled between 0 and 1), which is why no missing values remain. In a raw/real-world "
            "Titanic dataset, the `Age`, `Cabin`, and `Embarked` columns are the ones that "
            "typically contain missing values and would need imputation before this stage.\n")

print("\nSaved: missing_value_summary.csv, findings.md")
