from __future__ import annotations

import numpy as np
import pandas as pd


def generate_synthetic_upi_transactions(
    rows: int = 10000,
    fraud_rate: float = 0.03,
    random_state: int = 42,
) -> pd.DataFrame:
    """Generate PDF-aligned synthetic UPI transactions with sparse fraud labels."""
    rng = np.random.default_rng(random_state)
    start_time = pd.Timestamp("2024-08-01 00:00:00")
    timestamps = start_time + pd.to_timedelta(rng.integers(0, 30 * 24 * 60, size=rows), unit="m")
    sender_ids = rng.integers(1000, 1800, size=rows)
    receiver_ids = rng.integers(2000, 3200, size=rows)
    is_fraud = rng.random(rows) < fraud_rate

    amounts = rng.lognormal(mean=5.4, sigma=0.8, size=rows)
    amounts[is_fraud] *= rng.uniform(4.0, 12.0, size=is_fraud.sum())
    amounts = amounts.round(2)

    timestamps = pd.Series(timestamps)
    timestamps.loc[is_fraud] = timestamps.loc[is_fraud].dt.normalize() + pd.to_timedelta(
        rng.choice([1, 2, 3, 4], size=is_fraud.sum()), unit="h"
    )
    receiver_ids[is_fraud] = rng.integers(9000, 9999, size=is_fraud.sum())

    return pd.DataFrame(
        {
            "transaction_id": [f"TXN_202408_{i:05d}" for i in range(rows)],
            "timestamp": timestamps,
            "sender_account_id": [f"ACC_{account_id}" for account_id in sender_ids],
            "receiver_account_id": [f"ACC_{account_id}" for account_id in receiver_ids],
            "amount": amounts,
            "location_pincode": rng.choice(["400001", "560001", "110001", "700001", "600001"], size=rows),
            "transaction_type": rng.choice(["P2P", "Merchant"], size=rows, p=[0.72, 0.28]),
            "is_fraud": is_fraud.astype(int),
        }
    )
