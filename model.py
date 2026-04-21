import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# STEP 1 — Load dataset
df = pd.read_csv("data.csv")

print("Initial Data:")
print(df.head())

# STEP 2 — Clean data
df = df.replace(-200, np.nan)
df = df.dropna()

print("After Cleaning:", df.shape)

# STEP 3 — Select columns
df = df[
    [
        "CO_GT", "NO2_GT", "Nox_GT", "C6H6_GT",
        "PT08_S1_CO", "PT08_S2_NMHC", "PT08_S3_Nox",
        "PT08_S4_NO2", "PT08_S5_O3",
        "T", "RH", "AH"
    ]
]

# STEP 4 — Feature Engineering
df["Gas_Index"] = (
    df["CO_GT"] +
    df["NO2_GT"] +
    df["Nox_GT"] +
    df["C6H6_GT"]
) / 4

df = df.rename(columns={
    "PT08_S1_CO": "PM2.5",
    "T": "Temperature",
    "RH": "Humidity"
})

# STEP 5 — Create AQI Category
q1 = df["PM2.5"].quantile(0.33)
q2 = df["PM2.5"].quantile(0.66)

def categorize(pm25):
    if pm25 <= q1:
        return "Good"
    elif pm25 <= q2:
        return "Moderate"
    else:
        return "Poor"

df["AQI_Category"] = df["PM2.5"].apply(categorize)

print(df["AQI_Category"].value_counts())

# STEP 6 — Features & Labels
X = df[["Gas_Index", "Temperature", "Humidity"]]
y = df["AQI_Category"]

# STEP 7 — Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# STEP 8 — Train Model
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=6,
    random_state=42
)

model.fit(X_train, y_train)

# STEP 9 — Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# STEP 10 — Test Prediction
sample = [[200, 30, 60]]
prediction = model.predict(sample)

print("Sample Prediction:", prediction[0])

# STEP 11 — Save Model
joblib.dump(model, "aqi_model.pkl")

print("Model saved as aqi_model.pkl")





