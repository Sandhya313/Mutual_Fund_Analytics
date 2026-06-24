import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

returns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in returns:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1)
    |
    (df["expense_ratio_pct"] > 2.5)
]

print(
    "Expense Ratio Issues:",
    len(invalid_expense)
)

df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("Performance cleaned")