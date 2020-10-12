import cerberus
from termcolor import colored

def erros_print(v):
    if v.errors != {}:
        print(colored(v.errors, 'red'))

def id_path_param(path_params):
    v = cerberus.Validator()
    path_schema = {
            "id" : {"required": True, "type" : "string"}
        }

    v.validate(path_params, path_schema)
    erros_print(v)


def create_new_account(body_params):
    v = cerberus.Validator()
    body_schema = {
            "currency" : {"required": True, "type" : "string", "minlength": 2, "maxlength": 40},
            "xpub": {"type" : "string", "minlength": 1, "maxlength": 150},
            "customer": {"type" : "dict", "schema": {'externalId': {"required": True, "type" : "string", "minlength": 1, "maxlength": 100}, "providerCountry": {"type" : "string", "minlength": 2, "maxlength": 2}, "customerCountry": {"type" : "string", "minlength": 2, "maxlength": 2},           "accountingCurrency": {"type" : "string", "minlength": 3, "maxlength": 3} }},
            "compliant": {"type": "boolean"},
            "accountCode": {"type" : "string", "minlength": 1, "maxlength": 150},
            "accountingCurrency": {"type" : "string", "minlength": 3, "maxlength": 3}
        }

    v.validate(body_params, body_schema)
    erros_print(v)


def list_all_accounts(query_params):
    v = cerberus.Validator()
    schema = {
            "pageSize" : {"required": True, "type" : "integer", "min": 1, "max": 50},
            "offset": {"type" : "integer"}
        }

    v.validate(query_params, schema)
    erros_print(v)

def list_all_customer_accounts(path_params, query_params):
    v = cerberus.Validator()
    id_path_param(path_params)

    query_schema = {
            "pageSize" : {"required": True, "type" : "integer", "min": 1, "max": 50},
            "offset": {"type" : "integer"}
        }

    v.validate(query_params, query_schema)
    erros_print(v)

def block_amount_on_account(path_params, body_params):
    v = cerberus.Validator()
    id_path_param(path_params)

    body_schema = {
            "amount" : {"required": True, "type" : "string", "maxlength": 38},
            "type" : {"required": True, "type" : "string", "minlength": 1, "maxlength": 100},
            "description" : {"type" : "string", "minlength": 1, "maxlength": 300}
        }

    v.validate(body_params, body_schema)
    erros_print(v)

    not_allowed_chars = '^[+]?((\d+(\.\d*)?)|(\.\d+))$'
    for i in range(len(not_allowed_chars)-1):
        if not_allowed_chars[i] in body_params['amount']:
            print(colored("{'amount': contains not allowed characters}", 'red'))
            break

def unlock_amount_on_account_and_perform_transaction(path_params, body_params):
    v = cerberus.Validator()
    id_path_param(path_params)
    body_schema = {
            "recipientAccountId" : {"required": True, "type" : "string", "minlength": 24, "maxlength": 24},
            "amount" : {"required": True, "type" : "string", "maxlength": 38},
            "anonymous" : {"type" : "boolean"},
            "compliant" : {"type" : "boolean"},
            "transactionCode":{"type" : "string","minlength": 1, "maxlength": 100},
            "paymentId":{"type" : "string","minlength": 1, "maxlength": 100},
            "recipientNote":{"type" : "string","minlength": 1, "maxlength": 500},
            "baseRate":{"type" : "number","min": 0},
            "senderNote":{"type" : "string","minlength": 1, "maxlength": 500},
        }

    v.validate(body_params, body_schema)
    erros_print(v)

    not_allowed_chars = '^[+]?((\d+(\.\d*)?)|(\.\d+))$'
    for i in range(len(not_allowed_chars)-1):
        if not_allowed_chars[i] in body_params['amount']:
            print(colored("{'amount': contains not allowed characters}", 'red'))
            break

def get_blocked_amounts_on_account(path_params, query_params):
    v = cerberus.Validator()
    id_path_param(path_params)
    query_schema = {
            "pageSize" : {"required": True, "type" : "integer", "min": 1, "max": 50},
            "offset": {"type" : "integer"}
        }

    v.validate(query_params, query_schema)
    erros_print(v)


