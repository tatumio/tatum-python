import cerberus
import re
from termcolor import colored

v = cerberus.Validator()

def erros_print(v):
    if v.errors != {}:
        print(colored(v.errors, 'red')) 
        return False
    else:
        return True

def check_allowed_chars(allowed_chars, variableName, variableValue):
    match = re.search(allowed_chars, variableValue)
    if match is None:
        print(colored("'{}': contains not allowed characters".format(variableName), 'red'))
        return False
    else:
        return True


def check_correct_value_from_define_list(list, variableName, variableValue):
    correct = False
    for i in range(0, len(list)):
        if variableValue == list[i]:
            correct = True
            break
    if correct == False:
        print(colored('"{}": is not allowed type'.format(variableName), 'red'))
        return False
    else:
        return True

def id_path_param(path_params):
    path_schema = {
            "id" : {"required": True, "type" : "string"}
        }

    v.validate(path_params, path_schema)
    return erros_print(v)

def page_size_query_params(query_params):
    schema = {
            "pageSize" : {"required": True, "type" : "integer", "min": 1, "max": 50},
            "offset": {"type" : "integer"}
        }

    v.validate(query_params, schema)
    return erros_print(v)


# ___________________________________BLOCKCHAIN_________________________________________


def generate_litecoin_wallet(query_params):
    if query_params != {}:
        query_schema = {
                "mnemonic": {"type" : "string", "maxlength": 500},
            }

        v.validate(query_params, query_schema)

def generate_wallet(query_params):
    if query_params != {}:
        query_schema = {
                "index": {"type" : "integer"},
            }

        v.validate(query_params, query_schema)

