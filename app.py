import streamlit as st
from src.ml_model import BatteryMLModel
from src.battery_agent import EVSmartAgent
from src.station_finder import get_nearest_charging_station

st.set_page_config(page_title="EV Smart Battery Agent", page_icon="⚡", layout="wide")

st.title("⚡ EV Smart Battery & Range Agent")
st.markdown("Prédiction de l'autonomie et conseils de votre copilote IA.")

ml_model = BatteryMLModel()
agent = EVSmartAgent()


st.sidebar.header("🚗 Vehicle Inputs")
soc = st.sidebar.slider("Battery Charge (%)", 5, 100, 45)
temp = st.sidebar.slider("Temperature (°C)", -10, 45, 25)
speed = st.sidebar.slider("Vitesse current (km/h)", 20, 140, 90)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 ML Predictions")
    predicted_range = ml_model.predict_range(soc, temp, speed)
    st.metric(label="Autonomie Estimée", value=f"{predicted_range} km")
    
    nearest_station = get_nearest_charging_station(soc)
    st.info(f"📍 **Station la plus proche :** {nearest_station['name']} ({nearest_station['distance_km']} km)")

with col2:
    st.subheader("🤖 AI Agent Recommendations")
    if st.button("Obtenir les conseils de l'agent"):
        with st.spinner("Analyzing EV status..."):
            advice = agent.analyze_and_advise(soc, temp, speed, predicted_range, nearest_station)
            st.markdown(advice)