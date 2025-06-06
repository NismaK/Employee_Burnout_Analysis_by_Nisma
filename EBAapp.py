import streamlit as st
import numpy as np
import json
import pandas as pd

# Load trained model parameters
with open('model_params.json', 'r') as f:
    model_params = json.load(f)

coefficients = np.array(model_params['coefficients'])
intercept = model_params['intercept']

# One-hot encoding reference for categorical features
categorical_values = {
    'Gender': ['Male', 'Female'],
    'Company Type': ['Product', 'Service'],
    'WFH Setup Available': ['Yes', 'No']
}

def preprocess_input(doj, gender, company_type, wfh, designation, resource_alloc, mental_fatigue):
    # Convert Date of Joining to Unix timestamp
    try:
        doj_timestamp = pd.to_datetime(doj).timestamp()
    except:
        doj_timestamp = 0

    # One-hot encode categorical values in the same order as training
    gender_encoded = [1 if gender == val else 0 for val in categorical_values['Gender']]
    company_encoded = [1 if company_type == val else 0 for val in categorical_values['Company Type']]
    wfh_encoded = [1 if wfh == val else 0 for val in categorical_values['WFH Setup Available']]

    # Final input vector
    features = [doj_timestamp, designation, resource_alloc, mental_fatigue] + \
               gender_encoded + company_encoded + wfh_encoded
    return np.array(features)

def predict_burnout(features):
    return np.dot(features, coefficients) + intercept


# Streamlit UI
st.set_page_config(page_title="Employee Burnout Analysis", page_icon="🔥")
st.title("🔥 Employee Burnout Prediction")

st.header("Enter Employee Information:")

doj = st.date_input("Date of Joining")
gender = st.selectbox("Gender", categorical_values['Gender'])
company_type = st.selectbox("Company Type", categorical_values['Company Type'])
wfh_available = st.selectbox("WFH Setup Available", categorical_values['WFH Setup Available'])
designation = st.slider("Designation Level (0-5)", min_value=0, max_value=5, value=2)
resource_alloc = st.slider("Resource Allocation (1-10)", min_value=1, max_value=10, value=5)
mental_fatigue = st.slider("Mental Fatigue Score", min_value=0.0, max_value=10.0, value=5.0)

if st.button("Predict Burnout"):
    features = preprocess_input(doj, gender, company_type, wfh_available, designation, resource_alloc, mental_fatigue)
    prediction = predict_burnout(features)
    st.write(f"**Predicted Burnout Score:** {prediction:.2f}")

    if prediction > 0.5:
        st.error("⚠️ High risk of burnout detected.")
    else:
        st.success("✅ Low risk of burnout.")

st.markdown("---")
st.caption("Created by Nisma Kauser")

