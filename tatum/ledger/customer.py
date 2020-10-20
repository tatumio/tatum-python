import http.client
import json
import validator.ledger as ledger_validator
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

def list_all_customers(query_params):
    if ledger_validator.page_size_query_params(query_params):
        if len(query_params) != 1:
            conn.request("GET", "/v3/ledger/customer?pageSize={}&offset={}".format(query_params['pageSize'], query_params['offset']), headers=headers())
        else:
            conn.request("GET", "/v3/ledger/customer?pageSize={}".format(query_params['pageSize']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_customer_details(path_params):
    if ledger_validator.id_path_param(path_params):
        conn.request("GET", "/v3/ledger/customer/{}".format(path_params['id']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def update_customer(path_params, body_params):
    if ledger_validator.update_customer(path_params, body_params):
        body_params = json.dumps(body_params)
        conn.request("PUT", "/v3/ledger/customer/{}".format(path_params['id']), body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def activate_customer(path_params):
    if ledger_validator.id_path_param(path_params):
        conn.request("PUT", "/v3/ledger/customer/{}/activate".format(path_params['id']), headers=headers())  
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def deactivate_customer(path_params):
    if ledger_validator.id_path_param(path_params):
        conn.request("PUT", "/v3/ledger/customer/{}/deactivate".format(path_params['id']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def enable_customer(path_params):
    if ledger_validator.id_path_param(path_params):
        conn.request("PUT", "/v3/ledger/customer/{}/enable".format(path_params['id']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def disable_customer(path_params):
    if ledger_validator.id_path_param(path_params):
        conn.request("PUT", "/v3/ledger/customer/{}/disable".format(path_params['id']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")