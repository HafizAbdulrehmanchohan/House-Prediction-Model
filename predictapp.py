import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Set up the Streamlit app
st.set_page_config(page_title="House Price Predictor", layout="centered")
st.title("🏡 House Price Prediction App")
st.markdown("Enter the details of the house below to get an estimated price prediction.")

# Input fields in the desired order
area = st.number_input("📐 Area (in sq ft)", min_value=100, max_value=10000, value=1000, step=50)
bedrooms = st.slider("🛏️ Bedrooms", 1, 5, 3)
bathrooms = st.slider("🛁 Bathrooms", 1, 4, 2)
floors = st.slider("Floors", 1, 5, 1)
year_built = st.number_input("🏠 Year Built", min_value=1900, max_value=2025, value=2000)

location = st.selectbox("Location", ["Rural", "Suburban", "Urban", "Downtown"])
location_mapping = {"Rural": 1, "Suburban": 2, "Urban": 3, "Downtown": 4}
location_val = location_mapping[location]

condition = st.selectbox("🔧 Condition", ["Poor", "Fair", "Good", "Excellent"])
condition_mapping = {"Poor": 1, "Fair": 2, "Good": 3, "Excellent": 4}
condition_val = condition_mapping[condition]

garage = st.radio("🚗 Garage", ["Yes", "No"])
garage_val = 1 if garage == "Yes" else 0

# Predict button
if st.button("Predict House Price"):
    input_data = np.array([[area, bedrooms, bathrooms, floors, year_built, location_val, condition_val, garage_val]])
    prediction = model.predict(input_data)
    st.success(f"🏷️ Estimated House Price: ${prediction[0]:,.2f}")
