import pandas as pd
from src.recovery_metrics import recovery_curve, recovery_at_days

def test_recovery_curve():
    base = pd.DataFrame({
        "contract_id": ["C1", "C2"],
        "exposure_at_default": [1000.0, 1000.0]
    })
    events = pd.DataFrame({
        "contract_id": ["C1", "C2"],
        "days_after_default": [30, 60],
        "recovery_amount": [200.0, 400.0]
    })
    curve = recovery_curve(base, events, horizons=(0,30,60))
    assert curve.loc[curve.days_after_default.eq(0), "recovery_rate"].iloc[0] == 0
    assert curve.loc[curve.days_after_default.eq(30), "recovery_rate"].iloc[0] == 0.10
    assert curve.loc[curve.days_after_default.eq(60), "recovery_rate"].iloc[0] == 0.30

def test_recovery_at_days():
    base = pd.DataFrame({"contract_id": ["C1"], "exposure_at_default": [1000.0]})
    events = pd.DataFrame({
        "contract_id": ["C1"], "days_after_default": [30], "recovery_amount": [500.0]
    })
    assert recovery_at_days(base, events, 30) == 0.5
