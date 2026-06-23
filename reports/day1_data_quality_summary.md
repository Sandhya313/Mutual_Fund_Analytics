# Data Quality Summary

## Overview

A data quality assessment was performed on all datasets loaded during the data ingestion phase. The objective was to verify dataset completeness, consistency, and integrity before further analysis.

## Datasets Assessed

1. 01_fund_master.csv
2. 02_nav_history.csv
3. 03_aum_by_fund_house.csv
4. 04_monthly_sip_inflows.csv
5. 05_category_inflows.csv
6. 06_industry_folio_count.csv
7. 07_scheme_performance.csv
8. 08_investor_transactions.csv
9. 09_portfolio_holdings.csv
10. 10_benchmark_indices.csv
11. HDFC_Top100_Live_NAV.csv

## Missing Value Analysis

Most datasets contained no missing values.

One exception was identified:

* 04_monthly_sip_inflows.csv: 12 missing values

Further investigation is required to determine whether these missing values should be imputed, removed, or retained based on business requirements.

## Duplicate Record Analysis

Duplicate record checks were performed on all datasets.

Result:

* No duplicate records were found in any dataset.

## AMFI Code Validation

AMFI scheme codes were validated between:

* 01_fund_master.csv
* 02_nav_history.csv

Results:

* Total AMFI Codes in Fund Master: 40
* Total AMFI Codes in NAV History: 40
* Missing Codes: 0

All AMFI codes present in the fund master dataset were successfully found in NAV history.

## Data Consistency Checks

* Dataset schemas were successfully loaded and inspected.
* Column data types were verified using Pandas.
* Sample records were reviewed using the head() function.
* Live NAV data was successfully fetched from MFAPI and stored in the raw data folder.

## Conclusion

The datasets are generally clean and suitable for further analysis. No duplicate records were identified, and AMFI code integrity was successfully validated. The only notable issue is the presence of 12 missing values in the monthly SIP inflows dataset, which will be addressed during the data cleaning phase.
