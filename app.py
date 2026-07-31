import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("📊 Customer Churn Prediction")
st.markdown(
    "Predict whether a customer is likely to churn using **Machine Learning**."
)

st.markdown("---")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Customer Information")

age = st.sidebar.number_input(
    "Age",
    min_value=18,
    max_value=80,
    value=30
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Female", "Male", "Other"]
)

city = st.sidebar.selectbox(
    "City",
    [
        "Bangalore",
        "Chennai",
        "Delhi",
        "Hyderabad",
        "Jaipur",
        "Kolkata",
        "Mumbai",
        "Pune",
        "Surat"
    ]
)

total_orders = st.sidebar.number_input(
    "Total Orders",
    min_value=0,
    value=10
)

total_spending = st.sidebar.number_input(
    "Total Spending",
    min_value=0.0,
    value=5000.0
)

avg_order_value = st.sidebar.number_input(
    "Average Order Value",
    min_value=0.0,
    value=500.0
)

last_order_days = st.sidebar.number_input(
    "Days Since Last Order",
    min_value=0,
    value=10
)

customer_tenure = st.sidebar.number_input(
    "Customer Tenure (Days)",
    min_value=1,
    value=365
)

# -----------------------------
# Prediction Button
# -----------------------------
predict = st.sidebar.button("Predict Churn")
