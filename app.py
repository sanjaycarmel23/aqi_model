import streamlit as st
from predictor import predict_aqi
from utils import generate_sensor_data, analyze_data

st.set_page_config(page_title="AQaaS Dashboard", layout="wide")

st.title("🌫️ AQaaS - Interactive Dashboard")

# -------------------------
# INPUT SECTION
# -------------------------
st.sidebar.header("Sensor Inputs")

gas = st.sidebar.slider("Gas Index", 0.0, 500.0, 200.0)
temp = st.sidebar.slider("Temperature (°C)", 0.0, 50.0, 30.0)
hum = st.sidebar.slider("Humidity (%)", 0.0, 100.0, 60.0)

# -------------------------
# PREDICTION
# -------------------------
prediction = predict_aqi(gas, temp, hum)

st.subheader("Predicted AQI")

col1, col2 = st.columns(2)

with col1:
    if prediction == "Good":
        st.success("Good 🟢")
    elif prediction == "Moderate":
        st.warning("Moderate 🟡")
    else:
        st.error("Poor 🔴")

# -------------------------
# DATA GENERATION
# -------------------------
data = generate_sensor_data(gas, temp, hum)

# -------------------------
# GRAPHS
# -------------------------
with col2:
    st.write("### Sensor Trends")
    st.line_chart(data)

st.write("### Average Values")
st.bar_chart(data.mean())

# -------------------------
# ANALYSIS
# -------------------------
st.subheader("Analysis")

summary = analyze_data(data)

st.write(f"Average Gas: {summary['avg_gas']}")
st.write(f"Average Temperature: {summary['avg_temp']}")
st.write(f"Average Humidity: {summary['avg_hum']}")

# -------------------------
# INSIGHTS
# -------------------------
st.subheader("Insights")

if prediction == "Poor":
    st.write("⚠️ Air quality is unhealthy. Action recommended.")
elif prediction == "Moderate":
    st.write("🙂 Air quality is moderate. Monitor closely.")
else:
    st.write("✅ Air quality is good.")

