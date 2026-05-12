import streamlit as st
from services.weather import get_weather
import requests     


st.title("Weather Dashboard")

city = st.text_input("Enter a city in Denmark")

if city:
    data = get_weather(city)

    if data:
        st.subheader(data["city"])
        st.write(f"Temperature: {data['temp']}°C")
        st.write(f"Condition: {data['description']}")

    else:
        st.error("Could not fetch weather data")