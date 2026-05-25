# 🧠 PulseAI – Diabetes Risk Prediction App

PulseAI is a machine learning-based web application that predicts the risk of diabetes using basic health parameters. It is built using **Python, Scikit-learn, and Streamlit**, and deployed as an interactive web app.

---

## 🚀 Live Demo
👉 (Add your Streamlit link here after deployment)

Example:
https://your-app-name.streamlit.app

---

## 📌 Project Overview

This project uses a **Logistic Regression model** trained on a diabetes dataset to predict whether a person is at risk of diabetes based on:

- Glucose level
- Blood Pressure
- BMI (calculated from height and weight)
- Age

The app also provides a **risk probability score** for better interpretation.

---

## 🧠 Machine Learning Workflow

1. Load dataset (`diabetes.csv`)
2. Select features:
   - Glucose
   - BloodPressure
   - BMI
   - Age
3. Preprocess data using **StandardScaler**
4. Split dataset into training and testing sets
5. Train **Logistic Regression model**
6. Evaluate model performance
7. Save model and scaler using `joblib`

---

## ⚙️ Tech Stack

- Python 🐍
- Pandas
- Scikit-learn
- Streamlit
- Joblib

---

## 📁 Project Structure
