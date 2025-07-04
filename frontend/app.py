import streamlit as st
from predict import predict_conso

weather_path = "frontend/weather_paris.csv"

prediction_kW, today_weather = predict_conso(weather_path)
prediction_MW = prediction_kW / 1000

st.set_page_config(page_title="Résumé du jour", page_icon="🔆")
st.title("Météo & Consommation - Résumé du jour")

st.subheader(f"Date : {today_weather['date']}")

# Afichage météo
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Temp. moyenne", f"{today_weather['temp_moyenne']} °C")
    st.metric("Temp. min", f"{today_weather['temp_min']} °C")
    st.metric("Temp. max", f"{today_weather['temp_max']} °C")
with col2:
    st.metric("Précipitations", f"{today_weather['precipitations']} mm")
    st.metric("Ensoleillement", f"{today_weather['ensoleillement']} h")
    st.metric("Pression", f"{today_weather['pression']} hPa")
with col3:
    st.metric("Vent", f"{today_weather['vitesse_vent']} km/h")
    st.metric("Rafales", f"{today_weather['rafales_vent']} km/h")

st.markdown("---")

# Affichage prédiction
st.subheader("Prédiction de consommation d'énergie")
st.success(f"Consommation estimée : **{prediction_MW:.2f} MW**")

st.caption("Modèle alimenté par les données météo du jour.")
