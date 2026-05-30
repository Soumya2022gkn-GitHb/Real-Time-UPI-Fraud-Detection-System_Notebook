# Model Evaluation and Thresholding Action Module

## Real-Time-UPI-Fraud-Detection-System

### Module Overview

The Model Evaluation and Thresholding Action Module evaluates the performance of the trained anomaly detection model and determines the optimal threshold for fraud classification.

The Isolation Forest model produces anomaly scores rather than direct fraud probabilities. These anomaly scores indicate how unusual a transaction is relative to learned normal user behavior.

A critical challenge in anomaly detection is deciding the anomaly score threshold that separates normal transactions from potentially fraudulent transactions. This module systematically evaluates model performance across multiple thresholds and selects the threshold that maximizes the F1 Score, ensuring a balanced trade-off between fraud detection and false alarms.

The selected threshold becomes the operational decision boundary used during real-time fraud detection.

---

# Business Problem

The Isolation Forest model generates anomaly scores such as:

| Transaction | Anomaly Score |
| ----------- | ------------- |
| Normal      | 0.42          |
| Normal      | 0.18          |
| Suspicious  | -0.08         |
| Fraudulent  | -0.41         |

However, the model does not automatically determine:

```text
Which score should be considered fraud?
```

If the threshold is too strict:

```text
Many frauds are missed
(Low Recall)
```

If the threshold is too lenient:

```text
Many legitimate transactions
are incorrectly flagged
(Low Precision)
```

Therefore, threshold optimization is essential for production deployment.

---

# Module Objectives

The Model Evaluation and Thresholding Module is designed to:

1. Evaluate anomaly detection performance.
2. Generate anomaly score distributions.
3. Compare multiple threshold values.
4. Calculate fraud detection metrics.
5. Optimize threshold selection.
6. Maximize F1 Score.
7. Reduce false positives.
8. Create deployment-ready decision boundaries.

---

# Position in Project Pipeline

```text
Data Generation
       │
       ▼
Feature Engineering
       │
       ▼
Isolation Forest Training
       │
       ▼
Model Evaluation &
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
│   ├── processed/
│   └── predictions/
│       ├── anomaly_scores.csv
│       └── anomaly_predictions.csv
│
├── notebooks/
│   ├── 1_Data_generation_simulation.ipynb
│   ├── 2_Feature_engineering.ipynb
│   ├── 3_Anomaly_detection_Model_training.ipynb
│   └── 4_Model_evaluation_and_Thresholding_action.ipynb
│
├── docs/
│   └── Model_Evaluation_and_Thresholding_Action_README.md
│
├── models/
│   ├── isolation_forest.pkl
│   ├── scaler.pkl
│   └── threshold_config.json
│
└── README.md
```

---

# Module Inputs

The notebook consumes:

```text
models/isolation_forest.pkl
```

```text
data/processed/engineered_transactions.csv
```

```text
Synthetic Fraud Labels
```

Generated from:

```text
3_Anomaly_detection_Model_training.ipynb
```

---

# Why Threshold Optimization?

Isolation Forest outputs anomaly scores:

```text
Higher Score
    ↓
More Normal

Lower Score
    ↓
More Anomalous
```

The challenge is determining the cutoff point that best separates:

```text
Normal Transactions

and

Fraudulent Transactions
```

Threshold optimization converts anomaly scores into actionable fraud decisions.

---

# Evaluation Workflow

```text
Engineered Dataset
        │
        ▼
Load Trained Model
        │
        ▼
Generate Anomaly Scores
        │
        ▼
Evaluate Thresholds
        │
        ▼
Calculate Metrics
        │
        ▼
Find Best F1 Score
        │
        ▼
Select Optimal Threshold
        │
        ▼
Save Threshold Configuration
```

---

# Anomaly Score Analysis

The model generates anomaly scores for every transaction.

Example:

| Transaction ID | Score |
| -------------- | ----- |
| TXN10001       | 0.42  |
| TXN10002       | 0.19  |
| TXN10003       | -0.05 |
| TXN10004       | -0.37 |

Interpretation:

| Score Range   | Meaning           |
| ------------- | ----------------- |
| High Positive | Normal            |
| Near Zero     | Borderline        |
| Negative      | Suspicious        |
| Very Negative | Highly Suspicious |

---

# Evaluation Metrics

The module evaluates model performance using fraud labels available in the synthetic dataset.

### Precision

Measures:

```text
Of all flagged transactions,
how many were actually fraud?
```

Formula:

Precision=\frac{TP}{TP+FP}

---

### Recall

Measures:

```text
Of all fraud transactions,
how many were detected?
```

Formula:

Recall=\frac{TP}{TP+FN}

---

### F1 Score

