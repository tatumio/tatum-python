import http.client
import json
import validator
import requests

conn = http.client.HTTPSConnection("api.tatum.io")

def list_all_customers(API_KEY, query_params):
    validator.page_size_query_params(query_params)
    headers = {'x-api-key': API_KEY}
    if len(query_params) != 1:
        conn.request("GET", "/v3/ledger/customer?pageSize={}&offset={}".format(query_params['pageSize'], query_params['offset']), headers=headers)
    else:
        conn.request("GET", "/v3/ledger/customer?pageSize={}".format(query_params['pageSize']), headers=headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def get_customer_details(API_KEY, path_params):
    validator.id_path_param(path_params)
    headers = {'x-api-key': API_KEY}
    conn.request("GET", "/v3/ledger/customer/{}".format(path_params['id']), headers=headers)

    #   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def update_customer(API_KEY, path_params, body_params):
    validator.update_customer(path_params, body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY}
    conn.request("PUT", "/v3/ledger/customer/{}".format(path_params['id']), body_params, headers)

    #   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def activate_customer(API_KEY, path_params):
    validator.id_path_param(path_params)
    headers = {'x-api-key': API_KEY}
    conn.request("PUT", "/v3/ledger/customer/{}/activate".format(path_params['id']), headers=headers)
    #   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def deactivate_customer(API_KEY, path_params):
    validator.id_path_param(path_params)
    headers = {'x-api-key': API_KEY}
    conn.request("PUT", "/v3/ledger/customer/{}/deactivate".format(path_params['id']), headers=headers)
    #   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def enable_customer(API_KEY, path_params):
    validator.id_path_param(path_params)
    headers = {'x-api-key': API_KEY}
    conn.request("PUT", "/v3/ledger/customer/{}/enable".format(path_params['id']), headers=headers)
    #   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def disable_customer(API_KEY, path_params):
    validator.id_path_param(path_params)
    headers = {'x-api-key': API_KEY}
    conn.request("PUT", "/v3/ledger/customer/{}/disable".format(path_params['id']), headers=headers)
    #   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))