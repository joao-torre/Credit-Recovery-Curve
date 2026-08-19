from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"

def load_data():
    customers = pd.read_csv(RAW / "customers.csv")
    contracts = pd.read_csv(RAW / "contracts.csv", parse_dates=["origination_date"])
    installments = pd.read_csv(
        RAW / "installments.csv",
        parse_dates=["due_date", "payment_date"]
    )
    recoveries = pd.read_csv(RAW / "recoveries.csv", parse_dates=["recovery_date"])
    return customers, contracts, installments, recoveries

def validate_data(customers, contracts, installments, recoveries):
    checks = {
        "customers_unique": customers["customer_id"].is_unique,
        "contracts_unique": contracts["contract_id"].is_unique,
        "installments_unique": installments["installment_id"].is_unique,
        "recoveries_unique": recoveries["recovery_id"].is_unique,
        "negative_recovery_amount": (recoveries["recovery_amount"] < 0).sum() == 0,
        "negative_installment_value": (installments["installment_value"] < 0).sum() == 0,
        "valid_status": installments["status"].isin(["PAID", "LATE", "DEFAULT"]).all(),
    }
    return checks
