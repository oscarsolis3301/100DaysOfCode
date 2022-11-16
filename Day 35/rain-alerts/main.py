import requests
from twilio.rest import Client

# params = {
#     'lat': 31.761877,
#     'lon': -106.485023,
#     'appid': '69f04e4613056b159c2761a9d9e664d2'
# }
# response = requests.get(url='https://api.openweathermap.org/data/2.5/weather', verify=False, params=params)
# response.raise_for_status()
# print(response.status_code)
# data = response.json()

# print(data)

param = {
    "lat": 44.977753,
    "lon": -93.265015,
    "appid": "69f04e4613056b159c2761a9d9e664d2",
    "exclude": "current,minutely,daily"
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall?', params=param)
response.raise_for_status()
weather = response.json()
print("The url response is: " + response.url)
will_rain = False
list_of_weather = weather['hourly'][0:12]
for hour in list_of_weather:
    if hour['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    print("It's going to rain today. Don't forget your umbrella")
# list_of_all_weather = (weather["hourly"][:12])
# print(list_of_all_weather[0])
# first_12_hours = []
# for x in list_of_weather:
#     first_12_hours.append(list_of_weather[0]['weather'][0]['id'])
#
# for hours in first_12_hours:
#     if hours < 700:
#         print('')
