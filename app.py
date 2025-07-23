import streamlit as st
import joblib
import pandas as pd
import numpy as np
# & "C:\Users\hecto\AppData\Local\Programs\Python\Python311\python.exe" -m streamlit run app.py
#Cargar modelo y scalers
modelo = joblib.load("modelo_de_fraude.pkl")
scaler_amount = joblib.load("scaler_amount.pkl")
scaler_time = joblib.load("scaler_time.pkl")

st.title("💳 Detector de Fraude en Transacciones")

st.markdown("Introduce los valores para cada variable V1 a V28, el monto (`Amount`) y el tiempo (`Time`).")

#Inputs de usuario
v_features = []
for i in range(1, 29):
    v = st.number_input(f"V{i}", value=0.0, step=0.1)
    v_features.append(v)
    st.write(f"Valor ingresado para V{i}: {v:.10f}")  # Muestra 10 decimales para confirmar


amount = st.number_input("Monto de la transacción (Amount)", value=0.0, step=0.1)
time = st.number_input("Tiempo desde la primera transacción (Time)", value=0.0, step=1.0)

# Botón para predecir
if st.button("Predecir"):
    # Escalar amount y time
    scaled_amount = scaler_amount.transform([[amount]])[0][0]
    scaled_time = scaler_time.transform([[time]])[0][0]

    # Armar el vector completo en el orden correcto
    features = v_features + [scaled_amount, scaled_time]
    column_names = [f"V{i}" for i in range(1, 29)] + ["scaled_Amount", "scaled_Time"]
    features_df = pd.DataFrame([features], columns=column_names)

    # Hacer predicción
    pred = modelo.predict(features_df)[0]
    prob = modelo.predict_proba(features_df)[0][1]

    # Mostrar resultado
    if pred == 1:
        st.error(f"⚠️ FRAUDE detectado con probabilidad {prob:.2%}")
    else:
        st.success(f"✅ Transacción legítima con probabilidad de fraude {prob:.2%}")
