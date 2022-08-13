import smtplib
import requests
from datetime import datetime
import time

MY_LAT = 31.790280384297162
MY_LONG = -106.51167523415128

PASSWORD = "evjrgqurvboeantc"
EMAIL = "OscarLearnsPython@gmail.com"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 6
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 6
#
# print(data['results'])
time_now = datetime.now()

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

running = True


def night_time():
    if time_now.hour > sunset or time_now.hour < sunrise:
        print('Currently nighttime')
        return True


def iss_checker(night):
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and night:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                                msg=f"Subject:Look Above Right Now! \n\nThe ISS is above your head")
            print('Email Sent!')


while running:
    print('Program running')
    night_time = night_time()
    iss_checker(night_time)
    time.sleep(60)
