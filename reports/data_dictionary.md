# Data Dictionary

## 01_fund_master.csv

| Column             | Data Type | Business Definition            |
| ------------------ | --------- | ------------------------------ |
| amfi_code          | Integer   | Unique AMFI scheme identifier  |
| fund_house         | Text      | Asset Management Company (AMC) |
| scheme_name        | Text      | Mutual fund scheme name        |
| category           | Text      | Broad fund category            |
| sub_category       | Text      | Detailed scheme category       |
| plan               | Text      | Direct or Regular plan         |
| launch_date        | Date      | Scheme launch date             |
| benchmark          | Text      | Benchmark index                |
| expense_ratio_pct  | Float     | Annual expense ratio (%)       |
| exit_load_pct      | Float     | Exit load percentage           |
| min_sip_amount     | Float     | Minimum SIP amount             |
| min_lumpsum_amount | Float     | Minimum lump sum investment    |
| fund_manager       | Text      | Fund manager name              |
| risk_category      | Text      | Risk classification            |
| sebi_category_code | Text      | SEBI category identifier       |

## 02_nav_history.csv

| Column    | Data Type | Business Definition    |
| --------- | --------- | ---------------------- |
| amfi_code | Integer   | Mutual fund identifier |
| date      | Date      | NAV date               |
| nav       | Float     | Net Asset Value        |

## 07_scheme_performance.csv

| Column            | Data Type | Business Definition              |
| ----------------- | --------- | -------------------------------- |
| return_1yr_pct    | Float     | 1-year return (%)                |
| return_3yr_pct    | Float     | 3-year return (%)                |
| return_5yr_pct    | Float     | 5-year return (%)                |
| alpha             | Float     | Alpha measure                    |
| beta              | Float     | Beta measure                     |
| sharpe_ratio      | Float     | Risk-adjusted return metric      |
| expense_ratio_pct | Float     | Annual expense ratio (%)         |
| aum_crore         | Float     | Assets Under Management (Crores) |
| risk_grade        | Text      | Scheme risk grade                |

## 08_investor_transactions.csv

| Column             | Data Type | Business Definition           |
| ------------------ | --------- | ----------------------------- |
| investor_id        | Integer   | Unique investor identifier    |
| transaction_date   | Date      | Transaction date              |
| amfi_code          | Integer   | Scheme identifier             |
| transaction_type   | Text      | SIP / Lumpsum / Redemption    |
| amount_inr         | Float     | Transaction amount            |
| state              | Text      | Investor state                |
| city               | Text      | Investor city                 |
| city_tier          | Text      | Tier 1 / Tier 2 / Tier 3 city |
| age_group          | Text      | Investor age group            |
| gender             | Text      | Investor gender               |
| annual_income_lakh | Float     | Annual income in lakhs        |
| payment_mode       | Text      | UPI / Net Banking / etc.      |
| kyc_status         | Text      | KYC verification status       |

## Source

All datasets were provided as part of the Bluestock Mutual Fund Analytics internship dataset.
