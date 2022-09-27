import requests

param = {
    "lat": 33.685909,
    "lon": -117.824722,
    "appid": "69f04e4613056b159c2761a9d9e664d2",
    "exclude": "current,minutely,daily"
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall?', params=param)
response.raise_for_status()
weather = response.json()
print(weather)
