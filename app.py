import streamlit as st
import pandas as pd
import joblib
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)
st.title("📊 Customer Churn Prediction")

st.write(
    "Predict whether a customer is likely to churn using Machine Learning."
)
