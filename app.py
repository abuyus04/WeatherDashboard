import streamlit as st
from services.weather import get_weather
import requests     


# Sky blue theme farver
st.markdown(
    """
    <style>
    .stApp {
        background-color: #24A4F2;
    }
    h1, h2, h3, p {
        color: #0a3d62;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Weather Dashboard")

city = st.text_input("Enter a city in Denmark")

if city:

    # bruger nu FastAPI
    response = requests.get(f"http://127.0.0.1:8000/weather/{city}")

    if response.status_code == 200:
        data = response.json()

        if data:
            st.subheader(data["city"])
            st.write(f"Temperature: {data['temp']}°C")
            st.write(f"Condition: {data['description']}")

        else:
            st.error("Could not fetch weather data")

    else:
        st.error("API not responding")

 
    forecast_response = requests.get(f"http://127.0.0.1:8000/forecast/{city}")

    if forecast_response.status_code == 200:
        forecast_data = forecast_response.json()

        st.subheader("Forecast")

        for item in forecast_data[:8]:  # viser de første 8 entries
            st.write(f"{item['time']} → {item['temp']}°C")