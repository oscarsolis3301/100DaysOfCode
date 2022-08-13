import requests
from datetime import datetime

#
#
# response = requests.get(url='http://api.open-notify.org/iss-now.json/')
# response.raise_for_status()
#
# longitude = response.json()['iss_position']['longitude']
# latitude = response.json()['iss_position']['latitude']
#
# iss_position = (longitude, latitude)
#
# params = {"lat": latitude,
#           "lng": longitude}
#
# sunset = requests.get(url='https://api.sunrise-sunset.org/json/', parameters=params)
# sunset.raise_for_status()
#
# print(iss_position)

LATITUDE = 31.761877
LONGITUDE = 106.485023

parameters = {"lat": LATITUDE,
              "lng": LONGITUDE,
              "formatted": 0}
response = requests.get(url='https://api.sunrise-sunset.org/json', verify=False, params=parameters)
response.raise_for_status()
data = response.json()


sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

time_now = datetime.now()

print(f'Sunrise: {sunrise}')
print(f'Sunset: {sunset}')
print(f'Time now: {time_now.hour}')