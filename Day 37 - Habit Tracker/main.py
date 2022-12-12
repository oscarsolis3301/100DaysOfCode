import requests

USERNAME = 'venzeti'
TOKEN = 'jfsdlkjfdsfa3301faufh'
pixela_endpoint = 'https://pixe.la/v1/users'

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

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

print(response.text)
