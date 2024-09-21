import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model, encoder, and scaler
st.title("Sleep Health and Lifestyle Analysis (Pre-trained Model)")

with open('sleep_health_and_lifestyle.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the LabelEncoder
with open('label_encoder.pkl', 'rb') as label_file:
    label_encoder = pickle.load(label_file)

# Load the ColumnTransformer
with open('column_transformer.pkl', 'rb') as transformer_file:
    column_transformer = pickle.load(transformer_file)

# Define categorical and numerical columns as used during model training
categorical_features = ['Gender', 'Occupation', 'BMI Category']
numerical_features = ['Age', 'Sleep Duration', 'Quality of Sleep',
                      'Physical Activity Level', 'Stress Level', 'BP(Systolic)', 
                      'BP(Diastolic)', 'Heart Rate', 'Daily Steps']

# Occupation list based on what was used during training
occupations = [
    "Nurse", "Doctor", "Engineer", "Lawyer", "Teacher", "Accountant",
    "Salesperson", "Software Engineer", "Scientist", "Sales Representative", "Manager"
]

# Input fields for user to provide data
gender = st.selectbox("Gender", options=["Male", "Female"])
age = st.text_input("Age", placeholder="Enter an integer (e.g., 25)")
occupation = st.selectbox("Occupation", options=occupations)
sleep_duration = st.text_input("Sleep Duration", placeholder="Enter hours of sleep (e.g., 7.5)")
quality_of_sleep = st.text_input("Quality of Sleep", placeholder="Enter a score from 1-10")
physical_activity_level = st.text_input("Physical Activity Level", placeholder="Enter a score from 1-100")
stress_level = st.text_input("Stress Level", placeholder="Enter a score from 1-10")
bmi_category = st.selectbox("BMI Category", options=["Normal", "Overweight", "Obese"])
blood_pressure = st.text_input("Blood Pressure", placeholder="Enter blood pressure in mmHg (e.g., 120/80)")
heart_rate = st.text_input("Heart Rate", placeholder="Enter beats per minute (e.g., 70)")
daily_steps = st.text_input("Daily Steps", placeholder="Enter the number of steps (e.g., 5000)")

# Sleep disorder mapping
sleep_disorder_mapping = {
    0: "None",
    1: "Sleep Apnea",
    2: "Insomnia"
}

# Button for prediction
if st.button("Predict Sleep Disorder"):
    try:
        # Prepare input data as a DataFrame
        input_df = pd.DataFrame({
            'Gender': [gender],
            'Age': [int(age) if age.isdigit() else 0],
            'Occupation': [occupation],
            'Sleep Duration': [float(sleep_duration) if sleep_duration else 0.0],
            'Quality of Sleep': [int(quality_of_sleep) if quality_of_sleep.isdigit() else 0],
            'Physical Activity Level': [int(physical_activity_level) if physical_activity_level.isdigit() else 0],
            'Stress Level': [int(stress_level) if stress_level.isdigit() else 0],
            'BMI Category': [bmi_category],
            'BP(Systolic)': [int(blood_pressure.split('/')[0]) if blood_pressure else 0],
            'BP(Diastolic)': [int(blood_pressure.split('/')[1]) if blood_pressure and len(blood_pressure.split('/')) > 1 else 0],
            'Heart Rate': [int(heart_rate) if heart_rate.isdigit() else 0],
            'Daily Steps': [int(daily_steps) if daily_steps.isdigit() else 0]
        })

        # Standardize the input features using the pre-trained scaler
        input_scaled = column_transformer.transform(input_df)

        # Make predictions using the pre-trained model
        predictions = model.predict(input_scaled)

        # Ensure predictions is a 1D array
        if predictions.ndim > 1:
            predictions = predictions.flatten()

        # Map the predicted value to the sleep disorder label
        predicted_disorder = sleep_disorder_mapping.get(predictions[0], "Unknown")

        st.subheader("Prediction")
        st.write(f"The predicted sleep disorder is: {predicted_disorder}")

    except Exception as e:
        st.error(f"Input error: {str(e)}")
