from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import f1_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def train_isolation_forest(
    features: pd.DataFrame,
    contamination: float = 0.04,
    n_estimators: int = 300,
    random_state: int = 42,
) -> Pipeline:
    """Train an Isolation Forest pipeline on behavioral features."""
    return Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "model",
                IsolationForest(
                    contamination=contamination,
                    n_estimators=n_estimators,
                    random_state=random_state,
                ),
            ),
        ]
    ).fit(features)


def tune_threshold(scores: np.ndarray, labels: pd.Series, candidates: int = 100) -> tuple[float, float]:
    """Select the anomaly-score threshold with the best F1-score."""
    best_threshold = float(scores.min())
    best_f1 = 0.0

    for threshold in np.linspace(scores.min(), scores.max(), candidates):
        predictions = (scores <= threshold).astype(int)
        score = f1_score(labels, predictions)
        if score > best_f1:
            best_threshold = float(threshold)
            best_f1 = float(score)

    return best_threshold, best_f1
