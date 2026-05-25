import streamlit as st
import joblib
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>PulseAI</h1>", unsafe_allow_html=True)

st.markdown(
    "<h4 style='text-align: center;'>AI-powered diabetes risk assessment using basic health parameters</h4>",
    unsafe_allow_html=True
)
st.write("Enter your lab results below:")
glucose = st.number_input("Glucose (0–200)", min_value=0.0, max_value=200.0)
bp = st.number_input("Blood Pressure (0–130)", min_value=0.0, max_value=130.0)
weight = st.number_input("Weight (kg)", min_value=1.0)
height_cm = st.number_input("Height (cm)", min_value=1.0)
age = st.number_input("Age (10–100)", min_value=1.0)

# Convert height to meters
height_m = height_cm / 100

# Calculate BMI
if height_m > 0:
    bmi = weight / (height_m ** 2)
    st.write(f"Calculated BMI: {bmi:.2f}")
else:
    bmi = 0
if st.button("Predict Diabetes Risk"):
    input_data = [[glucose, bp, bmi, age]]
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    prob = model.predict_proba(input_scaled)[0][1]
    st.write(f"Risk Probability: {prob*100:.2f}%")
    if prediction[0] == 1:
        st.error("High risk of diabetes ⚠️")
    else:
        st.success("Low risk of diabetes ✅")