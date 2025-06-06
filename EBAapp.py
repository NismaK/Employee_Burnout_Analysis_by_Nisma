import streamlit as st
import numpy as np
import json


with open('model_params.json', 'r') as f:
    model_params = json.load(f)

coefficients = np.array(model_params['coefficients'])
intercept = model_params['intercept']


def predict_burnout(features):
    return np.dot(features, coefficients) + intercept


st.set_page_config(page_title="Employee Burnout Analysis", page_icon="🔥")
st.title("🔥 Employee Burnout Analysis")

st.header("Enter Employee Details:")

satisfaction_level = st.slider("Satisfaction Level", 0.0, 1.0, 0.5)
last_evaluation = st.slider("Last Evaluation Score", 0.0, 1.0, 0.5)
number_project = st.number_input("Number of Projects", min_value=1, max_value=10, value=3)
average_monthly_hours = st.number_input("Average Monthly Hours", min_value=50, max_value=400, value=160)
time_spent_company = st.number_input("Years at Company", min_value=0, max_value=20, value=3)
work_accident = st.selectbox("Had Work Accident?", ("No", "Yes"))
promotion_last_5years = st.selectbox("Promoted in Last 5 Years?", ("No", "Yes"))

work_accident_bin = 1 if work_accident == "Yes" else 0
promotion_bin = 1 if promotion_last_5years == "Yes" else 0

input_features = np.array([
    satisfaction_level, last_evaluation, number_project,
    average_monthly_hours, time_spent_company,
    work_accident_bin, promotion_bin
])

if st.button("Predict Burnout"):
    prediction = predict_burnout(input_features)
    st.write(f"**Model Output (Raw Prediction)**: {prediction:.2f}")
    if prediction > 0.5:
        st.error("⚠️ The employee is likely experiencing burnout.")
    else:
        st.success("✅ The employee is not likely experiencing burnout.")

st.markdown("---")
st.caption("Created with ❤️ by Nisma Kauser")
