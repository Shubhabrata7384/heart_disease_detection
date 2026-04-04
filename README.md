# ❤️ Heart Stroke Prediction App (Streamlit)

A Machine Learning web application that predicts the risk of heart stroke based on patient health data. This project is built using **Logistic Regression** and deployed using **Streamlit** for an interactive user interface.

---

## 🚀 Features

* 🧠 Predicts heart stroke risk using ML model
* 🎯 Accurate classification using Logistic Regression
* ⚡ Interactive UI with Streamlit
* 📊 Real-time prediction results
* 🔄 Automatic data preprocessing (encoding + scaling)

---

## 🛠️ Tech Stack

### 👨‍💻 Frontend & Backend

* Streamlit

### 🤖 Machine Learning

* Scikit-learn
* Logistic Regression
* StandardScaler

### 📦 Libraries

* Pandas
* Joblib

---

## 📁 Project Structure

```
heart_prediction_streamlit/
│
├── app.py
├── logistic Regression_heart.pkl
├── scaler.pkl
├── columns.pkl
```

---
## 📊 Input Features

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Max Heart Rate
* Exercise-Induced Angina
* Oldpeak (ST Depression)
* ST Slope

---

## 🎯 Output

* ⚠️ High Risk of Heart Stroke
* ✅ Low Risk of Heart Stroke

---

## 🧠 How It Works

1. User inputs health parameters
2. Data is encoded (One-Hot Encoding)
3. Data is scaled using StandardScaler
4. Logistic Regression model predicts risk
5. Result is displayed instantly

---

## 📌 Future Improvements

* 🎨 Upgrade UI with Flask + HTML/CSS/JS
* 📊 Add probability score & graphs
* 💾 Store patient data in database
* 🌐 Deploy online

---

## 👨‍🎓 Author

**Shubhabrata Choudhuri**
B.TECH CSE Student | Machine Learning Enthusiast

---

## 📜 License

This project is open-source and free to use.

---

## ⚠️ Disclaimer

This application is for educational purposes only and should not be used as a substitute for professional medical advice.
