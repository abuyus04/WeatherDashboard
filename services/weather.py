
import requests # requests lader koden tale med websider (APIs)

API_KEY = "d3ba092ff4bd774e3f96ffb3762a0314" # definerer api


def get_weather(city): #henter by

    url =  f"http://api.openweathermap.org/data/2.5/weather?q={city},DK&appid={API_KEY}&units=metric"
    # bygger api request


    response = requests.get(url)
    # sender request så result er stored i response
    
    print(response.status_code)   # ADD THIS
    print(response.text)          # ADD THIS
    

    if response.status_code != 200: # checker hvis response er andet end 200(success)
        return None
    
    data = response.json() # API sender messy data tilbage i JSON

    # her er den fx city vi har søgt efter sendt tilbage of istedet for at få city tilbage får vi
    # fx Copenhagen
    return {
        "city": city,
        "temp": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }

def get_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},DK&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code != 200:
        return None
     
    data = response.json()

    forecast_data = []

    for item in data["list"]:
        forecast_data.append({
            "time": item["dt_txt"],
            "temp": item["main"]["temp"]
        })

    return forecast_data
