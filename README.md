<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sleep Health and Lifestyle Analysis (Pre-trained Model) - README</title>
</head>
<body>

<h1>Sleep Health and Lifestyle Analysis (Pre-trained Model)</h1>

<p>This Streamlit application leverages a pre-trained machine learning model to analyze user input data related to sleep health and lifestyle. The model predicts whether a person may have a sleep disorder based on their health and lifestyle attributes.</p>

<h2>Features</h2>
<ul>
    <li>Input fields for demographic, health, and lifestyle attributes like <em>Gender, Age, Sleep Duration, Physical Activity Level, etc.</em></li>
    <li>Pre-trained model using pickle files (<code>sleep_health_and_lifestyle.pkl</code>, <code>label_encoder.pkl</code>, <code>column_transformer.pkl</code>) for prediction.</li>
    <li>Prediction of possible sleep disorders such as <em>Sleep Apnea</em> and <em>Insomnia</em>.</li>
</ul>

<h2>Application Setup</h2>
<ol>
    <li>Install the required libraries from the requirements file:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Ensure you have the following pre-trained files in the same directory as the script:
        <ul>
            <li><code>sleep_health_and_lifestyle.pkl</code> (Pre-trained model)</li>
            <li><code>label_encoder.pkl</code> (Label encoder)</li>
            <li><code>column_transformer.pkl</code> (Pre-trained transformer)</li>
        </ul>
    </li>
    <li>Run the application:
        <pre><code>streamlit run application.py</code></pre>
    </li>
</ol>

<h2>Input Fields</h2>
<ul>
    <li><strong>Person ID:</strong> Integer identifier for the person (e.g., 101).</li>
    <li><strong>Gender:</strong> Select either "Male" or "Female".</li>
    <li><strong>Age:</strong> Integer value representing age.</li>
    <li><strong>Occupation:</strong> Choose from predefined options like <em>Nurse, Doctor, Engineer, etc.</em></li>
    <li><strong>Sleep Duration:</strong> Hours of sleep per day (e.g., 7.5).</li>
    <li><strong>Quality of Sleep:</strong> A score between 1-10 indicating sleep quality.</li>
    <li><strong>Physical Activity Level:</strong> A score between 1-100 representing physical activity level.</li>
    <li><strong>Stress Level:</strong> A score between 1-10 indicating stress level.</li>
    <li><strong>BMI Category:</strong> Choose from predefined categories: <em>Normal, Overweight, Obese</em>.</li>
    <li><strong>Blood Pressure:</strong> Input in the format <code>Systolic/Diastolic</code> (e.g., 120/80).</li>
    <li><strong>Heart Rate:</strong> Beats per minute.</li>
    <li><strong>Daily Steps:</strong> Number of steps per day.</li>
</ul>

<h2>Prediction</h2>
<p>Upon providing all inputs and clicking the "Predict Sleep Disorder" button, the application will run the following steps:</p>
<ol>
    <li>Transform the input features using a pre-trained <code>ColumnTransformer</code>.</li>
    <li>Make predictions using the pre-trained machine learning model.</li>
    <li>Display the predicted sleep disorder (e.g., Sleep Apnea, Insomnia) or "None".</li>
</ol>

<h2>Error Handling</h2>
<p>If an invalid input is provided, the application will display an error message explaining the issue.</p>

<h2>Technologies Used</h2>
<ul>
    <li>Python</li>
    <li>Streamlit</li>
    <li>Pandas</li>
    <li>Pickle (for loading pre-trained model and transformers)</li>
</ul>

<h2>Code Snippet</h2>
<p>The core logic for the prediction is as follows:</p>
<pre><code>predictions = model.predict(input_scaled)
predicted_disorder = sleep_disorder_mapping.get(predictions[0], "Unknown")
st.write(f"The predicted sleep disorder is: {predicted_disorder}")</code></pre>

<p>To test the app <a href="https://health-prediction-kkgfjcqh8t29reulxnxuvg.streamlit.app/" target="_blank">click here</a>.</p>

</body>
</html>
