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
# -----------------------------------
# Prediction
# -----------------------------------

if predict:

    # Create a dictionary with all features initialized to 0
    input_data = {feature: 0 for feature in feature_names}

    # Numerical Features
    input_data["total_orders"] = total_orders
    input_data["total_spending"] = total_spending
    input_data["avg_order_value"] = avg_order_value
    input_data["last_order_days"] = last_order_days
    input_data["age"] = age
    input_data["customer_tenure"] = customer_tenure

    # Gender Encoding
    if gender == "Male":
        input_data["gender_Male"] = 1

    elif gender == "Other":
        input_data["gender_Other"] = 1

    # Female is represented by both values remaining 0

    # City Encoding
    city_column = f"city_{city}"

    if city_column in input_data:
        input_data[city_column] = 1

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    # Arrange columns exactly as training
    input_df = input_df[feature_names]

    # Scale input
    input_scaled = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(input_scaled)[0]

    probability = model.predict_proba(input_scaled)[0][1]

    st.markdown("---")

    st.header("Prediction Result")

    if prediction == 1:

        st.error("⚠️ Customer is likely to Churn")

    else:

        st.success("✅ Customer is likely to Stay")

    st.metric(
        "Churn Probability",
        f"{probability*100:.2f}%"
    )

    st.progress(float(probability))

    st.markdown("---")

    st.subheader("Business Recommendation")

    if probability >= 0.75:

        st.error("""
High Risk

• Offer discounts immediately

• Contact customer personally

• Provide loyalty rewards

• Send personalized offers
""")

    elif probability >= 0.40:

        st.warning("""
Medium Risk

• Send promotional emails

• Recommend products

• Offer coupons

• Increase engagement
""")

    else:

        st.success("""
Low Risk

• Customer is loyal

• Continue regular engagement

• Recommend premium services
""")

    st.markdown("---")

    st.subheader("Customer Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Orders", total_orders)

    col2.metric("Spending", f"₹{total_spending:,.2f}")

    col3.metric("Last Order", f"{last_order_days} Days")

    st.markdown("---")

    st.caption(
        "Built using Streamlit | Scikit-learn | Logistic Regression"
    )
