import http.client
import json
import validator
import requests
import os
from dotenv import load_dotenv

load_dotenv()

conn = http.client.HTTPSConnection(os.environ['API_URL'])
API_KEY = os.environ['API_KEY']

def list_all_historical_trades(query_params):
    validator.page_size_query_params(query_params)
    headers = { 'x-api-key': API_KEY }

    if len(query_params) != 1:
        conn.request("GET", "/v3/trade/history?pageSize={}&offset={}".format(query_params['pageSize'], query_params['offset']), headers=headers)
    else:
        conn.request("GET", "/v3/trade/history?pageSize={}".format(query_params['pageSize']), headers=headers)
#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def list_all_active_buy_trades(query_params):
    validator.list_all_active_buy_trades(query_params)
    headers = { 'x-api-key': API_KEY }

    id= ''
    offset = ''
    for key in query_params.keys():
        if key == 'offset':
            offset = 'offset={}'.format(query_params['offset'])

        if key == 'id':
            offset = 'id={}'.format(query_params['id'])
    
    conn.request("GET", "/v3/trade/buy?pageSize={}&{}&{}".format(query_params['pageSize'],id, offset), headers=headers)
    
#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def list_all_active_sell_trades(query_params):
    validator.list_all_active_buy_trades(query_params)
    headers = { 'x-api-key': API_KEY }

    id= ''
    offset = ''
    for key in query_params.keys():
        if key == 'offset':
            offset = 'offset={}'.format(query_params['offset'])

        if key == 'id':
            offset = 'id={}'.format(query_params['id'])
    
    conn.request("GET", "/v3/trade/sell?pageSize={}&{}&{}".format(query_params['pageSize'],id, offset), headers=headers)
    
#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_existing_trade(path_params):
    validator.id_path_param(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/trade/{}".format(path_params['id']), headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def cancel_existing_trade(path_params):
    validator.id_path_param(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("DELETE", "/v3/trade/{}".format(path_params['id']), headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def cancel_all_existing_trades_for_account(path_params):
    validator.id_path_param(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("DELETE", "/v3/trade/account/{}".format(path_params['id']), headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def store_buy_sell_trade(body_params):
    validator.store_buy_sell_trade(body_params)
    body_params = json.dumps(body_params)
    headers = { 
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/trade", body_params, headers)


#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))