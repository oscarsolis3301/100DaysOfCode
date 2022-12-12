import requests
from datetime import datetime

USERNAME = 'venzeti'
TOKEN = 'jfsdlkjfdsfa3301faufh'
pixela_endpoint = 'https://pixe.la/v1/users'

today = f'{datetime.now().strftime("%Y%m%d")}'

pixela_params = {
    'token': f'{TOKEN}',
    'username': f'{USERNAME}',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': 'graph1',
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_endpoint = f'{graph_endpoint}/graph1'

post_config = {
    'date': f'{today}',
    'quantity': '10'
}

put_endpoint = f'{post_endpoint}/{today}'
response = requests.put(url=post_endpoint, headers=headers, )
print(response.text)
# response = requests.post(url=post_endpoint, headers=headers, json=post_config)
# print(response.text)
