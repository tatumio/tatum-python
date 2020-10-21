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

# ___________________________________LEDGER/ACCOUNT_______________________________________
def create_new_account(body_params):
    body_schema = {
            "currency" : {"required": True, "type" : "string", "minlength": 2, "maxlength": 40},
            "xpub": {"type" : "string", "minlength": 1, "maxlength": 150},
            "customer": {"type" : "dict", "schema": {'externalId': {"required": True, "type" : "string", "minlength": 1, "maxlength": 100}, "providerCountry": {"type" : "string", "minlength": 2, "maxlength": 2}, "customerCountry": {"type" : "string", "minlength": 2, "maxlength": 2},           "accountingCurrency": {"type" : "string", "minlength": 3, "maxlength": 3} }},
            "compliant": {"type": "boolean"},
            "accountCode": {"type" : "string", "minlength": 1, "maxlength": 150},
            "accountingCurrency": {"type" : "string", "minlength": 3, "maxlength": 3}
        }
    v.validate(body_params, body_schema)
    return erros_print(v)

def list_all_customer_accounts(path_params, query_params):
    return id_path_param(path_params) & page_size_query_params(query_params) & True

def block_amount_on_account(path_params, body_params):
    result = True
    result = result & id_path_param(path_params)
    body_schema = {
            "amount" : {"required": True, "type" : "string", "maxlength": 38},
            "type" : {"required": True, "type" : "string", "minlength": 1, "maxlength": 100},
            "description" : {"type" : "string", "minlength": 1, "maxlength": 300}
        }
    v.validate(body_params, body_schema)
    result = result & erros_print(v)
    if result:
        result = result & check_allowed_chars('^^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])
        return  result
    

def unlock_amount_on_account_and_perform_transaction(path_params, body_params):
    result = True
    result = result & id_path_param(path_params)
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
    result = result & erros_print(v)
    if result:
        result = result & check_allowed_chars('^^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])
        return result



def get_blocked_amounts_on_account(path_params, query_params):
    return id_path_param(path_params) & page_size_query_params(query_params)

# ___________________________________LEDGER/TRANSACTION____________________________________

def send_payment(body_params):
    result = True
    body_schema = {
            "senderAccountId" : {"required": True, "type" : "string", "minlength": 24, "maxlength": 24},
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
    result = result & erros_print(v)
    if result:
        result = result & check_allowed_chars('^^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])
        return result


def find_transactions_for_account(query_params, body_params):
    result = True
    query_schema = {
            "pageSize" : {"required": True, "type" : "integer", "min": 1, "max": 50},
            "offset": {"type" : "integer"},
            "count": {"type" : "string"}
        }

    v.validate(query_params, query_schema)
    result = result & erros_print(v)

    body_schema = {
            "id" : {"required": True, "type" : "string", "minlength": 24, "maxlength": 24},
            "counterAccount" : {"type" : "string", "minlength": 24, "maxlength": 24},
            "from" : {"type" : "integer", "min": 0},
            "to" : {"type" : "integer", "min": 0},
            "currency" : {"type" : "string", "minlength": 1, "maxlength": 50},
            "transactionType" : {"type" : "string"},
            "opType" : {"type" : "string"},
            "transactionCode":{"type" : "string","minlength": 1, "maxlength": 100},
            "paymentId":{"type" : "string","minlength": 1, "maxlength": 100},
            "recipientNote":{"type" : "string","minlength": 1, "maxlength": 500},
            "senderNote":{"type" : "string","minlength": 1, "maxlength": 500},
        }

    v.validate(body_params, body_schema)
    result = result & erros_print(v)
    if result:
        transactionType = ["FAILED", "DEBIT_PAYMENT", "CREDIT_PAYMENT", "CREDIT_DEPOSIT", "DEBIT_WITHDRAWAL", "CANCEL_WITHDRAWAL", "DEBIT_OUTGOING_PAYMENT", "EXCHANGE_BUY", "EXCHANGE_SELL", "DEBIT_TRANSACTION", "CREDIT_INCOMING_PAYMENT"]
        if 'transactionType' in body_params.keys():
            result = result & check_correct_value_from_define_list(transactionType, 'transactionType', body_params['transactionType'])

        opTypes = ["PAYMENT", "WITHDRAWAL", "BLOCKCHAIN_TRANSACTION", "EXCHANGE", "FAILED", "DEPOSIT", "MINT", "REVOKE"]
        if 'opType' in body_params.keys():
            result = result & check_correct_value_from_define_list(opTypes, 'opType', body_params['opType'])
        return result

def find_transactions_for_customer_across_all_accounts_of_customer(query_params, body_params):
    result = True
    query_schema = {
            "pageSize" : {"required": True, "type" : "integer", "min": 1, "max": 50},
            "offset": {"type" : "integer"},
            "count": {"type" : "string"}
        }

    v.validate(query_params, query_schema)
    result = result & erros_print(v)

    body_schema = {
            "id" : {"required": True, "type" : "string", "minlength": 24, "maxlength": 24},
            "account" : {"type" : "string", "minlength": 24, "maxlength": 24},
            "counterAccount" : {"type" : "string", "minlength": 24, "maxlength": 24},
            "from" : {"type" : "integer", "min": 0},
            "to" : {"type" : "integer", "min": 0},
            "currency" : {"type" : "string", "minlength": 1, "maxlength": 50},
            "transactionType" : {"type" : "string"},
            "opType" : {"type" : "string"},
            "transactionCode":{"type" : "string","minlength": 1, "maxlength": 100},
            "paymentId":{"type" : "string","minlength": 1, "maxlength": 100},
            "recipientNote":{"type" : "string","minlength": 1, "maxlength": 500},
            "senderNote":{"type" : "string","minlength": 1, "maxlength": 500},
        }

    v.validate(body_params, body_schema)
    result = result & erros_print(v)
    if result:
        transactionType = ["FAILED", "DEBIT_PAYMENT", "CREDIT_PAYMENT", "CREDIT_DEPOSIT", "DEBIT_WITHDRAWAL", "CANCEL_WITHDRAWAL", "DEBIT_OUTGOING_PAYMENT", "EXCHANGE_BUY", "EXCHANGE_SELL", "DEBIT_TRANSACTION", "CREDIT_INCOMING_PAYMENT"]
        if 'transactionType' in body_params.keys():
            result = result & check_correct_value_from_define_list(transactionType, 'transactionType', body_params['transactionType'])

        opTypes = ["PAYMENT", "WITHDRAWAL", "BLOCKCHAIN_TRANSACTION", "EXCHANGE", "FAILED", "DEPOSIT", "MINT", "REVOKE"]
        if 'opType' in body_params.keys():
            result = result & check_correct_value_from_define_list(opTypes, 'opType', body_params['opType'])
        return result

def find_transactions_for_ledger(query_params, body_params):
    result = True
    query_schema = {
            "pageSize" : {"required": True, "type" : "integer", "min": 1, "max": 50},
            "offset": {"type" : "integer"},
            "count": {"type" : "string"}
        }

    v.validate(query_params, query_schema)
    result = result & erros_print(v)

    body_schema = {
            "account" : {"type" : "string", "minlength": 24, "maxlength": 24},
            "counterAccount" : {"type" : "string", "minlength": 24, "maxlength": 24},
            "from" : {"type" : "integer", "min": 0},
            "to" : {"type" : "integer", "min": 0},
            "currency" : {"type" : "string", "minlength": 1, "maxlength": 50},
            "transactionType" : {"type" : "string"},
            "opType" : {"type" : "string"},
            "transactionCode":{"type" : "string","minlength": 1, "maxlength": 100},
            "paymentId":{"type" : "string","minlength": 1, "maxlength": 100},
            "recipientNote":{"type" : "string","minlength": 1, "maxlength": 500},
            "senderNote":{"type" : "string","minlength": 1, "maxlength": 500},
        }

    v.validate(body_params, body_schema)
    result = result & erros_print(v)
    if result:
        transactionType = ["FAILED", "DEBIT_PAYMENT", "CREDIT_PAYMENT", "CREDIT_DEPOSIT", "DEBIT_WITHDRAWAL", "CANCEL_WITHDRAWAL", "DEBIT_OUTGOING_PAYMENT", "EXCHANGE_BUY", "EXCHANGE_SELL", "DEBIT_TRANSACTION", "CREDIT_INCOMING_PAYMENT"]
        if 'transactionType' in body_params.keys():
            result = result & check_correct_value_from_define_list(transactionType, 'transactionType', body_params['transactionType'])

        opTypes = ["PAYMENT", "WITHDRAWAL", "BLOCKCHAIN_TRANSACTION", "EXCHANGE", "FAILED", "DEPOSIT", "MINT", "REVOKE"]
        if 'opType' in body_params.keys():
            result = result & check_correct_value_from_define_list(opTypes, 'opType', body_params['opType'])
        return result

def find_transactions_with_given_reference_across_all_accounts(path_params):
    path_schema = {
            "reference" : {"required": True, "type" : "string", "minlength": 20, "maxlength": 100}
        }

    v.validate(path_params, path_schema)
    return erros_print(v)

# ___________________________________LEDGER/CUSTOMER_______________________________________

def update_customer(path_params, body_params):
    result = True
    result = result & id_path_param(path_params)
    body_schema = {
        "externalId": {"required": True, "type" : "string", "minlength": 1, "maxlength": 100}, "providerCountry": {"type" : "string", "minlength": 2, "maxlength": 2}, 
        "customerCountry": {"type" : "string", "minlength": 2, "maxlength": 2},           "accountingCurrency": {"type" : "string", "minlength": 3, "maxlength": 3} }

    v.validate(body_params, body_schema)
    result = result & erros_print(v)
    return result

# ___________________________________LEDGER/VIRTUAL CURRENCY_______________________________
def check_prefix_virtual_currency(name):
    if name[:3] != 'VC_':
        print(colored('Virtual currency name must be prefixed with "VC_".', 'red'))
        return False
    else: 
        return True

def create_new_vitual_currency(body_params):
    result = True
    body_schema = {
            "name" : {"required": True, "type" : "string", "minlength": 1, "maxlength": 30},
            "supply" : {"required": True, "type" : "string", "minlength": 1, "maxlength": 38},
            "basePair" : {"required": True, "type" : "string", "minlength": 3, "maxlength": 5},
            "baseRate" : {"type" : "number", "min": 0},
            "customer": {"type" : "dict", "schema": {'externalId': {"required": True, "type" : "string", "minlength": 1, "maxlength": 100}, "providerCountry": {"type" : "string", "minlength": 2, "maxlength": 2}, "customerCountry": {"type" : "string", "minlength": 2, "maxlength": 2},"accountingCurrency": {"type" : "string", "minlength": 3, "maxlength": 3} }},
            "description":{"type" : "string", "minlength": 1, "maxlength": 100},
            "accountCode":{"type" : "string", "minlength": 1, "maxlength": 50},
            "accountNumber":{"type" : "string"},
            "accountingCurrency":{"type" : "string", "minlength": 3, "maxlength": 3}
        }

    v.validate(body_params, body_schema)
    result = result & erros_print(v)
    if result:
        result = result & check_prefix_virtual_currency(body_params['name'])
        result = result & check_allowed_chars('^[a-zA-Z0-9_]+$', 'name', body_params['name'][3:])
        result = result & check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'supply', body_params['supply'])   
        return result
    

def update_vitual_currency(body_params):
    result = True
    body_schema = {
            "name" : {"required": True, "type" : "string", "minlength": 1, "maxlength": 30},
            "basePair" : {"type" : "string", "minlength": 3, "maxlength": 5},
            "baseRate" : {"type" : "number", "min": 0},
        }

    v.validate(body_params, body_schema)
    result = result & erros_print(v)
    if result:
        result = result & check_prefix_virtual_currency(body_params['name'])
        result = result & check_allowed_chars('^[a-zA-Z0-9_]+$', 'name', body_params['name'][3:])
        return result


def get_virtual_currency(path_params):
    path_schema = {
            "name" : {"required": True, "type" : "string", "minlength": 3, "maxlength": 100}
        }
    v.validate(path_params, path_schema)
    return erros_print(v)

def create_new_supply_of_virtual_currency(body_params):
    result = True
    body_schema = {
            "accountId" : {"required": True, "type" : "string", "minlength": 24, "maxlength": 24},
            "amount" : {"required": True, "type" : "string", "maxlength": 38},
            "paymentId" : {"type" : "string", "minlength": 1, "maxlength": 100},
            "reference" : {"type" : "string", "minlength": 1, "maxlength": 100},
            "transactionCode" : {"type" : "string", "minlength": 1, "maxlength": 100},
            "recipientNote" : {"type" : "string", "minlength": 1, "maxlength": 500},
            "counterAccount" : {"type" : "string", "minlength": 24, "maxlength": 24},
            "senderNote" : {"type" : "string", "minlength": 1, "maxlength": 500}
        }

    v.validate(body_params, body_schema)
    result = result & erros_print(v)
    if result:
        result = result & check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])
        return result


# ___________________________________LEDGER/SUBSCRIPTION___________________________________

def create_new_subcription(body_params):
    result = True
    body_schema = {
            "type" : {"required": True, "type" : "string"},
            "attr" : {"required": True, "type" : "dict", "schema": {'limit': {"required": True, "type" : "string", "maxlength": 38}, 'typeOfBalance': {"required": True, "type" : "string", "maxlength": 38}}
            }
         }

    v.validate(body_params, body_schema)
    result = result & erros_print(v)
    if result:
        types = ["ACCOUNT_BALANCE_LIMIT", "OFFCHAIN_WITHDRAWAL", "TRANSACTION_HISTORY_REPORT", "ACCOUNT_INCOMING_BLOCKCHAIN_TRANSACTION", "COMPLETE_BLOCKCHAIN_TRANSACTION"]
        result = result & check_correct_value_from_define_list(types, 'type', body_params['type'])

        result = result & check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'limit', body_params['attr']['limit'])

        typeOfBalance = ["account", "available"]
        result = result & check_correct_value_from_define_list(typeOfBalance, 'typeOfBalance', body_params['attr']['typeOfBalance'])
        return result


