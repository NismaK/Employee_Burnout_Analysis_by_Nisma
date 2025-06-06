## 🔥 Employee Burnout Analysis
   Employee burnout negatively impacts productivity, job satisfaction, and workplace well-being. This project aims to analyze and predict burnout risks using machine learning, focusing on key factors like workload and work-life balance.
This project mainly leverages a machine learning model to predict the likelihood of employee burnout based on key workplace and behavioral factors.

### 📝 Overview
- **Purpose**: Identify potential burnout risks among employees to enable proactive HR interventions.
- **Model Used**: Logistic Regression (pre-trained and saved as `EBA_LR.pkl`).
- ## ✨ Key Features

- 📈 **Predictive Modeling**: Uses a trained linear regression model to predict burnout risk based on real employee data.
- 🎛️ **Interactive Inputs**: Streamlit sliders and dropdowns for real-time input of employee details.
- 🧠 **Mental Fatigue Insights**: Includes fields like mental fatigue score, resource allocation, and designation to understand burnout causes.
- 📅 **Date Conversion**: Automatically converts "Date of Joining" into a numerical feature (Unix timestamp) for accurate modeling.
- 🏢 **Categorical Encoding**: Gender, Company Type, and WFH availability are one-hot encoded to ensure the model interprets them correctly.
- 📦 **Lightweight Deployment**: Deployable on Streamlit Cloud with a small model footprint via JSON (`model_params.json`).
- ✅ **Clear Feedback**: Returns visual feedback on the likelihood of burnout using color-coded messages.

### 🚀 Web Interface
The project includes a Streamlit-powered web application (`EBAapp.py`) where users can input employee data and get immediate burnout predictions.
## 🔗 Live Demo

Check out the live Streamlit app here:  
👉 [Employee Burnout Analysis Web App](https://employeeburnoutanalysisbynisma-hmj2dfxwcjzqvvkfh34yby.streamlit.app/)
