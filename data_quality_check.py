import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):

    if file.endswith(".csv"):

        df = pd.read_csv(os.path.join(folder, file))

        print("\n" + "="*70)
        print(file)

        print("Rows:", len(df))
        print("Columns:", len(df.columns))

        print("Missing Values:",
              df.isnull().sum().sum())

        print("Duplicate Rows:",
              df.duplicated().sum())