# Credit Recovery Curve

Analytics project focused on **credit recovery performance over time**, using synthetic data to analyze recovery curves, products, risk profiles, cohorts and vintages.

> All data in this repository is synthetic and generated for portfolio/learning purposes. It does not represent real customer, contract or company information.

## Objective

Answer business questions such as:

- How does cumulative recovery evolve after default?
- Which products recover more at 180 days?
- How does risk affect recovery?
- Which default cohorts perform better?
- How many days does the portfolio take to reach 50% recovery?
- Are newer vintages improving or deteriorating?

## Project architecture

```text
Credit-Recovery-Curve/
├── README.md
├── requirements.txt
├── .gitignore
├── main.py
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── contracts.csv
│   │   ├── installments.csv
│   │   └── recoveries.csv
│   └── processed/
├── src/
│   ├── data_generator.py
│   ├── data_cleaning.py
│   ├── recovery_metrics.py
│   ├── cohort_analysis.py
│   └── analysis.py
├── notebooks/
│   └── exploratory_analysis.ipynb
├── outputs/
└── tests/
```

## Synthetic dataset

The initial portfolio contains approximately:

- 10,000 customers
- 15,000 contracts
- 150,000 installments
- Recovery events generated with different behaviors by risk and product

Products:

- Personal Loan
- Vehicle Finance
- Credit Card
- Payroll Loan

Risk bands:

- LOW
- MEDIUM
- HIGH

## Main metric

### Recovery Rate

**Recovery Rate = Recovered Amount / Exposure at Default**

The central analysis is the cumulative recovery curve:

| Horizon | Metric |
|---:|---|
| 0 days | Recovery Rate |
| 30 days | Recovery Rate @ 30d |
| 60 days | Recovery Rate @ 60d |
| 90 days | Recovery Rate @ 90d |
| 120 days | Recovery Rate @ 120d |
| 180 days | Recovery Rate @ 180d |
| 360 days | Recovery Rate @ 360d |

## Important analytical decision

A vintage/cohort that has not yet reached a given horizon is **not treated as zero**.

For example, if a March cohort has only 100 days of observed history, its 180-day recovery rate is shown as missing/not mature.

This avoids artificially penalizing recent cohorts.

## Run locally

Python 3.11+ is recommended.

```bash
git clone <your-repository-url>
cd Credit-Recovery-Curve

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
python main.py
```

Run tests:

```bash
pytest -q
```

## Outputs

Running `main.py` produces:

- `outputs/recovery_curve.png`
- `outputs/recovery_by_product.png`
- `outputs/recovery_by_risk.png`
- `outputs/cohort_analysis.png`

And processed datasets:

- `data/processed/recovery_analysis.csv`
- `data/processed/recovery_by_product.csv`
- `data/processed/recovery_by_risk.csv`
- `data/processed/cohort_analysis.csv`
- `data/processed/vintage_matrix.csv`

## Methodology

1. Identify the first measurable default for each contract.
2. Establish the exposure base.
3. Link recovery events to the default date.
4. Calculate elapsed days after default.
5. Calculate cumulative recovery at standard horizons.
6. Segment by product and risk.
7. Compare default cohorts and monthly vintages.
8. Validate data quality before analysis.

## Limitations

This is a synthetic portfolio analytics project. It does not model:

- Actual collection strategy costs
- Discounted cash flow / NPV
- Legal recovery
- Operational collection capacity
- Macroeconomic scenarios
- Cure probability models
- Machine learning

Machine learning is intentionally outside the scope of this project so the portfolio focuses on **Business Analytics + Credit + SQL/Python + temporal/cohort analysis**.

## Roadmap

- [x] Synthetic customer/contract/installment/recovery data
- [x] Data quality validation
- [x] Recovery curve
- [x] Product segmentation
- [x] Risk segmentation
- [x] Cohort analysis
- [x] Vintage matrix
- [x] Automated outputs
- [ ] SQLite/DuckDB layer
- [ ] SQL analytical queries
- [ ] Power BI dashboard
- [ ] Optional AWS/S3/Athena architecture

## Portfolio positioning

This project is designed to demonstrate analytical thinking in a financial context rather than simply programming.

**Core skills:** Python, Pandas, SQL-ready data modeling, credit analytics, recovery curves, cohort analysis, vintage analysis and business interpretation.
