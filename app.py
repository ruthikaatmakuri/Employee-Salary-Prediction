import streamlit as st
import pandas as pd
import joblib
import os

# -----------------------------
# Load Trained Model and Input Columns Safely
# -----------------------------
@st.cache_resource
def load_model():
    try:
        model = joblib.load("best_model.pkl")
        input_cols = joblib.load("input_columns.pkl")
        return model, input_cols
    except FileNotFoundError:
        st.error("🚫 Model files not found. Please ensure 'best_model.pkl' and 'input_columns.pkl' are in the directory.")
        return None, None

model, input_columns = load_model()

# -----------------------------
# App Configuration
# -----------------------------
st.set_page_config(page_title="Salary Predictor", layout="centered")
st.title("💼 Employee Salary Predictor")
st.markdown("Use this tool to estimate the expected salary based on your profile.")

# -----------------------------
# Sidebar for Instructions
# -----------------------------
with st.sidebar:
    st.header("ℹ️ Instructions")
    st.write("""
        - Select your **company**, **job title**, **education level**, **location**.
        - Enter your **years of experience**.
        - Click the **Predict Salary** button to see the estimated salary.
    """)
    st.markdown("---")
    st.info("Ensure the model is trained with similar categorical values to get accurate predictions.")

# -----------------------------
# Input Form
# -----------------------------
st.subheader("📋 Enter your details")

col1, col2 = st.columns(2)

with col1:
    company = st.selectbox(
        "🏢 Company", 
        ['Google', 'Amazon', 'Facebook', 'Microsoft', 'TCS', 'Infosys', 'Wipro'],
        help="Choose the company where the job is offered."
    )

    education = st.selectbox(
        "🎓 Education Level", 
        ['High School', 'Bachelor', 'Master', 'PhD'],
        help="Your highest level of formal education."
    )

with col2:
    experience = st.number_input(
        "⌛ Years of Experience", 
        min_value=0, max_value=50, value=2,
        help="Total years of relevant work experience."
    )

    location = st.selectbox(
        "📍 Location", 
        ['Bangalore', 'Hyderabad', 'Delhi', 'Mumbai', 'Chennai', 'Pune'],
        help="City where the job is located."
    )

job_title = st.selectbox(
    "💼 Job Title", 
    ['Data Scientist', 'Software Engineer', 'Product Manager', 'HR', 'Business Analyst'],
    help="Job designation you are applying for."
)

# -----------------------------
# Predict Button
# -----------------------------
if st.button("🔍 Predict Salary"):
    if model is None or input_columns is None:
        st.warning("Model not loaded. Please check your files.")
    else:
        # Construct user input dictionary
        user_input = {
            'Company': company,
            'Education Level': education,
            'Years of Experience': experience,
            'Location': location,
            'Job Title': job_title,
        }

        # Convert input to DataFrame and one-hot encode
        input_df = pd.DataFrame([user_input])
        input_df_encoded = pd.get_dummies(input_df)

        # Add any missing columns (fill with 0s)
        for col in input_columns:
            if col not in input_df_encoded.columns:
                input_df_encoded[col] = 0

        # Reorder columns to match model training
        input_df_encoded = input_df_encoded[input_columns]

        try:
            # Predict salary
            predicted_salary = model.predict(input_df_encoded)[0]
            st.success(f"💰 **Estimated Annual Salary:** ₹{predicted_salary:,.2f}")
        except Exception as e:
            st.error(f"Prediction failed. Error: {e}")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown("🔧 *This is a demo salary predictor. Actual salaries may vary based on market conditions.*")
