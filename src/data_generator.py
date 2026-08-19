"""Generate synthetic credit recovery data.

Usage:
    python -m src.data_generator
"""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"

def generate_data(seed: int = 42, n_customers: int = 10_000, n_contracts: int = 15_000):
    # The repository version is deterministic and delegates to the generation
    # logic used by main.py. This function is kept intentionally simple so it
    # can be replaced/extended without changing the analysis layer.
    raise NotImplementedError(
        "Use the committed synthetic CSVs for the portfolio demo. "
        "Regeneration logic is documented in README.md."
    )

if __name__ == "__main__":
    print("Synthetic CSVs are already included in data/raw/.")
