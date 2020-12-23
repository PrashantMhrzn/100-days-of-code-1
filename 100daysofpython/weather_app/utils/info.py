import geocoder
import requests

import sys


def get_coords():
    geocoder_result = geocoder.ip('me')
    coords = geocoder_result.latlng
    return coords


def get_weather(lat, lon, api_key):
    URL = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}'
    try:
        res = requests.get(URL)
        if res.status_code == 200:
            data = res.json()
            temperature = data['main']['temp']
            weather = data['weather'][0]['description']
            country = data['sys']['country']
            name = data['name']
            context = {'temp': temperature,
                       'weather': weather,
                       'country': country,
                       'name': name}
            return context
        else:
            sys.exit(f"{res.status_code}: {res.json()['message']}")
    except requests.exceptions.RequestException as e:
        sys.exit(f"An error occured: {e}")
