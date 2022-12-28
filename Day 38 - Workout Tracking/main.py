import requests
import datetime
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_USER = os.environ.get("SHEETY_USER")
SHEETY_AUTH_USER = os.environ.get("SHEETY_AUTH_USER")
SHEETY_AUTH_PASS = os.environ.get("SHEETY_AUTH_PASS")

NUTRITIONIX_NATURAL_LANGUAGE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_WORKOUT_ENDPOINT = f'https://api.sheety.co/{SHEETY_USER}/workoutTracking/workouts'

today = datetime.datetime.now()

creds = {
    'Content-Type': 'application/json',
    'x-app-key': API_KEY,
    'x-app-id': APP_ID,
}

params = {
    "query": input('Tell me which exercise you did: '),
    "gender": "male",
    "weight_kg": 56.69,
    "height_cm": 175.26,
    "age": 22
}

request = requests.post(url=NUTRITIONIX_NATURAL_LANGUAGE_ENDPOINT, headers=creds, json=params,
                        auth=(SHEETY_AUTH_USER, SHEETY_AUTH_PASS))

nutrtionix_response = request.json()
print(nutrtionix_response)
exercise_name = nutrtionix_response['exercises'][0]['name']
exercise_duration = nutrtionix_response['exercises'][0]['duration_min']
exercise_calories = nutrtionix_response['exercises'][0]['nf_calories']
print(f'{str(exercise_name).title()} for {exercise_duration} minutes burns {exercise_calories} calories')

body = {
    "workout":
        {
            "date": today.strftime('%d/%m/%Y'),
            "time": today.strftime('%H:%M:%S'),
            "exercise": str(exercise_name).title(),
            "duration": exercise_duration,
            "calories": exercise_calories,
        }
}

# Getting All Cells
sheets = requests.get(SHEETY_WORKOUT_ENDPOINT, auth=(SHEETY_AUTH_USER, SHEETY_AUTH_PASS))
print(sheets.text)

# Adding a Cell
request = requests.post(url=SHEETY_WORKOUT_ENDPOINT, headers=creds, json=body,  auth=(SHEETY_AUTH_USER, SHEETY_AUTH_PASS))
print(f'\nAdding: {request.text}')
