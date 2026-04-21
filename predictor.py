import joblib
import numpy as np

# Load model once
model = joblib.load("aqi_model.pkl")

def predict_aqi(gas, temp, hum):
    input_data = np.array([[gas, temp, hum]])
    prediction = model.predict(input_data)[0]
    return prediction