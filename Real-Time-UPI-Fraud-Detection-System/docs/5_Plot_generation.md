# Plot Generation Module

## Real-Time-UPI-Fraud-Detection-System

### Module Overview

The Plot Generation Module is responsible for creating visualizations that help analyze transaction behavior, anomaly detection performance, fraud patterns, model outputs, and threshold optimization results.

Visual analytics play a critical role in fraud detection systems because anomaly detection models generate complex outputs that are difficult to interpret through raw numerical metrics alone. This module transforms transaction data, anomaly scores, fraud predictions, and evaluation metrics into intuitive charts and dashboards for exploratory analysis, model validation, stakeholder reporting, and Streamlit deployment.

The generated plots provide transparency into how the system identifies potentially fraudulent UPI transactions and help validate the effectiveness of the Isolation Forest model.

---

# Business Problem

Fraud detection models generate outputs such as:

* Anomaly scores
* Fraud predictions
* Precision values
* Recall values
* F1 scores
* Threshold optimization results

However, these metrics alone do not clearly explain:

```text
Which transactions appear abnormal?

How are frauds distributed?

How effective is the selected threshold?

How does the model separate frauds from normal transactions?
```

Visualization bridges the gap between technical model outputs and business understanding.

---

# Module Objectives

The Plot Generation Module is designed to:

1. Visualize transaction behavior.
2. Analyze fraud distributions.
3. Explore engineered features.
4. Display anomaly score patterns.
5. Evaluate model performance.
6. Visualize threshold optimization results.
7. Support model explainability.
8. Generate reporting artifacts.

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
Plot Generation
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
│
├── notebooks/
│   ├── 1_Data_generation_simulation.ipynb
│   ├── 2_Feature_engineering.ipynb
│   ├── 3_Anomaly_detection_Model_training.ipynb
│   ├── 4_Model_evaluation_and_Thresholding_action.ipynb
│   └── 5_Plot_generation.ipynb
│
├── reports/
│   ├── figures/
│   ├── plots/
│   └── model_visualizations/
│
├── docs/
│   └── Plot_Generation_README.md
│
└── README.md
```

---

# Module Inputs

The notebook consumes outputs from previous modules.

### Input Files

```text
data/raw/synthetic_upi_transactions.csv
```

```text
data/processed/engineered_transactions.csv
```

```text
data/predictions/anomaly_scores.csv
```

```text
data/predictions/final_fraud_predictions.csv
```

```text
models/threshold_config.json
```

---

# Plot Generation Workflow

```text
Load Transaction Data
          │
          ▼
Load Engineered Features
          │
          ▼
Load Anomaly Scores
          │
          ▼
Generate Exploratory Plots
          │
          ▼
Generate Evaluation Plots
          │
          ▼
Generate Fraud Analysis Plots
          │
          ▼
