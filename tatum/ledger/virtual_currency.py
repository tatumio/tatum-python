import http.client
import json
import validator
import requests
import os
from dotenv import load_dotenv

load_dotenv()

conn = http.client.HTTPSConnection(os.environ['API_URL'])
API_KEY = os.environ['API_KEY']


def create_new_vitual_currency(body_params):
    validator.create_new_vitual_currency(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }

    conn.request("POST", "/v3/ledger/virtualCurrency", body_params, headers)


#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def update_vitual_currency(body_params):
    validator.update_vitual_currency(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }

    conn.request("PUT", "/v3/ledger/virtualCurrency", body_params, headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def get_virtual_currency(path_params):
    validator.get_virtual_currency(path_params)
    headers = {
        'x-api-key': API_KEY
        }

    conn.request("GET", "/v3/ledger/virtualCurrency/{}".format(path_params['name']), headers=headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def create_new_supply_of_virtual_currency(body_params):
    validator.create_new_supply_of_virtual_currency(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }

    conn.request("PUT", "/v3/ledger/virtualCurrency/mint", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def destroy_supply_of_virtual_currency(body_params):
    validator.create_new_supply_of_virtual_currency(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }

    conn.request("PUT", "/v3/ledger/virtualCurrency/mint", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))