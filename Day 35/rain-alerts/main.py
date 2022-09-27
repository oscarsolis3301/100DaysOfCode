import requests

param = {
    "lat": 33.685909,
    "lng": -117.824722,

}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall?')
