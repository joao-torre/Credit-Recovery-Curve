import pandas as pd
from .recovery_metrics import recovery_curve, recovery_at_days

def segment_recovery(base, events, column, days=180):
    rows = []
    for segment, segment_base in base.groupby(column):
        contract_ids = set(segment_base["contract_id"])
        segment_events = events[events["contract_id"].isin(contract_ids)]
        rate = recovery_at_days(segment_base, segment_events, days=days)
        rows.append({column: segment, "days": days, "recovery_rate": rate})
    return pd.DataFrame(rows).sort_values("recovery_rate", ascending=False)

def vintage_matrix(base, events, horizons=(30,60,90,120,180)):
    base = base.copy()
    base["vintage"] = base["default_date"].dt.to_period("M").astype(str)
    rows = []
    for vintage, vbase in base.groupby("vintage"):
        vevents = events[events["contract_id"].isin(vbase["contract_id"])]
        row = {"vintage": vintage}
        age_days = (pd.Timestamp("2026-08-19") - vbase["default_date"]).dt.days.max()
        for h in horizons:
            if age_days < h:
                row[f"{h}d"] = None
            else:
                row[f"{h}d"] = recovery_at_days(vbase, vevents, h)
        rows.append(row)
    return pd.DataFrame(rows)
