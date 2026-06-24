import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.upper()
)

df = df[df["amount_inr"] > 0]

print(
    "KYC Values:",
    df["kyc_status"].unique()
)

df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("Transactions cleaned")