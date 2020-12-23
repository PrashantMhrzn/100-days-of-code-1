from utils import info
import dotenv
import os
dotenv.load_dotenv()

API_KEY = os.getenv('API_KEY')


lat, lon = info.get_coords()

data = info.get_weather(lat, lon, API_KEY)

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
heading = """
####################################
# WEATHER APPLICATION USING PYTHON #
####################################"""
print(heading)
print("Location:", data['country'], data['name'])
print("Latitude:", lat)
print("Longitude:", lon)
print("Weather:", data['weather'])
print("Temperature: {}{}".format(data['temp'], u'\u2103'))
