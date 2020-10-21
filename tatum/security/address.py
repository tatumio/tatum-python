import http.client
import json
import validator.security as security_validator
import requests
import os
from dotenv import load_dotenv
load_dotenv()

conn = http.client.HTTPSConnection(os.environ['API_URL'])
API_KEY = os.environ['API_KEY']

def headers(for_post = False):
    if for_post:
        return {
            'content-type': "application/json",
            'x-api-key': API_KEY
            }
    else:
        return {
            'x-api-key': API_KEY
            }

def check_malicous_address(path_params):
    if security_validator.check_malicous_address(path_params):
        conn.request("GET", "/v3/security/address/{}".format(path_params['address']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")