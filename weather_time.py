import requests 
from weather_ss import *

api_adress = "https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=&appid=" + api_key
json_data = requests.get(api_adress).json()

def temp():
    temprature = round(json_data["main"]["temp"]-273.15,1)
    return temprature

def des():
    description = json_data["weather"][0]["description"]
    return description

print(temp())
print(des())