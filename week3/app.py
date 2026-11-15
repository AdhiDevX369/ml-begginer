import joblib
import pandas as pd
import streamlit as st

bundle = joblib.load("sl_house_model.pkl")
model, features = bundle["model"], bundle["features"]

st.title("Sri Lankan House Price Predictor")
sqft = st.slider("Floor area (sq ft)", 1000, 9000, 3000, step=100)
perches = st.slider("Land (perches)", 6.0, 25.0, 12.0, step=0.5)
bedrooms = st.slider("Bedrooms", 2, 8, 4)
dist = st.slider("Distance to Colombo Fort (km)", 3.0, 10.5, 6.0, step=0.1)

row = pd.DataFrame([[sqft, perches, bedrooms, dist]], columns=features)
st.metric("Estimated asking price", f"Rs. {model.predict(row)[0]:,.1f} M")
st.caption("Trained on 31 LankaPropertyWeb listings. Valid only within the slider ranges.")
