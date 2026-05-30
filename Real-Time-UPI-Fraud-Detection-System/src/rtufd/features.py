from __future__ import annotations

import pandas as pd


FEATURE_COLUMNS = [
    "hour_of_day",
    "day_of_week",
    "transaction_value",
    "is_first_time_receiver",
    "velocity_last_10min",
    "amount_vs_user_avg",
]


def build_behavioral_features(transactions: pd.DataFrame) -> pd.DataFrame:
    """Create the six behavioral features highlighted in the project guide."""
    features = transactions.copy()
    features["timestamp"] = pd.to_datetime(features["timestamp"])
    features = features.sort_values(["sender_account_id", "timestamp"]).reset_index(drop=True)

    features["hour_of_day"] = features["timestamp"].dt.hour
    features["day_of_week"] = features["timestamp"].dt.dayofweek
    features["transaction_value"] = features["amount"]
    features["is_first_time_receiver"] = (~features.duplicated(["sender_account_id", "receiver_account_id"])).astype(int)
    features["velocity_last_10min"] = calculate_velocity(features)

    user_average = features.groupby("sender_account_id")["amount"].transform("mean")
    features["amount_vs_user_avg"] = features["amount"] / user_average.clip(lower=1)
    return features


def calculate_velocity(transactions: pd.DataFrame) -> pd.Series:
    """Count each sender's transactions in a rolling 10-minute window."""
    velocity = pd.Series(index=transactions.index, dtype=float)

    for _, group in transactions.groupby("sender_account_id"):
        ordered = group.sort_values("timestamp").set_index("timestamp")
        counts = ordered["transaction_id"].rolling("10min").count()
        velocity.loc[group.sort_values("timestamp").index] = counts.to_numpy()

    return velocity.fillna(1)
