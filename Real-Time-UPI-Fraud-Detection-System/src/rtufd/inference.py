from __future__ import annotations

import pandas as pd
from sklearn.pipeline import Pipeline


def predict_fraud_risk(
    model: Pipeline,
    features: pd.DataFrame,
    threshold: float,
) -> pd.DataFrame:
    """Score transactions and flag likely fraud cases."""
    scored = features.copy()
    scored["anomaly_score"] = model.decision_function(features)
    scored["is_suspicious"] = (scored["anomaly_score"] <= threshold).astype(int)
    return scored
