import pandas as pd
from .recovery_metrics import recovery_curve

def add_risk_band(base, customers):
    return base.merge(
        customers[["customer_id", "risk_score", "risk_band", "region", "income"]],
        on="customer_id",
        how="left"
    )

def cohort_curves(base, events, cohort_freq="Q"):
    base = base.copy()
    base["cohort"] = base["default_date"].dt.to_period(cohort_freq).astype(str)
    events = events.merge(base[["contract_id", "cohort"]], on="contract_id", how="inner")

    rows = []
    for cohort, cohort_base in base.groupby("cohort"):
        cohort_events = events[events["cohort"].eq(cohort)]
        curve = recovery_curve(cohort_base, cohort_events)
        curve["cohort"] = cohort
        rows.append(curve)
    return pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()
