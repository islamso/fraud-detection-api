## fraud-detection-api
## 💳 Credit Card Fraud Detection API

A machine learning project that detects fraudulent credit card transactions using multiple classification models.  
The best-performing model is deployed as a **FastAPI REST API** for real-time predictions.

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




