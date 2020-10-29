from flask import current_app
import requests

def weather_by_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key": "a9d38405ca4c4368b3a142732202809",
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    result = requests.get(weather_url, params=params)
    weather = result.json()
    if 'data' in weather:
        if 'weather' in weather['data']:
            try:
                return weather['data']['weather'][0]
            except(IndexError, TypeError):
                return False    
    return weather
      

if __name__ == "__main__":
    weather = weather_by_city("Moscow,Russia")
    print(weather['maxtempC'], weather['mintempC']) 