# Real-Time UPI Fraud Detection System

A machine learning-based anomaly detection system for identifying suspicious UPI transactions. The system learns the normal fingerprint of each user's transaction behavior and flags transactions that deviate significantly from that learned pattern. It does not rely on fixed rule thresholds alone.

This project simulates realistic UPI transaction data, engineers fraud-related behavioral features, trains an unsupervised Isolation Forest model, tunes anomaly thresholds using F1-score, and deploys a real-time fraud detection dashboard with Streamlit.

## Project Highlights

- Generates 10,000 synthetic UPI-style transactions with normal and fraudulent behavior patterns.
- Engineers behavioral signals such as transaction velocity, first-time receiver flag, transaction amount deviation, hour of day, and day of week.
- Trains an unsupervised Isolation Forest model to learn normal transaction behavior.
- Tunes the anomaly threshold using F1-score to balance fraud recall and false positives.
- Produces evaluation plots including confusion matrix, precision-recall curve, threshold tuning graph, and anomaly score distribution.
- Provides a Streamlit dashboard for real-time transaction risk scoring.

## Problem Statement

UPI fraud patterns evolve quickly. Rule-based systems such as "flag all transactions above a fixed amount" are easy for attackers to bypass by splitting payments, changing transaction timing, or using new accounts.

This project solves the problem with anomaly detection. Instead of hardcoding fraud rules, the model learns what normal transactions look like and flags unusual behavior, such as:

- Large transfers compared with a user's usual transaction amount.
- Transactions to a new beneficiary.
- Late-night payments.
- High transaction velocity within a short time window.
- Unusual combinations of amount, receiver, time, and user behavior.

## Folder Structure

```text
Real-Time-UPI-Fraud-Detection-System/
|-- app/
|   `-- streamlit_app.py
|-- config/
|   `-- config.yaml
|-- data/
|   |-- raw/
|   |   `-- upi_transactions.csv
|   |-- synthetic/
|   |   `-- upi_transactions.csv
|   |-- processed/
|   |   |-- upi_transactions_with_features.csv
|   |   |-- feature_matrix.csv
|   |   |-- labels.csv
|   |   |-- anomaly_scores.csv
|   |   |-- threshold_evaluation_results.csv
|   |   `-- final_predictions.csv
|   `-- interim/
|-- models/
|   |-- isolation_forest_model.pkl
|   |-- feature_scaler.pkl
|   |-- training_metadata.pkl
|   `-- threshold_metadata.pkl
|-- notebooks/
|   |-- 1_Data_generation_simulation.ipynb
|   |-- 2_Feature_engineering.ipynb
|   |-- 3_Anomaly_detection_Model_training.ipynb
|   |-- 4_Model_evaluation_and_Thresholding_action.ipynb
|   |-- 5_Building_Streamlit_UI_and_Real_time_simulation.ipynb
|   `-- Plot_generation.ipynb
|-- reports/
|   `-- figures/
|       |-- anomaly_score_distribution.png
|       |-- confusion_matrix.png
|       |-- precision_recall_curve.png
|       |-- threshold_tuning_graph.png
|       |-- fraud_rate_by_hour.png
|       |-- amount_vs_anomaly_score.png
|       |-- feature_mean_comparison.png
|       `-- alert_outcome_breakdown.png
|-- src/
|   `-- rtufd/
|-- tests/
|-- requirements.txt
`-- README.md
```

## Dataset

The project uses synthetic UPI transaction data because real fraud datasets are sensitive and usually unavailable publicly.

Core columns:

- `transaction_id`: Unique transaction identifier.
- `timestamp`: Transaction date and time.
- `sender_account_id`: Anonymized sender account.
- `receiver_account_id`: Anonymized receiver account.
- `amount`: Transaction amount.
- `location_pincode`: Transaction origin pincode.
- `transaction_type`: P2P or merchant transaction.
- `is_fraud`: Ground-truth label used only for evaluation and threshold tuning.

The generated dataset contains:

- 9,700 normal transactions.
- 300 fraudulent transactions.
- 3 percent fraud rate.

## Engineered Features

The model uses six behavioral features:

