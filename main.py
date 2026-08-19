from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

from src.data_cleaning import load_data, validate_data
from src.recovery_metrics import build_default_base, prepare_recovery_events, recovery_curve, time_to_recovery
from src.cohort_analysis import add_risk_band, cohort_curves
from src.analysis import segment_recovery, vintage_matrix

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
PROCESSED = ROOT / "data" / "processed"
OUT.mkdir(exist_ok=True)
PROCESSED.mkdir(exist_ok=True)

def main():
    customers, contracts, installments, recoveries = load_data()

    checks = validate_data(customers, contracts, installments, recoveries)
    assert all(checks.values()), checks

    base = build_default_base(contracts, installments)
    base = add_risk_band(base, customers)
    events = prepare_recovery_events(base, recoveries)

    curve = recovery_curve(base, events)
    product = segment_recovery(base, events, "product", days=180)
    risk = segment_recovery(base, events, "risk_band", days=180)
    cohorts = cohort_curves(base, events)
    vintage = vintage_matrix(base, events)

    analysis = curve.copy()
    analysis["metric"] = "Recovery Rate"
    analysis.to_csv(PROCESSED / "recovery_analysis.csv", index=False)
    product.to_csv(PROCESSED / "recovery_by_product.csv", index=False)
    risk.to_csv(PROCESSED / "recovery_by_risk.csv", index=False)
    cohorts.to_csv(PROCESSED / "cohort_analysis.csv", index=False)
    vintage.to_csv(PROCESSED / "vintage_matrix.csv", index=False)

    # Recovery curve
    plt.figure(figsize=(10, 6))
    plt.plot(curve["days_after_default"], curve["recovery_rate"] * 100, marker="o")
    plt.xlabel("Days after default")
    plt.ylabel("Cumulative Recovery Rate (%)")
    plt.title("Credit Recovery Curve")
    plt.grid(alpha=.25)
    plt.tight_layout()
    plt.savefig(OUT / "recovery_curve.png", dpi=160)
    plt.close()

    # Product
    plt.figure(figsize=(9, 5))
    plt.bar(product["product"], product["recovery_rate"] * 100)
    plt.ylabel("Recovery Rate @ 180d (%)")
    plt.title("Recovery by Product — 180 Days")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(OUT / "recovery_by_product.png", dpi=160)
    plt.close()

    # Risk
    plt.figure(figsize=(7, 5))
    risk_order = ["LOW", "MEDIUM", "HIGH"]
    risk_plot = risk.set_index("risk_band").reindex(risk_order).reset_index()
    plt.bar(risk_plot["risk_band"], risk_plot["recovery_rate"] * 100)
    plt.ylabel("Recovery Rate @ 180d (%)")
    plt.title("Recovery by Risk — 180 Days")
    plt.tight_layout()
    plt.savefig(OUT / "recovery_by_risk.png", dpi=160)
    plt.close()

    # Cohorts
    plt.figure(figsize=(10, 6))
    for cohort, g in cohorts.groupby("cohort"):
        plt.plot(g["days_after_default"], g["recovery_rate"] * 100, marker="o", label=cohort)
    plt.xlabel("Days after default")
    plt.ylabel("Cumulative Recovery Rate (%)")
    plt.title("Recovery Curve by Default Cohort")
    plt.legend(title="Cohort", fontsize=8)
    plt.grid(alpha=.25)
    plt.tight_layout()
    plt.savefig(OUT / "cohort_analysis.png", dpi=160)
    plt.close()

    total_exposure = base["exposure_at_default"].sum()
    total_recovered = events["recovery_amount"].sum()
    overall_rate = total_recovered / total_exposure if total_exposure else 0
    t50 = time_to_recovery(base, events, target=.50)

    print("\n=== CREDIT RECOVERY CURVE ===")
    print(f"Contracts in default base : {len(base):,}")
    print(f"Exposure at default       : R$ {total_exposure:,.2f}")
    print(f"Total recovered           : R$ {total_recovered:,.2f}")
    print(f"Overall recovery rate     : {overall_rate:.2%}")
    print(f"Recovery rate @ 180d      : {curve.loc[curve.days_after_default.eq(180), 'recovery_rate'].iloc[0]:.2%}")
    print(f"Time to 50% recovery      : {t50} days")

if __name__ == "__main__":
    main()
