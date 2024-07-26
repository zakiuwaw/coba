import streamlit as st
import joblib
import numpy as np

# Load model yang telah dilatih
model = joblib.load('best_model.pkl')

# Judul aplikasi Streamlit
st.title('Uber Fare Prediction App')

# Input dari pengguna
st.header('Enter trip details:')
pick_up_lat = st.number_input('Pick-up Latitude', format="%.6f", value=40.712776)
pick_up_long = st.number_input('Pick-up Longitude', format="%.6f", value=-74.005974)
drop_off_lat = st.number_input('Drop-off Latitude', format="%.6f", value=40.706001)
drop_off_long = st.number_input('Drop-off Longitude', format="%.6f", value=-74.008000)
hour = st.slider('Hour of the Day', 0, 23, 12)
day_of_week = st.slider('Day of the Week', 0, 6, 0)

# Menyiapkan fitur input
features = np.array([pick_up_lat, pick_up_long, drop_off_lat, drop_off_long, hour, day_of_week]).reshape(1, -1)

# Prediksi dan tampilkan hasil
if st.button('Predict Fare'):
    prediction = model.predict(features)
    st.write(f'Predicted Fare Amount: ${prediction[0]:.2f}')