- `hour_of_day`: Hour when the transaction occurred.
- `day_of_week`: Day of week from the timestamp.
- `transaction_value`: Transaction amount.
- `is_first_time_receiver`: Whether the sender is paying the receiver for the first time.
- `velocity_last_10min`: Sender transaction count in a recent 10-minute window.
- `amount_vs_user_avg`: Transaction amount compared with the sender's average amount.

## Modeling Approach

The model uses `IsolationForest` from scikit-learn.

Why Isolation Forest:

- It works well for anomaly detection.
- It does not require fraud labels during training.
- It isolates unusual records faster than normal records.
- It is suitable for identifying rare suspicious transactions in imbalanced data.

The training flow:

1. Load engineered feature matrix.
2. Scale features with `StandardScaler`.
3. Train `IsolationForest` with contamination set near the expected fraud rate.
4. Generate anomaly scores.
5. Tune the final alert threshold using F1-score.

## Evaluation

The project evaluates the model using metrics that matter for imbalanced fraud detection:

- Precision
- Recall
- F1-score
- Confusion matrix
- Precision-recall curve
- AUPRC

Accuracy is not the primary metric because fraud is rare. A model can get high accuracy by predicting every transaction as normal, while missing actual fraud.

## Results

From the current generated run:

- Best tuned threshold: `0.009042`
- F1-score: `0.9492`
- Precision: `0.9655`
- Recall: `0.9333`
- AUPRC: `0.9895`
- Confusion matrix: `[[9690, 10], [20, 280]]`

These values may change slightly if the synthetic data or model configuration is regenerated.

## Streamlit Dashboard

The dashboard lets a user enter transaction details and receive a real-time fraud risk decision.

Dashboard inputs include:

- Transaction amount
- User average amount
- Hour of day
- Day of week
- Receiver type
- Transactions in the last 10 minutes

The app converts these inputs into the same six model features used during training, scales them, computes an anomaly score, compares it with the tuned threshold, and displays whether the transaction is normal or suspicious.

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run the Project

Run notebooks in this order:

1. `notebooks/1_Data_generation_simulation.ipynb`
2. `notebooks/2_Feature_engineering.ipynb`
3. `notebooks/3_Anomaly_detection_Model_training.ipynb`
4. `notebooks/4_Model_evaluation_and_Thresholding_action.ipynb`
5. `notebooks/Plot_generation.ipynb`
6. `notebooks/5_Building_Streamlit_UI_and_Real_time_simulation.ipynb`

Run the Streamlit dashboard from the project root:

```bash
streamlit run app/streamlit_app.py
```

## Key Outputs

Model artifacts:

- `models/isolation_forest_model.pkl`
- `models/feature_scaler.pkl`
- `models/training_metadata.pkl`
- `models/threshold_metadata.pkl`

Processed datasets:

- `data/processed/feature_matrix.csv`
- `data/processed/labels.csv`
- `data/processed/final_predictions.csv`

Evaluation plots:

- `reports/figures/anomaly_score_distribution.png`
- `reports/figures/confusion_matrix.png`
- `reports/figures/precision_recall_curve.png`
- `reports/figures/threshold_tuning_graph.png`
- `reports/figures/fraud_rate_by_hour.png`
- `reports/figures/amount_vs_anomaly_score.png`
- `reports/figures/feature_mean_comparison.png`
- `reports/figures/alert_outcome_breakdown.png`

## Tech Stack

- Python
- Pandas
- NumPy
- scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit
- Jupyter Notebook

## Production Considerations

This project is a prototype that demonstrates the core ML logic. In a production UPI fraud system, the architecture would also include:

- Event streaming with Kafka or Kinesis.
- Real-time feature calculation with Flink or Spark Streaming.
- Low-latency feature storage with Redis, Feast, or another feature store.
- Model serving through FastAPI, BentoML, or a managed ML endpoint.
- Drift monitoring to detect stale model behavior.
- Scheduled retraining and human-reviewed fraud feedback loops.

## Project Status

Complete prototype with:

- Synthetic data generation
- Feature engineering
- Isolation Forest model training
- Threshold tuning
- Evaluation plots
- Streamlit dashboard

