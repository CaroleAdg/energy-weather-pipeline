import requests
import datetime
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Paris"

URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def get_weather():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        timestamp = datetime.datetime.now().isoformat()
        result = {
            "city": CITY,
            "timestamp": timestamp,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind_speed": data["wind"]["speed"],
            "weather": data["weather"][0]["description"]
        }

        print("Données météo :", result)
    else:
        print(f"Erreur {response.status_code} : {response.text}")

if __name__ == "__main__":
    get_weather()