# ___________________________________LEDGER/ORDER BOOK_____________________________________

def list_all_active_buy_trades(query_params):
    query_schema = {
            "id": {"type" : "string"},
            "pageSize" : {"required": True, "type" : "integer", "min": 1, "max": 50},
            "offset": {"type" : "integer"}
        }

    v.validate(query_params, query_schema)
    return erros_print(v)

def store_buy_sell_trade(body_params):
    result = True
    body_schema = {
            "type": {"required": True, "type" : "string"},
            "price" : {"required": True, "type" : "string", "maxlength": 38},
            "amount" : {"required": True, "type" : "string", "maxlength": 38},
            "pair" : {"required": True, "type" : "string", "minlength": 3, "maxlength": 30},
            "currency1AccountId" : {"required": True, "type" : "string", "minlength": 24, "maxlength": 24},
            "currency2AccountId" : {"required": True, "type" : "string", "minlength": 24, "maxlength": 24},
        }

    v.validate(body_params, body_schema)
    result = result & erros_print(v)
    if result:
        types = ["BUY", "SELL"]
        result = result & check_correct_value_from_define_list(types, 'type', body_params['type'])
        result = result & check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'price', body_params['price'])
        result = result & check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])
        result = result & check_allowed_chars('^[A-a-zZ0-9_\-]+\/[A-Za-z0-9_\-]+$', 'pair', body_params['pair'])

        return result