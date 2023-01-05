import requests
from keys import *


DEFAULT_KIWI_ENDPOINT = "https://www.api.tequila.kiwi.com/v2/search"

params = {
    "apikey": KIWI_API_KEY,
    "fly_from": "SNA",
    "date_from": "01/04/2023",
    "date_to": "05/05/2023"
}

response = requests.get(url=DEFAULT_KIWI_ENDPOINT, headers=params)
print(response.status_code)
kiwi_search = response.json()
print(kiwi_search)
