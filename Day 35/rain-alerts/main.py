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
    "lat": 48.191311,
    "lon": -122.126488,
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

account_sid = "ACde37ac0c708218fe613b664bfc7f6003"
auth_token = "df8a75478f0ca87b808e3510260f944f"

client = Client(account_sid, auth_token)

if will_rain:
    message = client.messages \
        .create(
        body="It's going to rain today. Don't forget your umbrella.",
        from_='+13022087105',
        to='+19498423049'
    )
    print(message.status)
else:
    print('It will not be raining in your area')
# list_of_all_weather = (weather["hourly"][:12])
# print(list_of_all_weather[0])
# first_12_hours = []
# for x in list_of_weather:
#     first_12_hours.append(list_of_weather[0]['weather'][0]['id'])
#
# for hours in first_12_hours:
#     if hours < 700:
#         print('')
