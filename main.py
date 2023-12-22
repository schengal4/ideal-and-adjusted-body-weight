import streamlit as st

def calculate_ideal_weight(gender, height_inches):
    if gender == "Male":
        ideal_weight = 50 + 2.3 * (height_inches - 60)
    else:  # Female
        ideal_weight = 45.5 + 2.3 * (height_inches - 60)
    return ideal_weight

st.title("Ideal Body Weight")
gender = st.radio("Select Gender", ["Male", "Female"])
height_cm = st.number_input("Enter your height in inches", min_value=1)
actual_weight = st.number_input("Enter your body weight (kg)", min_value=0)
if st.button("Calculate"):
    ideal_weight = calculate_ideal_weight(gender, height_cm)
    st.write(f"Your ideal body weight is {ideal_weight:.2f} kg.")

