import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title and Introduction
st.title("BMI Calculator Chatbot")
st.write("Hello! I'm a chatbot that helps you calculate your BMI and visualize it.")

# Input Section
st.subheader("Enter your details:")
weight = st.number_input("Weight (in kg):", min_value=1.0, max_value=500.0, value=70.0)
height = st.number_input("Height (in meters):", min_value=0.5, max_value=2.5, value=1.75)

# Calculate BMI
if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: **{bmi:.2f}**")

    # Determine BMI Category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    st.write(f"You are classified as: **{category}**")

    # Plotting the BMI Comparison Graph
    fig, ax = plt.subplots()

    # Normal BMI range (18.5 to 24.9)
    x = np.linspace(0, 35, 100)
    y = np.zeros_like(x)
    ax.plot(x, y, color='black', linewidth=2)
    ax.fill_between(x, -0.2, 0.2, where=(x >= 18.5) & (x <= 24.9), 
                    color='green', alpha=0.3, label='Normal BMI Range')

    # User's BMI point
    ax.scatter([bmi], [0], color='red', s=100, label=f'Your BMI: {bmi:.2f}')
    ax.legend(loc='upper right')

    # Labeling
    ax.set_yticks([])
    ax.set_xlim(0, 35)
    ax.set_xlabel("BMI")
    ax.set_title("BMI Comparison Graph")

    # Show the plot
    st.pyplot(fig)