def generate_deposit_address_from_extended_public_key(path_params):
    path_schema = {
            "xpub": {"required": True, "type" : "string"},
            "index": {"required": True, "type" : "integer", "min": 0}
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def generate_private_key(body_params):
    body_schema = {
            "mnemonic": {"required": True, "type" : "string", "minlength": 1, "maxlength": 500},
            "index": {"required": True, "type" : "integer", "max": 4294967295}
        }

    v.validate(body_params, body_schema)
    erros_print(v)

def get_block_hash(path_params):
    path_schema = {
            "i": {"required": True, "type" : "number"},
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def ethereum_get_block_hash(path_params):
    path_schema = {
            "hash": {"required": True, "type" : "string"},
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def get_block_by_hash_or_height(path_params):
    path_schema = {
            "hash": {"required": True, "type" : "string"},
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def get_transaction_by_address(path_params, query_params):
    page_size_query_params(query_params)
    path_schema = {
            "address": {"required": True, "type" : "string"},
        }

    v.validate(path_params, path_schema)
    erros_print(v)


def get_utxo_of_transaction(path_params):
    path_schema = {
            "hash": {"required": True, "type" : "string", "minlength": 64, "maxlength": 64},
            "index": {"required": True, "type" : "number", "min": 0}
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def send_bitcoin_to_blockchain_addresses(body_params):
    body_schema = {
            "fromAddress": {"type": "list", 
                            "schema": {"type": "dict", 
                                        "schema": 
                                        {"signatureId": {"type": "string", "minlength": 64, "maxlength": 128}, 
                                        "address": {"required": True, "type": "string", "minlength": 30, "maxlength": 50}, "privateKey": {"type": "string", "minlength": 52, "maxlength": 52}}}},

            "fromUTXO": {"type": "list", 
                        "schema": {"type": "dict", 
                                    "schema": 
                                    {"txHash": {"required": True, "type": "string", "minlength": 64, "maxlength": 64}, 
                                    "index": {"required": True, "type": "number", "min": 0, "max": 4294967295}, 
                                    "privateKey": {"type": "string", "minlength": 52, "maxlength": 52}, 
                                    "signatureId": {"type": "string", "minlength": 64, "maxlength": 128}}}},

            "to": {"required": True, "type": "list", "schema": {"type": "dict", "schema": {"address": {"required": True, "type": "string", "minlength": 30, "maxlength": 60}, "value": {"required": True, "type": "number", "min": 0}}}}

            }
    v.validate(body_params, body_schema)
    erros_print(v)

def broadcast_signed_transaction(body_params):
    body_schema = {
            "txData": {"required": True, "type" : "string", "minlength": 1, "maxlength": 500000},
            "signatureId": {"type" : "string", "minlength": 24, "maxlength": 24},
        }
    v.validate(body_params, body_schema)
    erros_print(v)

def get_ethereum_account_balance(path_params):
    path_schema = {
            "address": {"required": True, "type" : "string"},
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def get_ethereum_erc20_account_balance(path_params, query_params):
    path_schema = {
            "address": {"required": True, "type" : "string"},
        }

    v.validate(path_params, path_schema)
    erros_print(v)

    if query_params != {}:
        query_schema = {
                "currency": {"type" : "string"},
                "contractAddress": {"type" : "string", "minlength": 42, "maxlength": 42},
            }

        v.validate(query_params, query_schema)
        erros_print(v)

        currencies = ["USDT", "LEO", "LINK", "FREE", "MKR", "USDC", "BAT", "TUSD", "PAX", "PAXG", "PLTC", "MMY", "XCON"]
        if 'currency' in query_params.keys():
            check_correct_value_from_define_list(currencies, 'currency', query_params['currency'])

def get_count_of_outgoing_ethereum_transactions(path_params):
    path_schema = {
            "address": {"required": True, "type" : "string", "minlength": 42, "maxlength": 42 },
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def bitcoin_cash_get_block_hash(path_params):
    path_schema = {
            "hash": {"required": True, "type" : "string"},
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def get_bitcoin_cash_transaction_by_address(path_params, query_params):
    path_schema = {
            "address": {"required": True, "type" : "string"},
        }

    v.validate(path_params, path_schema)
    erros_print(v)
    if query_params != {}:
        query_schema = {
                "skip": {"type" : "integer"},
            }

        v.validate(query_params, query_schema)
        erros_print(v)

def send_bitcoin_cash_to_blockchain_addresses(body_params):
    body_schema = {
            "fromUTXO": {"type": "list", 
                        "schema": {"type": "dict", 
                                    "schema": 
                                    {"txHash": {"required": True, "type": "string", "minlength": 64, "maxlength": 64}, 
                                    "index": {"required": True, "type": "number", "min": 0, "max": 4294967295}, 
                                    "privateKey": {"type": "string", "minlength": 52, "maxlength": 52}, 
                                    "signatureId": {"type": "string", "minlength": 64, "maxlength": 128}}}},

            "to": {"required": True, "type": "list", "schema": {"type": "dict", "schema": {"address": {"required": True, "type": "string", "minlength": 30, "maxlength": 60}, "value": {"required": True, "type": "number", "min": 0}}}}

            }
    v.validate(body_params, body_schema)
    erros_print(v)

def get_account_transactions(path_params, query_params):
    path_schema = {
            "account": {"required": True, "type" : "string"},
        }

    v.validate(path_params, path_schema)
    erros_print(v)
    if query_params != {}:
        query_schema = {
                "min": {"type" : "number"},
                "marker": {"type" : "string"},
            }

        v.validate(query_params, query_schema)
        erros_print(v)

def get_ledger(path_params):
    path_schema = {
            "i": {"required": True, "type" : "number", 'min': 0},
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def get_account_info(path_params):
    path_schema = {
            "account": {"required": True, "type" : "string"},
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def send_xrp_to_blockchain_addresses(body_params):
    body_schema = {
            "fromAccount": {"required": True, "type" : "string", "minlength": 33, "maxlength": 34},
            "to": {"required": True, "type" : "string", "minlength": 33, "maxlength": 34},
            "amount": {"required": True, "type" : "string"},
            "fromSecret": {"type" : "string", "minlength": 29, "maxlength": 29},
            "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
            "fee": {"type" : "string"},
            "sourceTag": {"type" : "integer"},
            "destinationTag": {"type" : "integer"},
            "issuerAccount": {"type" : "string", "minlength": 33, "maxlength": 34},
            "token": {"type" : "string", "minlength": 40, "maxlength": 40}
        }

    v.validate(body_params, body_schema)
    erros_print(v)
    if 'fee' in body_params.keys():
        check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'fee', body_params['fee'])
    check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])
    if 'token' in body_params.keys():
        check_allowed_chars('^[A-F0-9]{40}$', 'token', body_params['token'])

def create_update_delete_xrp_trust_line(body_params):
    body_schema = {
            "fromAccount": {"required": True, "type" : "string", "minlength": 33, "maxlength": 34},
            "issuerAccount": {"required": True, "type" : "string", "minlength": 33, "maxlength": 34},
            "limit": {"required": True, "type" : "string"},
            "token": {"required": True, "type" : "string", "minlength": 40, "maxlength": 40},
            "fromSecret": {"type" : "string", "minlength": 29, "maxlength": 29},
            "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
            "fee": {"type" : "string"}
        }

    v.validate(body_params, body_schema)
    erros_print(v)
    if 'fee' in body_params.keys():
        check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'fee', body_params['fee'])
    check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'limit', body_params['limit'])
    check_allowed_chars('^[A-F0-9]{40}$', 'token', body_params['token'])

def modify_xrp_account(body_params):
    body_schema = {
            "fromAccount": {"required": True, "type" : "string", "minlength": 33, "maxlength": 34},
            "fromSecret": {"type" : "string", "minlength": 29, "maxlength": 29},
            "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
            "fee": {"type" : "string"},
            "rippling": {"type" : "boolean"},
            "requireDestinationTag": {"type" : "boolean"}
        }

    v.validate(body_params, body_schema)
    erros_print(v)
    if 'fee' in body_params.keys():
        check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'fee', body_params['fee'])

def send_xlm_from_address_to_address(body_params):
    body_schema = {
            "fromAccount": {"required": True, "type" : "string", "minlength": 56, "maxlength": 56},
            "to": {"required": True, "type" : "string", "minlength": 56, "maxlength": 56},
            "amount" : {"required": True, "type" : "string"},
            "fromSecret": {"type" : "string", "minlength": 56, "maxlength": 56},
            "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
            "initialize": {"type": "boolean"},
            "message":{"type" : "string","maxlength": 64},
            "issuerAccount": {"type" : "string", "minlength": 56, "maxlength": 56},
            "token": {"type" : "string", "minlength": 1, "maxlength": 12}
        }
    v.validate(body_params, body_schema)
    erros_print(v)
    check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])
    if 'message' in body_params.keys():
        check_allowed_chars('^[ -~]{0,64}$', 'message', body_params['message'])
    if 'token' in body_params.keys():
        check_allowed_chars('^[a-zA-Z0-9]{1,12}$', 'token', body_params['token'])

def create_update_delete_xlm_trust_line(body_params):
    body_schema = {
            "fromAccount": {"required": True, "type" : "string", "minlength": 56, "maxlength": 56},
            "issuerAccount": {"required": True, "type" : "string", "minlength": 56, "maxlength": 56},
            "limit": {"type" : "string"},
            "token": {"required": True, "type" : "string", "minlength": 1, "maxlength": 12},
            "fromSecret": {"type" : "string", "minlength": 56, "maxlength": 56},
            "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
            "fee": {"type" : "string"}
        }

    v.validate(body_params, body_schema)
    erros_print(v)
    if 'fee' in body_params.keys():
        check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'fee', body_params['fee'])
    if 'limit' in body_params.keys():
        check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'limit', body_params['limit'])
    check_allowed_chars('^[a-zA-Z0-9]{1,12}$', 'token', body_params['token'])

