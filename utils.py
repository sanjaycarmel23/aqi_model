import pandas as pd
import numpy as np

def generate_sensor_data(gas, temp, hum):
    data = pd.DataFrame({
        "Gas": np.random.normal(gas, 20, 30),
        "Temperature": np.random.normal(temp, 2, 30),
        "Humidity": np.random.normal(hum, 5, 30)
    })
    return data


def analyze_data(data):
    summary = {
        "avg_gas": round(data["Gas"].mean(), 2),
        "avg_temp": round(data["Temperature"].mean(), 2),
        "avg_hum": round(data["Humidity"].mean(), 2)
    }
    return summary