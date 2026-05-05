from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from utils.features import compute_features

app = FastAPI()

# load artifacts
model = joblib.load("model/fraud_model.pkl")
threshold = joblib.load("model/threshold.pkl")
amount_mean = joblib.load("model/amount_mean.pkl")
amount_std = joblib.load("model/amount_std.pkl")

class Transaction(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Time: float
    Amount: float

@app.post("/predict")
def predict(data: Transaction):

    features = compute_features(data, amount_mean, amount_std)
    features = np.array(features).reshape(1, -1)

    prob = model.predict_proba(features)[0][1]
    prediction = int(prob >= threshold)

    return {
        "fraud_probability": float(prob),
        "prediction": prediction
    }