from fastapi import FastAPI
from services.weather import get_weather, get_forecast


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Weather API is running"}

@app.get("/weather/{city}")
def weather(city: str):
    data = get_weather(city)

    if data is None:
        return {"error": "Could not fetch weather data"}

    return data

@app.get("/forecast/{city}")
def forecast(city: str):
    return get_forecast(city)