def send_ethereum_erc20_from_account_to_account(body_params):
    body_schema = {
            "data": {"type" : "string", "maxlength": 50000},
            "nonce": {"type" : "string",  "minlength": 0},
            "to": {"required": True, "type" : "string", "minlength": 42, "maxlength": 42},
            "currency": {"required": True, "type" : "string"},
            "fee": {"type" : "dict", 'schema': {'gasLimit': {"required": True, "type" : "string"}, 'gasPrice': {"required": True, "type" : "string"}}},
            "amount": {"required": True, "type" : "string"},
            "fromPrivateKey": {"type" : "string", "minlength": 66, "maxlength": 66},
            "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
        }

    v.validate(body_params, body_schema)
    erros_print(v)
    currencies = ["USDT", "LEO", "LINK", "FREE", "MKR", "USDC", "BAT", "TUSD", "PAX", "PAXG", "PLTC", "MMY", "XCON", "ETH"]
    check_correct_value_from_define_list(currencies, 'currency', body_params['currency'])
    check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])
    check_allowed_chars('^[+]?\d+$', 'gasLimit', body_params['fee']['gasLimit'])
    check_allowed_chars('^[+]?\d+$', 'gasPrice', body_params['fee']['gasPrice'])

def invoke_smart_contract_method(body_params):
    body_schema = {
            "contractAddress": {"required": True, "type" : "string", "minlength": 42, "maxlength": 42},
            "methodName": {"required": True, "type" : "string", "minlength": 1, "maxlength": 500},
            "methodABI": {"required": True, "type" : "dict"},
            "params": {"required": True, "type" : "dict"},
            "fromPrivateKey": {"type" : "string", "minlength": 66, "maxlength": 66},
            "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
            "nonce": {"type" : "string",  "minlength": 0},
            "fee": {"type" : "dict", 'schema': {'gasLimit': {"required": True, "type" : "string"}, 'gasPrice': {"required": True, "type" : "string"}}}
        }
    v.validate(body_params, body_schema)
    erros_print(v)
    if 'fee' in body_params.keys():
        check_allowed_chars('^[+]?\d+$', 'gasLimit', body_params['fee']['gasLimit'])
        check_allowed_chars('^[+]?\d+$', 'gasPrice', body_params['fee']['gasPrice'])

