from __future__ import annotations

from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = PROJECT_ROOT / "models"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

MODEL_PATH = MODELS_DIR / "isolation_forest_model.pkl"
SCALER_PATH = MODELS_DIR / "feature_scaler.pkl"
THRESHOLD_METADATA_PATH = MODELS_DIR / "threshold_metadata.pkl"
FEATURE_DATA_PATH = PROCESSED_DATA_DIR / "upi_transactions_with_features.csv"

FEATURE_COLUMNS = [
    "hour_of_day",
    "day_of_week",
    "transaction_value",
    "is_first_time_receiver",
    "velocity_last_10min",
    "amount_vs_user_avg",
]

DAY_NAME_TO_NUMBER = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}


@st.cache_resource
def load_model_artifacts() -> tuple[Any, Any, dict[str, Any]]:
    """Load trained model, scaler, and threshold metadata once per app session."""
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    threshold_metadata = joblib.load(THRESHOLD_METADATA_PATH)
    return model, scaler, threshold_metadata


@st.cache_data
def load_reference_transactions() -> pd.DataFrame:
    """Load engineered transactions for dashboard context and recent-risk examples."""
    if not FEATURE_DATA_PATH.exists():
        return pd.DataFrame()
    return pd.read_csv(FEATURE_DATA_PATH, parse_dates=["timestamp"])


def build_feature_frame(
    amount: float,
    hour_of_day: int,
    day_name: str,
    receiver_type: str,
    velocity_last_10min: int,
    user_average_amount: float,
) -> pd.DataFrame:
    """Convert dashboard inputs into the model's six-feature schema."""
    safe_average = max(user_average_amount, 1.0)
    amount_vs_user_avg = amount / safe_average
    is_first_time_receiver = int(receiver_type == "New Beneficiary")

    return pd.DataFrame(
        [
            {
                "hour_of_day": hour_of_day,
                "day_of_week": DAY_NAME_TO_NUMBER[day_name],
                "transaction_value": amount,
                "is_first_time_receiver": is_first_time_receiver,
                "velocity_last_10min": velocity_last_10min,
                "amount_vs_user_avg": amount_vs_user_avg,
            }
        ],
        columns=FEATURE_COLUMNS,
    )


def score_transaction(feature_frame: pd.DataFrame, model: Any, scaler: Any, threshold: float) -> dict[str, Any]:
    """Score a single transaction and return decision metadata."""
    scaled_features = scaler.transform(feature_frame)
    decision_score = float(model.decision_function(scaled_features)[0])
    anomaly_score = -decision_score
    is_suspicious = anomaly_score >= threshold

    return {
        "decision_score": decision_score,
        "anomaly_score": anomaly_score,
        "threshold": threshold,
        "is_suspicious": is_suspicious,
    }


def render_result(score: dict[str, Any]) -> None:
    """Render the model decision in the dashboard."""
    if score["is_suspicious"]:
        st.error("High fraud risk: review or block this transaction.")
    else:
        st.success("Low fraud risk: transaction behavior looks normal.")

    metric_columns = st.columns(3)
    metric_columns[0].metric("Anomaly score", f"{score['anomaly_score']:.4f}")
    metric_columns[1].metric("Alert threshold", f"{score['threshold']:.4f}")
    metric_columns[2].metric("Decision", "Suspicious" if score["is_suspicious"] else "Normal")


def render_reference_table(reference_data: pd.DataFrame) -> None:
    """Show recent synthetic transactions for context."""
    if reference_data.empty:
        return

    display_columns = [
        "timestamp",
        "sender_account_id",
        "receiver_account_id",
        "amount",
        "transaction_type",
        "is_fraud",
        "hour_of_day",
        "velocity_last_10min",
        "amount_vs_user_avg",
    ]
    available_columns = [column for column in display_columns if column in reference_data.columns]
    st.dataframe(reference_data[available_columns].tail(25), use_container_width=True)


def main() -> None:
    """Run the Streamlit app."""
    st.set_page_config(page_title="UPI Fraud Detector", layout="wide")
    st.title("Real-Time UPI Fraud Detection")

    model, scaler, threshold_metadata = load_model_artifacts()
    reference_data = load_reference_transactions()
    threshold = float(threshold_metadata["best_threshold"])

    with st.sidebar:
        st.header("Transaction Input")
        amount = st.number_input("Transaction amount", min_value=1.0, max_value=500000.0, value=48000.0, step=500.0)
        user_average_amount = st.number_input("User average amount", min_value=1.0, max_value=250000.0, value=4000.0, step=500.0)
        hour_of_day = st.slider("Hour of day", min_value=0, max_value=23, value=2)
        day_name = st.selectbox("Day of week", list(DAY_NAME_TO_NUMBER.keys()), index=4)
        receiver_type = st.selectbox("Receiver type", ["New Beneficiary", "Known Beneficiary"])
        velocity_last_10min = st.slider("Transactions in last 10 minutes", min_value=1, max_value=25, value=4)

    feature_frame = build_feature_frame(
        amount=amount,
        hour_of_day=hour_of_day,
        day_name=day_name,
        receiver_type=receiver_type,
        velocity_last_10min=velocity_last_10min,
        user_average_amount=user_average_amount,
    )
    score = score_transaction(feature_frame, model, scaler, threshold)

    render_result(score)

    st.subheader("Model Features")
    st.dataframe(feature_frame, use_container_width=True)

    st.subheader("Tuned Threshold Metadata")
    st.json(threshold_metadata)

    st.subheader("Recent Simulated Transactions")
    render_reference_table(reference_data)


if __name__ == "__main__":
    main()
