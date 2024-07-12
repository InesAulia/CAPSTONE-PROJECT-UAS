import pickle
import numpy as np
import streamlit as st

#save model
model = pickle.load(open('prediksi.sav','rb'))

#Title
st.markdown("""
    <style>
        .title {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            text-align: center;
            border-radius: 5px;
            margin-bottom: 20px;
        }
            
        .prediction-button {
            background-color: #2196F3;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .prediction-button:hover {
            background-color: #1976D2;
        }
        .result {
            background-color: #2196F3;
            color: white;
            padding: 10px;
            border-radius: 5px;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">Prediksi Penyakit Jantung</h1>', unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    age = st.text_input('Umur')

with col2:
    sex = st.text_input('Jenis Kelamin')

with col1:
    cp = st.text_input('Nyeri Dada')

with col2:
    trestbps = st.text_input('Tekanan Darah')

with col1:
    chol = st.text_input('Kolesterol')

with col2:
    fbs = st.text_input('Gula Darah')

with col1:
    restecg = st.text_input('Hasil Electrocardiografi')

with col2:
    thalach = st.text_input('Detak Jantung Maksimal')

with col1:
    exang = st.text_input('Induksi Angina')

with col2:
    oldpeak = st.text_input('ST Depresi')


#code prediksi
jantung_diagnosis = ''

# Prediction button
if st.button('Prediksi'):
    try:
        # Convert input to float
        inputs = np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak]).astype(float)
        
        # Make prediction
        jantung_prediction = model.predict([inputs])

        # Set diagnosis message based on prediction
        if jantung_prediction[0] == 1:
            jantung_diagnosis = 'Terkena Penyakit Jantung'
        else:
            jantung_diagnosis = 'Tidak Terkena Penyakit Jantung'
    
    except ValueError:
        st.error("Pastikan untuk mengisi semua kolom dengan angka.")

# Display diagnosis result
st.success(jantung_diagnosis)