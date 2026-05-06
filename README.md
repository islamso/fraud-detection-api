## 💳 Credit Card Fraud Detection System (End-to-End AI Project)

This project is a machine learning-based fraud detection system that identifies fraudulent credit card transactions using anonymized financial data. It is deployed as a real-time REST API for live inference.


---
## 🚀 Project Overview

This project aims to detect fraudulent transactions using supervised machine learning techniques.  
It includes data preprocessing, feature engineering, model training, evaluation, and deployment as an API.

The final system exposes a REST API that returns:
- Fraud probability
- Final prediction (0 = legitimate, 1 = fraud)

---

## 🧠 Problem Statement

Credit card fraud is a major issue in modern financial systems, causing significant financial losses for banks and customers.
It also affects trust and reliability in digital payment systems. So Detecting fraudulent transactions in real time is therefore a critical requirement 
The goal is to accurately identify fraudulent transactions while minimizing false positives.

---

## ⚙️ Solution Overview

This system follows an end-to-end machine learning pipeline:

- Data preprocessing and cleaning  
- Exploratory Data Analysis (EDA)  
- Feature engineering  
- Model training and evaluation  
- Hyperparameter tuning  
- Threshold optimization  
- Deployment as a REST API

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

The model is deployed using FastAPI for serving real-time detections.
It can be run locally for testing or accessed online through a cloud deployment on Render.


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
├── requirements.txt        # Dependencies for deployment
│
├── README.md
```


## ▶️ How to Run Locally

pip install -r requirements.txt
uvicorn app:app --reload

then open : http://127.0.0.1:8000/docs

## 🌍 How to Run Online

The project is deployed using Render.

Once deployed, the API is accessible via:

https://fraud-detection-api-7tf0.onrender.com/docs

You can:

Open the link in a browser
Use the /predict endpoint via Swagger UI
Send transaction data (V1–V28, Time, Amount)
Receive real-time fraud detection results


## Author

Built by Islam soussi, an aspiring Data scientist and AI Engineer  



