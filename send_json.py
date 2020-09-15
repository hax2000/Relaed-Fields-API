import os
import requests
from dotenv import load_dotenv
load_dotenv()

server_url = f'http://{os.getenv("SERVER_URL")}/main/'

login = 'john'
password = 'johnpassword'
TOKEN = requests.post(url=f"{server_url}api-token-auth/",
                      data={'username': login, 'password': password}).json()['token']

data_load_list = [{
    "field1": 1,
    "field2": 2,
    "field3": 3,
    "field4": 4,
    "field5": 5,
    "field6": 6,
    "relfield1": "Related Field №1",
    "relfield2": "Related Field №2",
    "relfield3": "Related Field №3"
} for i in range(1000)
]

load_list_response = requests.post(url=f"{server_url}upload/",
                                   headers={'Authorization': f'Token {TOKEN}'},
                                   json=data_load_list)
print(len(load_list_response.json()))  # need to be 1000
