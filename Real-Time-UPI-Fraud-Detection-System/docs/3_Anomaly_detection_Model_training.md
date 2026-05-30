# Anomaly Detection Model Training Module

## Real-Time-UPI-Fraud-Detection-System

### Module Overview

The Anomaly Detection Model Training Module is responsible for training the machine learning model that identifies potentially fraudulent UPI transactions.

Unlike traditional fraud detection systems that rely on manually defined business rules, this project uses an unsupervised learning approach. The model learns the normal behavioral fingerprint of users from historical transaction patterns and identifies transactions that deviate significantly from those learned patterns.

This module trains an Isolation Forest model using engineered behavioral features generated from the Feature Engineering Module and produces anomaly scores that indicate the likelihood of fraud.

---

# Business Problem

Fraudulent UPI transactions constantly evolve, making static rule-based systems difficult to maintain.

Examples of limitations of rule-based systems:

* Fraudsters adapt to predefined rules.
* New fraud patterns remain undetected.
* Rules generate excessive false positives.
* Manual maintenance becomes expensive.

Instead of defining fraud manually, the Isolation Forest algorithm learns normal transaction behavior and detects anomalies automatically.

The objective of this module is to train a model capable of identifying suspicious transactions based on deviations from normal user activity.

---

# Module Objectives

The Model Training Module is designed to:

1. Load engineered transaction features.
2. Prepare data for anomaly detection.
3. Train an Isolation Forest model.
4. Learn normal user behavior patterns.
5. Generate anomaly scores.
6. Evaluate model performance.
7. Save trained artifacts for deployment.
8. Support real-time fraud detection.

---

# Position in Project Pipeline

```text
Data Generation
       │
       ▼
Feature Engineering
       │
       ▼
Anomaly Detection Model Training
       │
       ▼
Threshold Optimization
       │
       ▼
Real-Time Prediction
       │
       ▼
Streamlit Dashboard
```

---

# Folder Structure

```text
Real-Time-UPI-Fraud-Detection-System/
│
├── data/
│   ├── raw/
│   │   └── synthetic_upi_transactions.csv
│   │
│   └── processed/
│       └── engineered_transactions.csv
│
├── notebooks/
│   ├── 1_Data_generation_simulation.ipynb
│   ├── 2_Feature_engineering.ipynb
│   └── 3_Anomaly_detection_Model_training.ipynb
│
├── docs/
│   ├── Data_Generation_README.md
│   ├── Feature_Engineering_README.md
│   └── Anomaly_Detection_Model_Training_README.md
│
├── src/
│   ├── features/
│   └── models/
│       ├── train_model.py
│       └── evaluate_model.py
│
├── models/
│   ├── isolation_forest.pkl
│   └── scaler.pkl
│
└── README.md
```

---

# Module Input

The training notebook consumes:

```text
data/processed/engineered_transactions.csv
```

Generated from:

```text
2_Feature_engineering.ipynb
```

---

# Why Isolation Forest?

Isolation Forest is a popular unsupervised anomaly detection algorithm.

It is particularly suitable because:

* Fraud cases are rare.
* Fraud labels are often unavailable.
* It scales efficiently to large datasets.
* It isolates anomalous observations quickly.
* It works well with behavioral features.

Unlike classification algorithms, Isolation Forest does not require balanced fraud labels for training.

---

# Isolation Forest Concept

The algorithm works by recursively partitioning data points.

Normal transactions:

```text
Require many splits
to isolate
```

Anomalous transactions:

```text
Require very few splits
to isolate
```

Therefore:

```text
Shorter Path Length
        =
Higher Anomaly Score
```

Transactions that are isolated quickly are considered suspicious.

---

# Training Workflow

```text
Engineered Dataset
        │
        ▼
Feature Selection
        │
        ▼
Scaling
        │
        ▼
Isolation Forest Training
        │
        ▼
Anomaly Score Generation
        │
        ▼
Performance Evaluation
        │
        ▼
Model Serialization
```

---

# Feature Selection

The module selects fraud-related behavioral features.

Typical features include:

| Feature                      |
| ---------------------------- |
| amount_ratio                 |
| amount_zscore                |
| transaction_gap_minutes      |
| transactions_last_hour       |
| transactions_last_day        |
| merchant_frequency           |
| new_merchant_flag            |
| location_match_flag          |
| device_change_flag           |
| night_transaction_flag       |
| behavioral_consistency_score |

These features collectively represent a user's transaction fingerprint.

---

# Feature Scaling

Before training, numerical features are scaled.

