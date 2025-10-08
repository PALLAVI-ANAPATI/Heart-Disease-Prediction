import os
import pickle
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Heart Disease Prediction",
                   layout="wide",
                   page_icon="❤️")

# Get working directory of the main file
working_dir = os.path.dirname(os.path.abspath(__file__))

# Load the saved heart disease model
model_path = f"heart_disease_model.sav"
heart_disease_model = pickle.load(open(model_path, 'rb'))

# App title
st.title("❤️ Heart Disease Prediction using Machine Learning")

st.markdown("### Enter the following details:")

# Vertical input fields
age = st.text_input("Age")
sex = st.text_input("Sex (1 = male, 0 = female)")
cp = st.text_input("Chest Pain Type (0–3)")
trestbps = st.text_input("Resting Blood Pressure (mm Hg)")
chol = st.text_input("Serum Cholesterol (mg/dl)")
fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl (1 = true, 0 = false)")
restecg = st.text_input("Resting ECG Results (0–2)")
thalach = st.text_input("Maximum Heart Rate Achieved")
exang = st.text_input("Exercise Induced Angina (1 = yes, 0 = no)")
oldpeak = st.text_input("ST Depression Induced by Exercise")
slope = st.text_input("Slope of Peak Exercise ST Segment (0–2)")
ca = st.text_input("Number of Major Vessels (0–3)")
thal = st.text_input("Thal (0 = normal, 1 = fixed defect, 2 = reversible defect)")

# Prediction section
heart_diagnosis = ""

if st.button("🔍 Predict Heart Disease"):
    try:
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg,
                      thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]

        # Model prediction
        prediction = heart_disease_model.predict([user_input])

        if prediction[0] == 1:
            heart_diagnosis = "🚨 The person **has heart disease**."
        else:
            heart_diagnosis = "✅ The person **does not have heart disease**."

        st.success(heart_diagnosis)
    except ValueError:
        st.error("⚠️ Please enter valid numeric values in all fields.")
    except Exception as e:
        st.error(f"Error: {str(e)}")


