import pandas as pd
import os

data_folder = "data/raw"

csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

print(f"\nFound {len(csv_files)} CSV files\n")

for file in csv_files:
    print("=" * 80)
    print("FILE:", file)

    path = os.path.join(data_folder, file)

    try:
        df = pd.read_csv(path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

    except Exception as e:
        print("Error:", e)