def deploy_ethereum_erc20_smart_contract(body_params):
    body_schema = {
        "symbol": {"required": True, "type" : "string", "minlength": 1, "maxlength": 30},
        "name": {"required": True, "type" : "string", "minlength": 1, "maxlength": 100},
        "supply": {"required": True, "type" : "string", "maxlength": 38},
        "digits": {"required": True, "type" : "number", "min": 1, "max": 30},
        "address": {"required": True, "type" : "string", "minlength": 42, "maxlength": 42},
        "fromPrivateKey": {"type" : "string", "minlength": 66, "maxlength": 66},
        "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
        "nonce": {"type" : "string",  "minlength": 0},
        "fee": {"type" : "dict", 'schema': {'gasLimit': {"required": True, "type" : "string"}, 'gasPrice': {"required": True, "type" : "string"}}},
    }

    v.validate(body_params, body_schema)
    erros_print(v)
    check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'supply', body_params['supply'])    
    check_allowed_chars('^[a-zA-Z0-9_]+$', 'name', body_params['name'])
    if 'fee' in body_params.keys():
        check_allowed_chars('^[+]?\d+$', 'gasLimit', body_params['fee']['gasLimit'])
        check_allowed_chars('^[+]?\d+$', 'gasPrice', body_params['fee']['gasPrice'])

def transfer_ethereum_erc20(body_params):
    body_schema = {
        "to": {"required": True, "type" : "string", "minlength": 1, "maxlength": 50},
        "amount": {"required": True, "type" : "string"},
        "contractAddress": {"required": True, "type" : "string", "minlength": 42, "maxlength": 42},
        "digits": {"required": True, "type" : "number", "min": 1, "max": 30},
        "fromPrivateKey": {"type" : "string", "minlength": 66, "maxlength": 66},
        "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
        "nonce": {"type" : "string",  "minlength": 0},
        "fee": {"type" : "dict", 'schema': {'gasLimit': {"required": True, "type" : "string"}, 'gasPrice': {"required": True, "type" : "string"}}}
    }

    v.validate(body_params, body_schema)
    erros_print(v)
    check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])

    if 'fee' in body_params.keys():
        check_allowed_chars('^[+]?\d+$', 'gasLimit', body_params['fee']['gasLimit'])
        check_allowed_chars('^[+]?\d+$', 'gasPrice', body_params['fee']['gasPrice'])


def deploy_ethereum_erc721_smart_contract(body_params):
    body_schema = {
            "name": {"required": True, "type" : "string", "minlength": 1, "maxlength": 100},
            "symbol": {"required": True, "type" : "string", "minlength": 1, "maxlength": 30},
            "fromPrivateKey": {"type" : "string", "minlength": 66, "maxlength": 66},
            "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
            "nonce": {"type" : "string",  "minlength": 0},
            "fee": {"type" : "dict", 'schema': {'gasLimit': {"required": True, "type" : "string"}, 'gasPrice': {"required": True, "type" : "string"}}}
        }

    v.validate(body_params, body_schema)
    erros_print(v)
    check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'supply', body_params['supply'])    
    check_allowed_chars('^[a-zA-Z0-9_]+$', 'name', body_params['name'])
    if 'fee' in body_params.keys():
        check_allowed_chars('^[+]?\d+$', 'gasLimit', body_params['fee']['gasLimit'])
        check_allowed_chars('^[+]?\d+$', 'gasPrice', body_params['fee']['gasPrice'])

