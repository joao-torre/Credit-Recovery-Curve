import numpy as np
import pandas as pd

def build_default_base(contracts, installments):
    """One observation per contract that experienced a measurable default.

    Exposure at default is approximated by the remaining scheduled
    installment balance from the first default installment through maturity.
    """
    defaults = installments[installments["status"].eq("DEFAULT")].copy()
    first_default = (
        defaults.sort_values(["contract_id", "due_date"])
        .groupby("contract_id", as_index=False)
        .first()[["contract_id", "due_date", "installment_number"]]
        .rename(columns={
            "due_date": "default_date",
            "installment_number": "default_installment_number"
        })
    )
    base = first_default.merge(
        contracts[[
            "contract_id", "customer_id", "product", "contract_value",
            "installment_value", "term_months"
        ]],
        on="contract_id",
        how="left"
    )
    base["exposure_at_default"] = (
        base["installment_value"]
        * (base["term_months"] - base["default_installment_number"] + 1)
    )
    return base

def prepare_recovery_events(default_base, recoveries):
    events = recoveries.merge(
        default_base[["contract_id", "default_date"]],
        on="contract_id",
        how="inner"
    )
    events["days_after_default"] = (
        events["recovery_date"] - events["default_date"]
    ).dt.days
    events = events[events["days_after_default"] >= 0].copy()
    return events

def recovery_curve(default_base, events, horizons=(0, 30, 60, 90, 120, 180, 360)):
    """Cumulative recovery rate at each horizon."""
    total_exposure = default_base["exposure_at_default"].sum()
    if total_exposure == 0:
        return pd.DataFrame({"days_after_default": horizons, "recovery_rate": np.nan})

    out = []
    for h in horizons:
        amount = events.loc[
            events["days_after_default"].le(h), "recovery_amount"
        ].sum()
        out.append({
            "days_after_default": h,
            "recovered_amount": amount,
            "recovery_rate": amount / total_exposure
        })
    return pd.DataFrame(out)

def recovery_at_days(default_base, events, days=180):
    total_exposure = default_base["exposure_at_default"].sum()
    recovered = events.loc[events["days_after_default"].le(days), "recovery_amount"].sum()
    return recovered / total_exposure if total_exposure else np.nan

def time_to_recovery(default_base, events, target=0.50):
    curve = recovery_curve(default_base, events, horizons=range(0, 366))
    reached = curve[curve["recovery_rate"].ge(target)]
    return int(reached.iloc[0]["days_after_default"]) if not reached.empty else np.nan
