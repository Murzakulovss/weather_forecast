import requests
from django.conf import settings

def get_weather(city: str ):
    api_key = settings.WEATHER_API_KEY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.Timeout:
        return {"error": "Service timeout"}
    except requests.exceptions.ConnectionError:
        return {"error": "Weather service connection error"}
    except requests.exceptions.RequestException:
        return {"error": "Unexpected error while contacting weather service"}

    if response.status_code == 200:
        data =response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "icon": f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
        }
    elif response.status_code == 401:
        return {"error": "Invalid API key"}
    elif response.status_code == 404:
        return {"error": "City not found"}
    elif response.status_code == 429:
        return {"error": "Too many requests"}
    elif response.status_code in(500,502,503):
        return {"error": "Weather service unavailable"}

get_weather("Bishkek")


