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

def list_all_historical_trades(query_params):
    if ledger_validator.page_size_query_params(query_params):
        if len(query_params) != 1:
            conn.request("GET", "/v3/trade/history?pageSize={}&offset={}".format(query_params['pageSize'], query_params['offset']), headers=headers())
        else:
            conn.request("GET", "/v3/trade/history?pageSize={}".format(query_params['pageSize']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def list_all_active_buy_trades(query_params):
    if ledger_validator.list_all_active_buy_trades(query_params):
        id= ''
        offset = ''
        for key in query_params.keys():
            if key == 'offset':
                offset = 'offset={}'.format(query_params['offset'])

            if key == 'id':
                offset = 'id={}'.format(query_params['id'])
        
        conn.request("GET", "/v3/trade/buy?pageSize={}&{}&{}".format(query_params['pageSize'],id, offset), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def list_all_active_sell_trades(query_params):
    if ledger_validator.list_all_active_buy_trades(query_params):
        id= ''
        offset = ''
        for key in query_params.keys():
            if key == 'offset':
                offset = 'offset={}'.format(query_params['offset'])

            if key == 'id':
                offset = 'id={}'.format(query_params['id'])
        
        conn.request("GET", "/v3/trade/sell?pageSize={}&{}&{}".format(query_params['pageSize'],id, offset), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_existing_trade(path_params):
    if ledger_validator.id_path_param(path_params):
        conn.request("GET", "/v3/trade/{}".format(path_params['id']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def cancel_existing_trade(path_params):
    if ledger_validator.id_path_param(path_params):
        conn.request("DELETE", "/v3/trade/{}".format(path_params['id']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def cancel_all_existing_trades_for_account(path_params):
    if ledger_validator.id_path_param(path_params):
        conn.request("DELETE", "/v3/trade/account/{}".format(path_params['id']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def store_buy_sell_trade(body_params):
    if ledger_validator.store_buy_sell_trade(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/trade", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")