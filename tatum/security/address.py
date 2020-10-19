import http.client
import json
import validator.security as security_validator
import requests
import os
from dotenv import load_dotenv

load_dotenv()

conn = http.client.HTTPSConnection(os.environ['API_URL'])
API_KEY = os.environ['API_KEY']

def check_malicous_address(path_params):
    security_validator.check_malicous_address(path_params)
    headers = {
        'x-api-key': API_KEY
        }

    conn.request("GET", "/v3/security/address/{}".format(path_params['address']), headers=headers)

    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")