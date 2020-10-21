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

# ___________________________________SECURITY/KEY MANAGEMENT SYSTEM_____________________________________

def get_pending_transactions_to_sign(path_params):
    result = True
    path_schema = {
            "chain": {"required": True, "type" : "string"},
        }

    v.validate(path_params, path_schema)
    result = result & erros_print(v)
    if result:
        chains = ["BTC", "ETH", "XLM", "XRP", "BCH", "LTC", "VET"]
        result = result & check_correct_value_from_define_list(chains, 'chain', path_params['chain'])
        return result

def complete_pending_transaction_to_sign(path_params):
    path_schema = {
            "id": {"required": True, "type" : "string", "minlength": 24, "maxlength": 24},
            "txId": {"required": True, "type" : "string", "minlength": 10, "maxlength": 80},
        }

    v.validate(path_params, path_schema)
    return erros_print(v)

def delete_transaction(path_params, query_params):
    result = True
    result = result & id_path_param(path_params)
    query_schema = {
            "revert": {"type" : "string"},
        }

    v.validate(query_params, query_schema)
    result = result & erros_print(v)
    
    if query_params != {}:
        reverts = ["true", "false"]
        result = result & check_correct_value_from_define_list(reverts, 'revert', query_params['revert'])
    return result

# ___________________________________SECURITY/ADDRESS_____________________________________


def check_malicous_address(path_params):
    path_schema = {
            "address": {"required": True, "type" : "string"},
        }
    v.validate(path_params, path_schema)
    return erros_print(v)