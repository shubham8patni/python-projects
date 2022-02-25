from operator import ge
import requests
from werkzeug import Response

API_KEY = "0da10599861aad9142cfabf12e8c89c9"
BASE_URL = f"http://api.openweathermap.org/data/2.5/weather"
CITY = input("Enter City name: ")

request_url = f"{BASE_URL}?q={CITY}&appid={API_KEY}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"]-273.15,2)
    humidity = data["main"]["humidity"]
    print(f"CITY: {CITY} \nTemperature: {temperature} celcius \nHumidity: {humidity} \nWeather: {weather}")
else:
    print("An error occured")
