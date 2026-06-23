import requests
import pandas as pd

scheme_code = 125497

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

data = response.json()

latest_nav = data["data"][0]

df = pd.DataFrame([latest_nav])

df.to_csv(
    "data/raw/HDFC_Top100_Live_NAV.csv",
    index=False
)

print("NAV saved successfully")