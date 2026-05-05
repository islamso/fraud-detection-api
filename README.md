## 💳 Credit Card Fraud Detection API

A machine learning project that detects fraudulent credit card transactions using multiple classification models.  
The best-performing model is deployed as a **FastAPI REST API** for real-time detections.

---

## 🚀 Project Overview

This project aims to detect fraudulent transactions using supervised machine learning techniques.  
It includes data preprocessing, feature engineering, model training, evaluation, and deployment as an API.

The final system exposes a REST API that returns:
- Fraud probability
- Final prediction (0 = legitimate, 1 = fraud)

---

## 🧠 Problem Statement

Credit card fraud is a major issue in financial systems.  
The goal is to accurately identify fraudulent transactions while minimizing false positives.

---

## ⚙️ Tech Stack

- Python 🐍
- Pandas & NumPy
- Scikit-learn
- XGBoost
- CatBoost
- FastAPI
- Joblib

---

## 📊 Machine Learning Models

The following models were trained and evaluated:

- Random Forest
- XGBoost
- CatBoost (Best Model)

The final model was selected based on:
- F1-score
- ROC-AUC
- Precision/Recall balance

---

## 🧪 Feature Engineering

Key transformations applied:

- ⏰ Time-based features (Hour extraction)
- 🔁 Cyclical encoding (sin/cos for time)
- 📉 Log transformation of transaction amount
- 📊 Z-score normalization
- ⚠️ Binary feature for small transactions

---

## 🏆 Final Model

The best-performing model is:

👉 **CatBoost Classifier**

It was tuned using hyperparameter optimization and handles class imbalance effectively.

---

## 🌐 API Usage

The model is deployed using FastAPI.


## 📥 Input Example

json
```
{
  "V1": -1.3,
  "V2": 0.2,
  "V3": 1.1,
  "V4": -0.5,
  "V5": 0.3,
  "V6": -0.2,
  "V7": 0.8,
  "V8": -0.1,
  "V9": 0.4,
  "V10": -0.6,
  "V11": 0.2,
  "V12": -1.2,
  "V13": 0.5,
  "V14": -0.7,
  "V15": 0.3,
  "V16": -0.4,
  "V17": 0.9,
  "V18": -0.2,
  "V19": 0.1,
  "V20": 0.05,
  "V21": -0.03,
  "V22": 0.02,
  "V23": -0.01,
  "V24": 0.01,
  "V25": -0.02,
  "V26": 0.03,
  "V27": -0.01,
  "V28": 0.02,
  "Time": 100000,
  "Amount": 150.0
}
```

## 📥 output example
```
{
  "fraud_probability": 0.0023,
  "prediction": 0
}
```

## Project Structure

```
fraud_project/
│
├── app.py                  # FastAPI backend
│
├── model/                 # Trained ML models (.pkl)
│   ├── fraud_model.pkl
│   ├── threshold.pkl
│   ├── amount_mean.pkl
│   ├── amount_std.pkl
│
├── utils/                 # Feature engineering logic
│   ├── features.py
│
├── notebooks/             # Training notebook
│   ├── Credit_card.ipynb
│
├── README.md
```


## ▶️ How to Run Locally

pip install -r requirements.txt
uvicorn app:app --reload

then open : http://127.0.0.1:8000/docs


## Author

Built by Islam soussi, an aspiring Data scientist and AI Engineer  



