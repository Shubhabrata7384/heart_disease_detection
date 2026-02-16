import streamlit as st
import pandas as pd
import joblib

model = joblib.load("logistic Regression_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")
st.title("Heart Stroke Prediction by Shubhabrata")
#st.markdown("### Provide the following details")

age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("Sex", ["M", "F"])
chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVM"])
max_hr = st.slider("Max Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

if st.button("Predict"):
    raw_input = {
        "Age": age,
        f"Sex_{sex}": 1,
        f"ChestPainType_{chest_pain}": 1,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        f"RestingECG_{resting_ecg}": 1,
        "MaxHR": max_hr,
        f"ExerciseAngina_{exercise_angina}": 1,
        "Oldpeak": oldpeak,
        f"ST_Slope_{st_slope}": 1
    }

    df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in df.columns:
            df[col] = 0

    df = df[expected_columns]
    scaled = scaler.transform(df)
    prediction = model.predict(scaled)[0]

    if prediction == 1:
        st.error("⚠️ High risk of heart stroke. Please consult a doctor.")
    else:
        st.success("✅ Low risk of heart stroke.")
