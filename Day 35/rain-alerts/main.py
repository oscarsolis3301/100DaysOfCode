import requests

params = {
    'lat': 31.761877,
    'lon': -106.485023,
    'appid': '69f04e4613056b159c2761a9d9e664d2'
}
response = requests.get(url='https://api.openweathermap.org/data/2.5/weather', verify=False, params=params)
response.raise_for_status()
print(response.status_code)
data = response.json()

print(data)
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
#print(response.url)
list_of_weather = (weather["hourly"][0:12])
first_12_hours = []
for x in list_of_weather:
    first_12_hours.append(list_of_weather[0]['weather'][0]['id'])

for x in first_12_hours:
    if x == 801:
