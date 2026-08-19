from src.data_cleaning import load_data, validate_data

def test_data_quality():
    customers, contracts, installments, recoveries = load_data()
    checks = validate_data(customers, contracts, installments, recoveries)
    assert all(checks.values())
