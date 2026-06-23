import requests
import pandas as pd

SCHEMES = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, scheme_code in SCHEMES.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        latest_nav = data["data"][0]

        df = pd.DataFrame([latest_nav])

        output_file = f"data/raw/{fund_name}_Live_NAV.csv"

        df.to_csv(output_file, index=False)

        print(f"✅ Saved: {output_file}")

    except Exception as e:
        print(f"❌ Error fetching {fund_name}: {e}")