### Common Scaling Methods

* StandardScaler
* RobustScaler

Benefits:

* Improves feature consistency.
* Prevents dominant feature influence.
* Stabilizes anomaly score generation.

Output Artifact:

```text
models/scaler.pkl
```

---

# Model Training

The notebook trains an Isolation Forest model.

### Typical Parameters

| Parameter     | Description                 |
| ------------- | --------------------------- |
| n_estimators  | Number of isolation trees   |
| contamination | Expected anomaly proportion |
| max_samples   | Samples per tree            |
| random_state  | Reproducibility seed        |

Example:

```python
IsolationForest(
    n_estimators=200,
    contamination=0.05,
    random_state=42
)
```

---

# Learning User Behavior

The model learns:

### Spending Behavior

* Typical transaction amounts
* Average daily spend
* Spending deviations

### Transaction Timing

* Active hours
* Weekend behavior
* Night activity

### Merchant Preferences

* Frequently used merchants
* Category preferences

### Location Patterns

* Common transaction locations
* Travel behavior

### Device Usage

* Known devices
* Device switching behavior

These characteristics collectively form a behavioral fingerprint for each user.

---

# Anomaly Score Generation

After training, each transaction receives an anomaly score.

Example:

| Transaction      | Score |
| ---------------- | ----- |
| Normal           | 0.82  |
| Suspicious       | -0.12 |
| Highly Anomalous | -0.55 |

Lower scores indicate higher anomaly likelihood.

---

# Fraud Prediction Logic

The model predicts:

```text
1  → Normal Transaction

-1 → Anomalous Transaction
```

These predictions are later refined through threshold optimization.

---

# Model Evaluation

The notebook evaluates model performance using available fraud labels from the synthetic dataset.

### Evaluation Metrics

| Metric           | Purpose                         |
| ---------------- | ------------------------------- |
| Precision        | Fraud detection accuracy        |
| Recall           | Fraud capture rate              |
| F1 Score         | Balance of precision and recall |
| Confusion Matrix | Classification summary          |
| ROC-AUC          | Ranking performance             |

---

# Expected Outputs

### Trained Model

```text
models/isolation_forest.pkl
```

### Feature Scaler

```text
models/scaler.pkl
```

### Anomaly Predictions

```text
data/predictions/anomaly_predictions.csv
```

### Anomaly Scores

```text
data/predictions/anomaly_scores.csv
```

---

# Sample Prediction Output

| transaction_id | anomaly_score | prediction |
| -------------- | ------------- | ---------- |
| TXN10001       | 0.41          | Normal     |
| TXN10002       | -0.33         | Fraud      |

---

# Model Artifact Management

Generated artifacts:

```text
models/
│
├── isolation_forest.pkl
├── scaler.pkl
└── model_metadata.json
```

These artifacts are used during deployment and real-time inference.

---

# Integration with Threshold Optimization

The Isolation Forest generates anomaly scores but does not determine the optimal fraud classification threshold.

Therefore, the next module:

```text
4_Threshold_Optimization.ipynb
```

uses anomaly scores and known fraud labels to identify the threshold that maximizes the F1 Score.

---

# Benefits of Isolation Forest

### Unsupervised Learning

No large labeled fraud dataset required.

### Scalable

Efficient for large transaction volumes.

### Robust

Handles high-dimensional behavioral features.

### Adaptable

Learns evolving transaction patterns.

### Production Friendly

Fast inference for real-time fraud detection.

---

# Future Enhancements

Potential improvements include:

* Extended Isolation Forest
* One-Class SVM
* Autoencoder-based anomaly detection
* Deep learning anomaly detection
* Ensemble anomaly detection
* Graph neural network fraud detection
* Real-time streaming model training

---

# Module Deliverables

### Input

```text
data/processed/engineered_transactions.csv
```

### Outputs

```text
models/isolation_forest.pkl

models/scaler.pkl

data/predictions/anomaly_scores.csv

data/predictions/anomaly_predictions.csv
```

### Generated Artifacts

* Trained Isolation Forest model
* Feature scaler
* Anomaly scores
* Fraud predictions
* Model metadata

---

# Conclusion

The Anomaly Detection Model Training Module serves as the core intelligence engine of the Real-Time-UPI-Fraud-Detection-System. By leveraging Isolation Forest, the system learns normal user transaction behavior and identifies unusual activities without relying on hardcoded fraud rules. The trained model generates anomaly scores that form the basis for threshold optimization, real-time fraud prediction, and interactive fraud monitoring through the Streamlit dashboard.