def mint_ethereum_erc721(body_params):
    body_schema = {
            "tokenId": {"required": True, "type" : "string", "maxlength": 32},
            "to": {"required": True, "type" : "string", "minlength": 42, "maxlength": 42},
            "contractAddress": {"required": True, "type" : "string", "minlength": 42, "maxlength": 42},
            "url": {"required": True, "type" : "string", "maxlength": 256},
            "fromPrivateKey": {"type" : "string", "minlength": 66, "maxlength": 66},
            "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
            "nonce": {"type" : "number",  "min": 0},
            "fee": {"type" : "dict", 'schema': {'gasLimit': {"required": True, "type" : "string"}, 'gasPrice': {"required": True, "type" : "string"}}}
        }

    v.validate(body_params, body_schema)
    erros_print(v)
    if 'fee' in body_params.keys():
        check_allowed_chars('^[+]?\d+$', 'gasLimit', body_params['fee']['gasLimit'])
        check_allowed_chars('^[+]?\d+$', 'gasPrice', body_params['fee']['gasPrice'])

def transfer_ethereum_erc721_token(body_params):
    body_schema = {
            "to": {"required": True, "type" : "string", "minlength": 42, "maxlength": 42},
            "tokenId": {"required": True, "type" : "string", "maxlength": 256},
            "contractAddress": {"required": True, "type" : "string", "minlength": 42, "maxlength": 42},
            "fromPrivateKey": {"type" : "string", "minlength": 66, "maxlength": 66},
            "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
            "nonce": {"type" : "number"},
            "fee": {"type" : "dict", 'schema': {'gasLimit': {"required": True, "type" : "string"}, 'gasPrice': {"required": True, "type" : "string"}}}
        }

    v.validate(body_params, body_schema)
    erros_print(v)
    if 'fee' in body_params.keys():
        check_allowed_chars('^[+]?\d+$', 'gasLimit', body_params['fee']['gasLimit'])
        check_allowed_chars('^[+]?\d+$', 'gasPrice', body_params['fee']['gasPrice'])

def mint_ethereum_erc721_multiple_tokens(body_params):
    body_schema = {
            "to": {"required": True, "type" : "list"},
            "tokenId": {"required": True, "type" : "list"},
            "contractAddress": {"required": True, "type" : "string", "minlength": 42, "maxlength": 42},
            "fromPrivateKey": {"type" : "string", "minlength": 66, "maxlength": 66},
            "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
            "nonce": {"type" : "number",  "min": 0},
            "fee": {"type" : "dict", 'schema': {'gasLimit': {"required": True, "type" : "string"}, 'gasPrice': {"required": True, "type" : "string"}}}
        }

    v.validate(body_params, body_schema)
    erros_print(v)
    if 'fee' in body_params.keys():
        check_allowed_chars('^[+]?\d+$', 'gasLimit', body_params['fee']['gasLimit'])
        check_allowed_chars('^[+]?\d+$', 'gasPrice', body_params['fee']['gasPrice'])

def burn_ethereum_erc721(body_params):
    body_schema = {
            "tokenId": {"required": True, "type" : "string", "maxlength": 32},
            "contractAddress": {"required": True, "type" : "string", "minlength": 42, "maxlength": 42},
            "fromPrivateKey": {"type" : "string", "minlength": 66, "maxlength": 66},
            "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
            "nonce": {"type" : "number"},
            "fee": {"type" : "dict", 'schema': {'gasLimit': {"required": True, "type" : "string"}, 'gasPrice': {"required": True, "type" : "string"}}}
        }

    v.validate(body_params, body_schema)
    erros_print(v)
    if 'fee' in body_params.keys():
        check_allowed_chars('^[+]?\d+$', 'gasLimit', body_params['fee']['gasLimit'])
        check_allowed_chars('^[+]?\d+$', 'gasPrice', body_params['fee']['gasPrice'])

def get_ethereum_erc721_account_balance(path_params):
    path_schema = {
        "address": {"required": True, "type" : "string"},
        "contractAddress": {"required": True, "type" : "string"},
    }

    v.validate(path_params, path_schema)
    erros_print(v)

def get_ethereum_erc721_token(path_params):
    path_schema = {
        "address": {"required": True, "type" : "string"},        
        "index": {"required": True, "type" : "number"},
        "contractAddress": {"required": True, "type" : "string"},
    }
    v.validate(path_params, path_schema)
    erros_print(v)

def get_ethereum_erc721_token_metadata(path_params):
    path_schema = {
        "token": {"required": True, "type" : "string", "maxlength": 32},        
        "contractAddress": {"required": True, "type" : "string"},
    }
    v.validate(path_params, path_schema)
    erros_print(v)