# Data Generation & Simulation Module

## Real-Time-UPI-Fraud-Detection-System

### Module Overview

The Data Generation & Simulation Module is the foundation of the Real-Time-UPI-Fraud-Detection-System. Since real banking and UPI transaction data is highly sensitive and restricted due to privacy and regulatory requirements, this module generates realistic synthetic transaction data that mimics genuine user behavior.

The generated dataset is used to train, validate, and test machine learning models for fraud detection without exposing any real customer information.

This module creates:

* Synthetic UPI users
* Merchant profiles
* Realistic transaction patterns
* User behavioral characteristics
* Fraud-like anomalies
* Historical transaction records

The output dataset serves as the input for the Feature Engineering and Anomaly Detection pipelines.

---

# Business Problem

UPI transactions occur continuously across multiple users, devices, merchants, and locations. Fraudulent activities often differ from a user's normal spending behavior.

Traditional fraud detection systems rely on predefined rules such as:

* Transaction amount > ₹50,000
* More than 10 transactions per minute
* Transactions from unusual locations

These rule-based approaches struggle to adapt to evolving fraud patterns.

The objective of this project is to build an anomaly detection system that learns the normal transaction fingerprint of each user and flags unusual activities automatically.

To achieve this, a large volume of realistic transaction data is required.

---

# Module Objectives

The Data Generation Module is designed to:

1. Simulate realistic UPI transactions.
2. Create diverse customer spending patterns.
3. Generate merchant interaction history.
4. Produce historical transaction records.
5. Simulate suspicious transaction behavior.
6. Create datasets for anomaly detection model training.
7. Support reproducible machine learning experiments.

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
│   ├── processed/
│   │
│   └── external/
│
├── notebooks/
│   └── 1_Data_generation_simulation.ipynb
│
├── docs/
│   └── Data_Generation_README.md
│
├── src/
│   └── data_generation/
│
└── README.md
```

---

# Data Generation Workflow

The notebook follows the workflow below:

```text
Create Users
      │
      ▼
Create Merchants
      │
      ▼
Generate Transactions
      │
      ▼
Simulate User Behaviour
      │
      ▼
Inject Fraud Scenarios
      │
      ▼
Export Dataset
```

---

# Synthetic User Generation

Each user is assigned unique behavioral attributes.

### User Attributes

| Attribute                  | Description                         |
| -------------------------- | ----------------------------------- |
| user_id                    | Unique user identifier              |
| age_group                  | Customer age category               |
| location                   | User city or region                 |
| average_transaction_amount | Typical spending amount             |
| transaction_frequency      | Transactions per day                |
| preferred_transaction_time | Most active period                  |
| preferred_merchants        | Frequently used merchant categories |
| account_age_days           | Age of account                      |

Example:

```text
User ID: U1001

Average Amount: ₹750
Transactions Per Day: 6
Preferred Time: Evening
Location: Bengaluru
```

---

# Merchant Generation

Merchant profiles are created to simulate real UPI ecosystems.

### Merchant Categories

* Grocery
* Food Delivery
* Retail
* Fuel Station
* Pharmacy
* Utilities
* Entertainment
* Travel
* Shopping
* Education

Each merchant is assigned:

* Merchant ID
* Merchant Category
* Location
* Risk Profile

---

# Transaction Simulation

Transactions are generated using realistic behavioral rules.

### Simulated Transaction Attributes

| Feature          | Description                   |
| ---------------- | ----------------------------- |
| transaction_id   | Unique transaction identifier |
| timestamp        | Transaction timestamp         |
| user_id          | User identifier               |
| merchant_id      | Merchant identifier           |
| amount           | Transaction value             |
| transaction_type | P2P or P2M                    |
| device_type      | Android / iOS                 |
| location         | Transaction location          |
| payment_mode     | UPI payment method            |

---

# Behavioral Pattern Simulation

The system creates realistic transaction patterns.

Examples include:

### Spending Pattern

```text
Salary Day:
Higher spending

Weekdays:
Moderate spending

Weekends:
Increased entertainment spending
```

### Time-Based Pattern

```text
Morning:
Utility payments

Afternoon:
Shopping

Evening:
Food and travel payments
```

### Merchant Preference Pattern

Users repeatedly interact with familiar merchants.

---

# Fraud Scenario Simulation

To support anomaly detection training, the system injects suspicious transaction patterns.

## 1. High-Value Transactions

A user suddenly performs a transaction significantly larger than their normal spending range.

Example:

```text
Normal Amount: ₹800

Fraud Amount: ₹45,000
```

---

## 2. Unusual Transaction Timing

Transactions occur at times rarely used by the customer.

Example:

```text
Normal Activity:
08:00 AM – 10:00 PM

Suspicious Activity:
02:30 AM
```

---

## 3. Location Anomaly

Transactions originate from unfamiliar locations.

Example:

```text
Normal Location:
Bengaluru

Suspicious Location:
Delhi
```

---

## 4. Rapid Successive Transactions

Multiple transactions occur within a short period.

Example:

```text
15 Transactions
Within 3 Minutes
```

---

## 5. New Merchant Interaction

Payments are made to merchants with no previous interaction history.

---

## 6. Device Change

A transaction originates from a new or unknown device.

---

# Dataset Output

The notebook generates:

```text
synthetic_upi_transactions.csv
```

Output Location:

```text
data/raw/
```

---

# Data Quality Validation

The module performs validation checks to ensure dataset reliability.

### Validation Checks

* Missing value detection
* Duplicate transaction detection
* Invalid timestamps
* Invalid transaction amounts
* User consistency verification
* Merchant consistency verification

---

# Sample Dataset Schema

| Column Name      | Data Type |
| ---------------- | --------- |
| transaction_id   | String    |
| user_id          | String    |
| merchant_id      | String    |
| timestamp        | Datetime  |
| amount           | Float     |
| location         | String    |
| device_type      | String    |
| transaction_type | String    |

---

# Expected Output Volume

The notebook can generate:

| Metric          | Typical Size   |
| --------------- | -------------- |
| Users           | 1,000+         |
| Merchants       | 500+           |
| Transactions    | 100,000+       |
| Fraud Scenarios | Multiple Types |

---

# Integration with Feature Engineering

The generated dataset is consumed by the Feature Engineering module to create fraud-detection features such as:

* Transaction velocity
* Average spending deviation
* Merchant novelty score
* Device novelty score
* Location deviation score
* Time-of-day anomaly score

These features are later used by the Isolation Forest model.

---

# Benefits of Synthetic Data

### Privacy Protection

No real customer data is used.

### Regulatory Compliance

Avoids exposure of sensitive financial information.

### Scalability

Millions of transactions can be generated on demand.

### Controlled Fraud Injection

Specific fraud scenarios can be simulated and analyzed.

### Reproducibility

Experiments can be repeated consistently.

---

# Future Enhancements

Potential improvements include:

* Seasonal transaction behavior
* Festival spending simulation
* User lifecycle modeling
* Device fingerprint generation
* Graph-based fraud simulation
* Real-time Kafka transaction streams
* Synthetic identity fraud generation

---

# Conclusion

The Data Generation & Simulation Module provides a scalable and privacy-preserving mechanism for creating realistic UPI transaction datasets. By modeling genuine customer behavior and injecting fraud-like anomalies, it enables the development and evaluation of machine learning-based fraud detection systems. The generated data serves as the foundation for feature engineering, anomaly detection model training, threshold optimization, and real-time fraud monitoring through the Streamlit dashboard.
