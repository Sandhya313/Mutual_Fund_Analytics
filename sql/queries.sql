SELECT
scheme_name,
aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;


SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM nav_history
GROUP BY month
ORDER BY month;


SELECT
state,
COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;


SELECT
scheme_name,
expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;


SELECT
AVG(amount_inr) AS avg_amount
FROM investor_transactions;


SELECT
fund_house,
SUM(aum_crore) AS total_aum
FROM scheme_performance
GROUP BY fund_house
ORDER BY total_aum DESC;


SELECT
scheme_name,
return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


SELECT
risk_grade,
COUNT(*) AS total_funds
FROM scheme_performance
GROUP BY risk_grade;


SELECT
strftime('%Y-%m', transaction_date) AS month,
SUM(amount_inr) AS transaction_volume
FROM investor_transactions
GROUP BY month;


SELECT
category,
AVG(alpha) AS avg_alpha
FROM scheme_performance
GROUP BY category;
