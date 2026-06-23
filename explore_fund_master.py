import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("Total Schemes:")
print(len(df))

print("\nUnique Fund Houses:")
print(df["fund_house"].nunique())

print("\nFund Houses:")
print(df["fund_house"].unique())

print("\nCategories:")
print(df["category"].unique())

print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nRisk Categories:")
print(df["risk_category"].unique())

print("\nPlans:")
print(df["plan"].unique())