Measures the balance between precision and recall.

Formula:

F1=2\times\frac{Precision\times Recall}{Precision+Recall}

The optimal threshold is selected using the highest F1 Score.

---

# Threshold Search Process

The notebook evaluates multiple candidate thresholds.

Example:

| Threshold | Precision | Recall | F1 Score |
| --------- | --------- | ------ | -------- |
| -0.50     | 0.92      | 0.42   | 0.58     |
| -0.40     | 0.88      | 0.61   | 0.72     |
| -0.30     | 0.83      | 0.75   | 0.79     |
| -0.20     | 0.72      | 0.86   | 0.78     |

Result:

```text
Best Threshold = -0.30

Highest F1 Score = 0.79
```

---

# Confusion Matrix Analysis

The module generates a confusion matrix.

|               | Predicted Normal | Predicted Fraud |
| ------------- | ---------------- | --------------- |
| Actual Normal | TN               | FP              |
| Actual Fraud  | FN               | TP              |

Where:

* TP = True Positive
* FP = False Positive
* TN = True Negative
* FN = False Negative

This helps analyze model behavior and business impact.

---

# ROC Curve Evaluation

The notebook may generate:

### ROC Curve

Measures:

```text
True Positive Rate
vs
False Positive Rate
```

### ROC-AUC

Interpretation:

| ROC-AUC | Performance |
| ------- | ----------- |
| 0.50    | Random      |
| 0.70+   | Good        |
| 0.80+   | Strong      |
| 0.90+   | Excellent   |

---

# Precision-Recall Curve

For fraud detection, Precision-Recall curves are often more informative than ROC curves because fraud transactions are rare.

The module evaluates:

* Precision
* Recall
* F1 Score
* Threshold Stability

---

# Fraud Decision Logic

After threshold selection:

```text
If Score >= Threshold
      ↓
Normal Transaction

If Score < Threshold
      ↓
Fraud Alert
```

Example:

```text
Threshold = -0.30

Score = -0.45

Prediction = Fraud
```

---

# Threshold Configuration Storage

The selected threshold is saved for deployment.

Example:

```json
{
  "optimal_threshold": -0.30,
  "best_f1_score": 0.79
}
```

Output:

```text
models/threshold_config.json
```

---

# Outputs Generated

### Threshold Configuration

```text
models/threshold_config.json
```

### Evaluation Report

```text
reports/model_evaluation_report.pdf
```

### Threshold Metrics

```text
reports/threshold_metrics.csv
```

### Fraud Predictions

```text
data/predictions/final_fraud_predictions.csv
```

---

# Sample Prediction Output

| Transaction ID | Score | Threshold | Prediction |
| -------------- | ----- | --------- | ---------- |
| TXN10001       | 0.34  | -0.30     | Normal     |
| TXN10002       | -0.41 | -0.30     | Fraud      |

---

# Integration with Real-Time Prediction

The optimized threshold is passed to:

```text
5_Real_Time_Prediction.ipynb
```

During inference:

```text
Incoming Transaction
        │
        ▼
Generate Features
        │
        ▼
Isolation Forest Score
        │
        ▼
Apply Optimized Threshold
        │
        ▼
Fraud Decision
```

---

# Business Benefits

### Improved Fraud Detection

Captures more fraudulent transactions.

### Reduced False Positives

Minimizes unnecessary customer disruptions.

### Better Customer Experience

Fewer legitimate transactions are blocked.

### Operational Efficiency

Fraud analysts focus on high-risk alerts.

### Production Readiness

Provides a stable fraud decision boundary.

---

# Future Enhancements

Potential improvements include:

* Dynamic threshold adaptation
* User-specific thresholds
* Merchant-specific thresholds
* Risk-based thresholding
* Cost-sensitive optimization
* Real-time threshold recalibration
* Ensemble anomaly score calibration

---

# Module Deliverables

### Inputs

```text
engineered_transactions.csv

isolation_forest.pkl
```

### Outputs

```text
threshold_config.json

final_fraud_predictions.csv

threshold_metrics.csv

model_evaluation_report.pdf
```

### Generated Artifacts

* Precision metrics
* Recall metrics
* F1 metrics
* Confusion matrix
* ROC-AUC results
* Optimal threshold
* Final fraud predictions

---

# Conclusion

The Model Evaluation and Thresholding Action Module transforms raw anomaly scores into actionable fraud decisions. By systematically evaluating multiple thresholds and selecting the threshold that maximizes the F1 Score, the module establishes a robust decision boundary for production deployment. This optimization ensures an effective balance between fraud detection accuracy and false-positive control, enabling reliable real-time fraud monitoring within the Real-Time-UPI-Fraud-Detection-System.