Save Visual Reports
```

---

# Transaction Analysis Plots

These plots help understand transaction behavior.

## Transaction Amount Distribution

Purpose:

```text
Visualize spending patterns
across users
```

Insights:

* Normal transaction ranges
* Outliers
* High-value transactions

Output:

```text
transaction_amount_distribution.png
```

---

## Transaction Frequency Distribution

Purpose:

```text
Analyze transaction volume
per user
```

Insights:

* Active users
* Low-activity users
* Suspicious transaction bursts

Output:

```text
transaction_frequency_distribution.png
```

---

# Time-Based Analysis Plots

## Transactions by Hour

Purpose:

```text
Identify peak transaction hours
```

Insights:

* User activity patterns
* Night-time anomalies
* High-risk transaction periods

Output:

```text
transactions_by_hour.png
```

---

## Transactions by Day of Week

Purpose:

```text
Analyze weekly transaction patterns
```

Insights:

* Weekend spending behavior
* Workday activity trends

Output:

```text
transactions_by_day.png
```

---

# Feature Engineering Visualization

These plots validate engineered behavioral features.

## Amount Ratio Distribution

Purpose:

```text
Measure spending deviations
from normal behavior
```

Insights:

* Unusual spending spikes
* Fraud concentration zones

Output:

```text
amount_ratio_distribution.png
```

---

## Transaction Velocity Distribution

Purpose:

```text
Analyze rapid transaction activity
```

Insights:

* Velocity anomalies
* Potential fraud bursts

Output:

```text
transaction_velocity_distribution.png
```

---

## Merchant Frequency Analysis

Purpose:

```text
Analyze merchant interaction behavior
```

Insights:

* Frequent merchants
* New merchant activity
* Merchant concentration

Output:

```text
merchant_frequency_analysis.png
```

---

# Fraud Visualization

## Fraud vs Normal Transactions

Purpose:

```text
Compare fraud and normal transaction counts
```

Insights:

* Fraud prevalence
* Class imbalance

Output:

```text
fraud_vs_normal_distribution.png
```

---

## Fraud Transaction Amounts

Purpose:

```text
Compare spending behavior
between fraud and normal users
```

Insights:

* Fraud spending spikes
* Abnormal payment values

Output:

```text
fraud_amount_analysis.png
```

---

# Isolation Forest Visualization

## Anomaly Score Distribution

Purpose:

```text
Visualize anomaly score spread
```

Insights:

* Normal score range
* Suspicious score range
* Threshold separation

Output:

```text
anomaly_score_distribution.png
```

---

## Anomaly Score Histogram

Purpose:

```text
Understand score density
```

Insights:

* Fraud concentration
* Decision boundary quality

Output:

```text
anomaly_score_histogram.png
```

---

# Threshold Optimization Visualization

## Threshold vs F1 Score

Purpose:

```text
Find the best threshold
for fraud classification
```

Insights:

* Optimal decision boundary
* F1 score stability

Output:

```text
threshold_vs_f1_score.png
```

---

## Threshold vs Precision

Purpose:

```text
Measure precision changes
across thresholds
```

Output:

```text
threshold_vs_precision.png
```

---

## Threshold vs Recall

Purpose:

```text
Measure recall changes
across thresholds
```

Output:

```text
threshold_vs_recall.png
```

---

# Model Evaluation Visualizations

## Confusion Matrix

Purpose:

```text
Evaluate prediction quality
```

Visual Components:

| Actual | Predicted |
| ------ | --------- |
| Normal | Normal    |
| Normal | Fraud     |
| Fraud  | Normal    |
| Fraud  | Fraud     |

Output:

```text
confusion_matrix.png
```

---

## ROC Curve

Purpose:

```text
Measure ranking performance
```

Insights:

* True Positive Rate
* False Positive Rate
* ROC-AUC

Output:

```text
roc_curve.png
```

---

## Precision-Recall Curve

Purpose:

```text
Evaluate fraud detection performance
under class imbalance
```

Output:

```text
precision_recall_curve.png
```

---

# Feature Importance Visualization

Although Isolation Forest does not provide traditional feature importance, proxy methods can be visualized.

Examples:

* SHAP values
* Permutation importance
* Feature contribution scores

Output:

```text
feature_importance_analysis.png
```

---

# Streamlit Dashboard Integration

The generated plots are used within the Streamlit dashboard.

Dashboard Sections:

```text
Overview Dashboard

Fraud Analytics Dashboard

Transaction Monitoring Dashboard

Model Performance Dashboard

Threshold Analysis Dashboard
```

Plots are loaded dynamically for real-time monitoring.

---

# Generated Outputs

## Visualization Files

```text
reports/figures/
```

Example Outputs:

```text
transaction_amount_distribution.png

transactions_by_hour.png

fraud_vs_normal_distribution.png

anomaly_score_distribution.png

threshold_vs_f1_score.png

confusion_matrix.png

roc_curve.png

precision_recall_curve.png
```

---

# Business Benefits

### Improved Explainability

Makes anomaly detection easier to understand.

### Better Decision Making

Supports fraud analyst investigations.

### Model Validation

Verifies model effectiveness visually.

### Stakeholder Reporting

Provides management-friendly insights.

### Dashboard Readiness

Supports Streamlit deployment.

---

# Future Enhancements

Potential improvements include:

* Interactive Plotly dashboards
* Real-time streaming visualizations
* Geospatial fraud maps
* User behavior timelines
* Network fraud graphs
* SHAP-based explainability plots
* Live anomaly monitoring

---

# Module Deliverables

### Inputs

```text
synthetic_upi_transactions.csv

engineered_transactions.csv

anomaly_scores.csv

final_fraud_predictions.csv
```

### Outputs

```text
reports/figures/

reports/plots/

reports/model_visualizations/
```

### Generated Artifacts

* Distribution plots
* Fraud analysis charts
* Threshold optimization graphs
* ROC curves
* Precision-Recall curves
* Confusion matrices
* Dashboard-ready visualizations

---

# Conclusion

The Plot Generation Module provides the visual intelligence layer of the Real-Time-UPI-Fraud-Detection-System. It transforms transaction data, anomaly scores, fraud predictions, and evaluation metrics into meaningful visual insights. These visualizations improve model transparency, support fraud investigations, validate anomaly detection performance, and provide the graphical foundation for the real-time Streamlit fraud monitoring dashboard.
