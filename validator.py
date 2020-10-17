import cerberus
import re
from termcolor import colored

def erros_print(v):
    if v.errors != {}:
        print(colored(v.errors, 'red'))

def check_allowed_chars(allowed_chars, variableName, variableValue):
    match = re.search(allowed_chars, variableValue)
    if match is None:
        print(colored("'{}': contains not allowed characters".format(variableName), 'red'))


def check_correct_value_from_define_list(list, variableName, variableValue):
    correct = False
    for i in range(0, len(list)):
        if variableValue == list[i]:
            correct = True
            break
    if correct == False:
        print(colored('"{}": is not allowed type'.format(variableName), 'red'))

def id_path_param(path_params):
    v = cerberus.Validator()
    path_schema = {
            "id" : {"required": True, "type" : "string"}
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def page_size_query_params(query_params):
    v = cerberus.Validator()
    schema = {
            "pageSize" : {"required": True, "type" : "integer", "min": 1, "max": 50},
            "offset": {"type" : "integer"}
        }

    v.validate(query_params, schema)
    erros_print(v)

# ___________________________________LEDGER/ACCOUNT_______________________________________
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

def list_all_customer_accounts(path_params, query_params):
    v = cerberus.Validator()
    id_path_param(path_params)
    page_size_query_params(query_params)

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
    check_allowed_chars('^^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])
    

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

    check_allowed_chars('^^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])


def get_blocked_amounts_on_account(path_params, query_params):
    v = cerberus.Validator()
    id_path_param(path_params)
    page_size_query_params(query_params)

# ___________________________________LEDGER/TRANSACTION____________________________________

def send_payment(body_params):
    v = cerberus.Validator()
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
    erros_print(v)

    check_allowed_chars('^^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])


def find_transactions_for_account(query_params, body_params):
    v = cerberus.Validator()

    query_schema = {
            "pageSize" : {"required": True, "type" : "integer", "min": 1, "max": 50},
            "offset": {"type" : "integer"},
            "count": {"type" : "string"}
        }

    v.validate(query_params, query_schema)
    erros_print(v)

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
    erros_print(v)

    transactionType = ["FAILED", "DEBIT_PAYMENT", "CREDIT_PAYMENT", "CREDIT_DEPOSIT", "DEBIT_WITHDRAWAL", "CANCEL_WITHDRAWAL", "DEBIT_OUTGOING_PAYMENT", "EXCHANGE_BUY", "EXCHANGE_SELL", "DEBIT_TRANSACTION", "CREDIT_INCOMING_PAYMENT"]
    if 'transactionType' in body_params.keys():
        check_correct_value_from_define_list(transactionType, 'transactionType', body_params['transactionType'])

    opTypes = ["PAYMENT", "WITHDRAWAL", "BLOCKCHAIN_TRANSACTION", "EXCHANGE", "FAILED", "DEPOSIT", "MINT", "REVOKE"]
    if 'opType' in body_params.keys():
        check_correct_value_from_define_list(opTypes, 'opType', body_params['opType'])

def find_transactions_for_customer_across_all_accounts_of_customer(query_params, body_params):
    v = cerberus.Validator()

    query_schema = {
            "pageSize" : {"required": True, "type" : "integer", "min": 1, "max": 50},
            "offset": {"type" : "integer"},
            "count": {"type" : "string"}
        }

    v.validate(query_params, query_schema)
    erros_print(v)

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
    erros_print(v)

    transactionType = ["FAILED", "DEBIT_PAYMENT", "CREDIT_PAYMENT", "CREDIT_DEPOSIT", "DEBIT_WITHDRAWAL", "CANCEL_WITHDRAWAL", "DEBIT_OUTGOING_PAYMENT", "EXCHANGE_BUY", "EXCHANGE_SELL", "DEBIT_TRANSACTION", "CREDIT_INCOMING_PAYMENT"]
    if 'transactionType' in body_params.keys():
        check_correct_value_from_define_list(transactionType, 'transactionType', body_params['transactionType'])

    opTypes = ["PAYMENT", "WITHDRAWAL", "BLOCKCHAIN_TRANSACTION", "EXCHANGE", "FAILED", "DEPOSIT", "MINT", "REVOKE"]
    if 'opType' in body_params.keys():
        check_correct_value_from_define_list(opTypes, 'opType', body_params['opType'])

def find_transactions_for_ledger(query_params, body_params):
    v = cerberus.Validator()

    query_schema = {
            "pageSize" : {"required": True, "type" : "integer", "min": 1, "max": 50},
            "offset": {"type" : "integer"},
            "count": {"type" : "string"}
        }

    v.validate(query_params, query_schema)
    erros_print(v)

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
    erros_print(v)

    transactionType = ["FAILED", "DEBIT_PAYMENT", "CREDIT_PAYMENT", "CREDIT_DEPOSIT", "DEBIT_WITHDRAWAL", "CANCEL_WITHDRAWAL", "DEBIT_OUTGOING_PAYMENT", "EXCHANGE_BUY", "EXCHANGE_SELL", "DEBIT_TRANSACTION", "CREDIT_INCOMING_PAYMENT"]
    if 'transactionType' in body_params.keys():
        check_correct_value_from_define_list(transactionType, 'transactionType', body_params['transactionType'])

    opTypes = ["PAYMENT", "WITHDRAWAL", "BLOCKCHAIN_TRANSACTION", "EXCHANGE", "FAILED", "DEPOSIT", "MINT", "REVOKE"]
    if 'opType' in body_params.keys():
        check_correct_value_from_define_list(opTypes, 'opType', body_params['opType'])

def find_transactions_with_given_reference_across_all_accounts(path_params):
    v = cerberus.Validator()

    path_schema = {
            "reference" : {"required": True, "type" : "string", "minlength": 20, "maxlength": 100}
        }

    v.validate(path_params, path_schema)
    erros_print(v)

# ___________________________________LEDGER/CUSTOMER_______________________________________

def update_customer(path_params, body_params):
    v = cerberus.Validator()
    id_path_param(path_params)
    body_schema = {
        "externalId": {"required": True, "type" : "string", "minlength": 1, "maxlength": 100}, "providerCountry": {"type" : "string", "minlength": 2, "maxlength": 2}, 
        "customerCountry": {"type" : "string", "minlength": 2, "maxlength": 2},           "accountingCurrency": {"type" : "string", "minlength": 3, "maxlength": 3} }

    v.validate(body_params, body_schema)
    erros_print(v)

# ___________________________________LEDGER/VIRTUAL CURRENCY_______________________________
def create_new_vitual_currency(body_params):
    v = cerberus.Validator()
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
    erros_print(v)
    check_allowed_chars('^[a-zA-Z0-9_]+$', 'name', body_params['name'][3:])
    check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'supply', body_params['supply'])   
    

def update_vitual_currency(body_params):
    v = cerberus.Validator()
    body_schema = {
            "name" : {"required": True, "type" : "string", "minlength": 1, "maxlength": 30},
            "basePair" : {"type" : "string", "minlength": 3, "maxlength": 5},
            "baseRate" : {"type" : "number", "min": 0},
        }

    v.validate(body_params, body_schema)
    erros_print(v)

    check_allowed_chars('^[a-zA-Z0-9_]+$', 'name', body_params['name'][3:])


def get_virtual_currency(path_params):
    v = cerberus.Validator()
    path_schema = {
            "name" : {"required": True, "type" : "string", "minlength": 3, "maxlength": 100}
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def create_new_supply_of_virtual_currency(body_params):
    v = cerberus.Validator()
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
    erros_print(v)

    check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])



# ___________________________________LEDGER/SUBSCRIPTION___________________________________

def create_new_subcription(body_params):
    v = cerberus.Validator()
    body_schema = {
            "type" : {"required": True, "type" : "string"},
            "attr" : {"required": True, "type" : "dict", "schema": {'limit': {"required": True, "type" : "string", "maxlength": 38}, 'typeOfBalance': {"required": True, "type" : "string", "maxlength": 38}}
            }
         }

    v.validate(body_params, body_schema)
    erros_print(v)

    types = ["ACCOUNT_BALANCE_LIMIT", "OFFCHAIN_WITHDRAWAL", "TRANSACTION_HISTORY_REPORT", "ACCOUNT_INCOMING_BLOCKCHAIN_TRANSACTION", "COMPLETE_BLOCKCHAIN_TRANSACTION"]
    check_correct_value_from_define_list(types, 'type', body_params['type'])

    check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'limit', body_params['attr']['limit'])

    typeOfBalance = ["account", "available"]
    check_correct_value_from_define_list(typeOfBalance, 'typeOfBalance', body_params['typeOfBalance'])


# ___________________________________LEDGER/ORDER BOOK_____________________________________

def list_all_active_buy_trades(query_params):
    v = cerberus.Validator()
    query_schema = {
            "id": {"type" : "string"},
            "pageSize" : {"required": True, "type" : "integer", "min": 1, "max": 50},
            "offset": {"type" : "integer"}
        }

    v.validate(query_params, query_schema)
    erros_print(v)

def store_buy_sell_trade(body_params):
    v = cerberus.Validator()
    body_schema = {
            "type": {"required": True, "type" : "string"},
            "price" : {"required": True, "type" : "string", "maxlength": 38},
            "amount" : {"required": True, "type" : "string", "maxlength": 38},
            "pair" : {"required": True, "type" : "string", "minlength": 3, "maxlength": 30},
            "currency1AccountId" : {"required": True, "type" : "string", "minlength": 24, "maxlength": 24},
            "currency2AccountId" : {"required": True, "type" : "string", "minlength": 24, "maxlength": 24},
        }

    v.validate(body_params, body_schema)
    erros_print(v)
    types = ["BUY", "SELL"]
    check_correct_value_from_define_list(types, 'type', body_params['type'])
    check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'price', body_params['price'])
    check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])
    check_allowed_chars('^[A-a-zZ0-9_\-]+\/[A-Za-z0-9_\-]+$', 'pair', body_params['pair'])

# ___________________________________SECURITY/KEY MANAGEMENT SYSTEM_____________________________________

def get_pending_transactions_to_sign(path_params):
    v = cerberus.Validator()
    path_schema = {
            "chain": {"required": True, "type" : "string"},
        }

    v.validate(path_params, path_schema)
    erros_print(v)

    chains = ["BTC", "ETH", "XLM", "XRP", "BCH", "LTC", "VET"]
    check_correct_value_from_define_list(chains, 'chain', path_params['chain'])

def complete_pending_transaction_to_sign(path_params):
    v = cerberus.Validator()
    path_schema = {
            "id": {"required": True, "type" : "string", "minlength": 24, "maxlength": 24},
            "txId": {"required": True, "type" : "string", "minlength": 10, "maxlength": 80},
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def delete_transaction(path_params, query_params):
    v = cerberus.Validator()
    id_path_param(path_params)
    query_schema = {
            "revert": {"type" : "string"},
        }

    v.validate(query_params, query_schema)
    erros_print(v)
    
    if query_params != {}:
        reverts = ["true", "false"]
        check_correct_value_from_define_list(reverts, 'revert', query_params['revert'])

# ___________________________________SECURITY/ADDRESS_____________________________________


def check_malicous_address(path_params):
    v = cerberus.Validator()
    path_schema = {
            "address": {"required": True, "type" : "string"},
        }
    v.validate(path_params, path_schema)
    erros_print(v)

# ___________________________________OFFCHAIN/ ACCOUNT_________________________________________


def create_new_deposit_address(path_params, query_params):
    v = cerberus.Validator()
    id_path_param(path_params)

    if query_params != {}:
        query_schema = {
                "index": {"type" : "integer"},
            }

        v.validate(query_params, query_schema)
        erros_print(v)

def check_if_deposit_address_is_asigned(path_params, query_params):
    v = cerberus.Validator()
    path_schema = {
            "address": {"required": True, "type" : "string"},
            "currency": {"required": True, "type" : "string"}
        }
    v.validate(path_params, path_schema)
    erros_print(v)

    if query_params != {}:
        query_schema = {
                "index": {"type" : "integer"},
            }

        v.validate(query_params, query_schema)
        erros_print(v)

def remove_address_for_account(path_params):
    v = cerberus.Validator()
    path_schema = {
            "address": {"required": True, "type" : "string"},
            "id": {"required": True, "type" : "string"}
        }
    v.validate(path_params, path_schema)
    erros_print(v)

# ___________________________________OFFCHAIN/ WITHDRAWAL_________________________________________


def store_withdrawal(body_params):
    v = cerberus.Validator()
    body_schema = {
            "senderAccountId": {"required": True, "type" : "string", "minlength": 24, "maxlength": 24},
            "address": {"required": True, "type" : "string", "minlength": 1, "maxlength": 100},
            "amount": {"required": True, "type" : "string", "maxlength": 38},
            "attr": {"type" : "string", "minlength": 1, "maxlength": 64},
            "compliant": {"type": "boolean"},
            "fee": {"type" : "string"},
            "paymentId": {"type" : "string", "minlength": 1, "maxlength": 100},
            "senderBlockchainAddress": {"type" : "string", "minlength": 1, "maxlength": 100},
            "senderNote": {"type" : "string", "minlength": 1, "maxlength": 500}
        }
    v.validate(body_params, body_schema)
    erros_print(v)
    if 'amount' in body_params.keys():
        check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])
    if 'fee' in body_params.keys():
        check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'fee', body_params['fee'])

def broadcast_signed_transaction_and_complete_withdrawal(body_params):
    v = cerberus.Validator()
    body_schema = {
            "currency": {"required": True, "type" : "string", "minlength": 2, "maxlength": 40},
            "txData": {"required": True, "type" : "string", "minlength": 1, "maxlength": 500000},
            "withdrawalId": {"type" : "string", "minlength": 24, "maxlength": 24},
            "signatureId": {"type" : "string", "minlength": 24, "maxlength": 24},
        }
    v.validate(body_params, body_schema)
    erros_print(v)

# ___________________________________OFFCHAIN/ BLOCKCHAIN_________________________________________

def send_from_tatum_account_to_address(body_params):
    v = cerberus.Validator()
    body_schema = {
            "senderAccountId": {"required": True, "type" : "string", "minlength": 24, "maxlength": 24},
            "address": {"required": True, "type" : "string", "minlength": 1, "maxlength": 100},
            "amount": {"required": True, "type" : "string", "maxlength": 38},
            "compliant": {"type": "boolean"},
            "fee": {"type" : "string"},
            "keyPair": {"type": "list", "schema": {"type": "dict", "schema": {"address": {"type": "string", "minlength": 1, "maxlength": 100}, "privateKey": {"type": "string", "minlength": 1, "maxlength": 100}}}},
            "attr": {"type" : "string", "minlength": 1, "maxlength": 64},
            "mnemonic": {"type" : "string", "minlength": 1, "maxlength": 500},
            "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
            "xpub": {"type" : "string", "minlength": 1, "maxlength": 150},
            "paymentId": {"type" : "string", "minlength": 1, "maxlength": 100},
            "senderNote": {"type" : "string", "minlength": 1, "maxlength": 500}
        }
    v.validate(body_params, body_schema)
    erros_print(v)
    
    if 'amount' in body_params.keys():
        check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])
    if 'fee' in body_params.keys():
        check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'fee', body_params['fee'])

def send_ethereum_from_tatum_ledger_to_blockchain(body_params):
    v = cerberus.Validator()
    body_schema = {
            "nonce": {"type": "integer", "min": 0},
            "address": {"required": True, "type" : "string", "minlength": 42, "maxlength": 42},
            "amount": {"required": True, "type" : "string", "maxlength": 38},
            "currency": {"type": "string"},
            "compliant": {"type": "boolean"},
            "privateKey": {"type": "string", "minlength": 66, "maxlength": 66},
            "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
            "index": {"type": "integer", "max": 4294967295},
            "mnemonic": {"type" : "string", "minlength": 1, "maxlength": 500},
            "paymentId": {"type" : "string", "minlength": 1, "maxlength": 100},
            "senderAccountId" : {"required": True, "type" : "string", "minlength": 24, "maxlength": 24},
            "senderNote": {"type" : "string", "minlength": 1, "maxlength": 500}
         }
    v.validate(body_params, body_schema)
    erros_print(v)
    
    currencies = ["USDT", "LEO", "LINK", "FREE", "MKR", "USDC", "BAT", "TUSD", "PAX", "PAXG", "PLTC", "MMY", "XCON", "ETH"]
    if 'currency' in body_params.keys():
        check_correct_value_from_define_list(currencies, 'currency', body_params['currency'])


    if 'amount' in body_params.keys():
        check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])
    if 'fee' in body_params.keys():
        check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'fee', body_params['fee'])

def create_new_ERC20_token(body_params):
    v = cerberus.Validator()
    body_schema = {
            "symbol": {"required": True, "type" : "string", "minlength": 1, "maxlength": 30},
            "supply" : {"required": True, "type" : "string", "minlength": 1, "maxlength": 38},
            "description" : {"required": True, "type" : "string", "minlength": 1, "maxlength": 100},
            "basePair" : {"required": True, "type" : "string", "minlength": 3, "maxlength": 5},
            "customer": {"type" : "dict", "schema": {'externalId': {"required": True, "type" : "string", "minlength": 1, "maxlength": 100}, "providerCountry": {"type" : "string", "minlength": 2, "maxlength": 2}, "customerCountry": {"type" : "string", "minlength": 2, "maxlength": 2},           "accountingCurrency": {"type" : "string", "minlength": 3, "maxlength": 3} }},
            "accountingCurrency": {"type" : "string", "minlength": 3, "maxlength": 3},
            "derivationIndex": {"type": "integer", "max": 4294967295},
            "xpub": {"type" : "string", "minlength": 1, "maxlength": 150},
            "address": {"type" : "string", "minlength": 42, "maxlength": 42}
         }
    v.validate(body_params, body_schema)
    erros_print(v)
    check_allowed_chars('^[a-zA-Z0-9_]+$', 'symbol', body_params['symbol'])
    check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'supply', body_params['supply'])   

    currencies = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BAT", "BBD", "BCH", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTC", "BTN", "BWP", "BYN", "BYR", "BZD", "CAD", "CDF", "CHF", "CLF", "CLP", "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "ETH", "EUR", "FJD", "FKP", "FREE", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LEO", "LINK", "LKR", "LRD", "LSL", "LTC", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MKR", "MMK", "MMY", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PAX", "PAXG", "PEN", "PGK", "PHP", "PKR", "PLN", "PLTC", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TUSD", "TWD", "TZS", "UAH", "UGX", "USD", "USDC", "USDT", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XCD", "XCON", "XDR", "XLM", "XOF", "XPF", "XRP", "YER", "ZAR", "ZMK", "ZMW", "ZWL"]
    check_correct_value_from_define_list(currencies, 'basePair', body_params['basePair'])
    if 'customer' in body_params.keys():
        if 'accountingCurrency' in body_params.keys():
            check_correct_value_from_define_list(currencies, 'accountingCurrency', body_params['customer']['accountingCurrency'])
    if 'accountingCurrency' in body_params.keys():
        check_correct_value_from_define_list(currencies, 'accountingCurrency', body_params['accountingCurrency'])


def deploy_ethereum_erc20_smart_contract_offchain(body_params):
    v = cerberus.Validator()
    body_schema = {
            "symbol": {"required": True, "type" : "string", "minlength": 1, "maxlength": 30},
            "supply" : {"required": True, "type" : "string", "minlength": 1, "maxlength": 38},
            "description" : {"required": True, "type" : "string", "minlength": 1, "maxlength": 100},
            "basePair" : {"required": True, "type" : "string", "minlength": 2, "maxlength": 30},
            "customer": {"type" : "dict", "schema": {'externalId': {"required": True, "type" : "string", "minlength": 1, "maxlength": 100}, "providerCountry": {"type" : "string", "minlength": 2, "maxlength": 2}, "customerCountry": {"type" : "string", "minlength": 2, "maxlength": 2},           "accountingCurrency": {"type" : "string", "minlength": 3, "maxlength": 3} }},
            "xpub": {"type" : "string", "minlength": 1, "maxlength": 150},
            "derivationIndex": {"type": "integer", "max": 4294967295},
            "address": {"type" : "string", "minlength": 42, "maxlength": 42},
            "mnemonic": {"type" : "string", "minlength": 1, "maxlength": 500},
            "index": {"type": "integer", "max": 4294967295},
            "privateKey": {"type": "string", "minlength": 66, "maxlength": 66},
            "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
            "nonce": {"type": "integer", "min": 0}           
         }
    v.validate(body_params, body_schema)
    erros_print(v)
    check_allowed_chars('^[a-zA-Z0-9_]+$', 'symbol', body_params['symbol'])
    check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'supply', body_params['supply'])   

    currencies = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BAT", "BBD", "BCH", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTC", "BTN", "BWP", "BYN", "BYR", "BZD", "CAD", "CDF", "CHF", "CLF", "CLP", "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "ETH", "EUR", "FJD", "FKP", "FREE", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LEO", "LINK", "LKR", "LRD", "LSL", "LTC", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MKR", "MMK", "MMY", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PAX", "PAXG", "PEN", "PGK", "PHP", "PKR", "PLN", "PLTC", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TUSD", "TWD", "TZS", "UAH", "UGX", "USD", "USDC", "USDT", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XCD", "XCON", "XDR", "XLM", "XOF", "XPF", "XRP", "YER", "ZAR", "ZMK", "ZMW", "ZWL"]
    if 'customer' in body_params.keys():
        if 'accountingCurrency' in body_params.keys():
            check_correct_value_from_define_list(currencies, 'accountingCurrency', body_params['customer']['accountingCurrency'])

def set_erc20_token_contract_address(path_params):
    v = cerberus.Validator()
    path_schema = {
            "address": {"required": True, "type" : "string", "minlength": 1, "maxlength": 100},
            "name": {"required": True, "type" : "string", "minlength": 1, "maxlength": 30},
        }
    v.validate(path_params, path_schema)
    erros_print(v)
    check_allowed_chars('^[a-zA-Z0-9_]+$', 'name', path_params['name'])

def transfer_ethereum_erc20_from_tatum_ledger_to_blockchain(body_params):
    v = cerberus.Validator()
    body_schema = {
            "senderAccountId" : {"required": True, "type" : "string", "minlength": 24, "maxlength": 24},
            "address": {"required": True, "type" : "string", "minlength": 42, "maxlength": 42},
            "amount" : {"required": True, "type" : "string", "maxlength": 38},
            "compliant": {"type": "boolean"},
            "currency" : {"type" : "string", "minlength": 2, "maxlength": 30},
            "privateKey": {"type": "string", "minlength": 66, "maxlength": 66},
            "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
            "mnemonic": {"type" : "string", "minlength": 1, "maxlength": 500},
            "index": {"type": "integer", "max": 4294967295},
            "nonce": {"type": "integer", "min": 0},
            "paymentId":{"type" : "string","minlength": 1, "maxlength": 100},
            "senderNote":{"type" : "string","minlength": 1, "maxlength": 500}
        }
    v.validate(body_params, body_schema)
    erros_print(v)
    check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])

def send_xlm_asset_from_tatum_ledger_to_blockchain(body_params):
    v = cerberus.Validator()
    body_schema = {
            "senderAccountId" : {"required": True, "type" : "string", "minlength": 24, "maxlength": 24},
            "fromAccount": {"required": True, "type" : "string", "minlength": 56, "maxlength": 56},
            "address": {"required": True, "type" : "string", "minlength": 56, "maxlength": 56},
            "amount" : {"required": True, "type" : "string", "maxlength": 38},
            "secret": {"type" : "string", "minlength": 56, "maxlength": 56},
            "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},
            "compliant": {"type": "boolean"},
            "attr": {"type" : "string", "maxlength": 64},
            "paymentId":{"type" : "string","minlength": 1, "maxlength": 100},
            "senderNote":{"type" : "string","minlength": 1, "maxlength": 500},
            "issuerAccount": {"type" : "string", "minlength": 56, "maxlength": 56},
            "token": {"type" : "string", "minlength": 1, "maxlength": 12}
        }
    v.validate(body_params, body_schema)
    erros_print(v)
    check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])
    if 'attr' in body_params.keys():
        check_allowed_chars('^[ -~]{0,64}$', 'attr', body_params['attr'])
    if 'token' in body_params.keys():
        check_allowed_chars('^[a-zA-Z0-9]{1,12}$', 'token', body_params['token'])

def create_xlm_based_asset(body_params):
    v = cerberus.Validator()
    body_schema = {
            "issuerAccount": {"required": True, "type" : "string", "minlength": 56, "maxlength": 56},
            "token": {"required": True, "type" : "string", "minlength": 1, "maxlength": 12},
            "basePair" : {"required": True, "type" : "string", "minlength": 3, "maxlength": 5}
        }
    v.validate(body_params, body_schema)
    erros_print(v)
    check_allowed_chars('^[a-zA-Z0-9]{1,12}$', 'token', body_params['token'])
    currencies = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BAT", "BBD", "BCH", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTC", "BTN", "BWP", "BYN", "BYR", "BZD", "CAD", "CDF", "CHF", "CLF", "CLP", "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "ETH", "EUR", "FJD", "FKP", "FREE", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LEO", "LINK", "LKR", "LRD", "LSL", "LTC", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MKR", "MMK", "MMY", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PAX", "PAXG", "PEN", "PGK", "PHP", "PKR", "PLN", "PLTC", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TUSD", "TWD", "TZS", "UAH", "UGX", "USD", "USDC", "USDT", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XCD", "XCON", "XDR", "XLM", "XOF", "XPF", "XRP", "YER", "ZAR", "ZMK", "ZMW", "ZWL"]
    check_correct_value_from_define_list(currencies, 'basePair', body_params['basePair'])

def send_xrp_from_tatum_ledger_to_blockchain(body_params):
    v = cerberus.Validator()
    body_schema = {
            "senderAccountId" : {"required": True, "type" : "string", "minlength": 24, "maxlength": 24},
            "account": {"required": True, "type" : "string", "minlength": 1, "maxlength": 100},
            "address": {"required": True, "type" : "string", "minlength": 1, "maxlength": 100},
            "amount" : {"required": True, "type" : "string", "maxlength": 38},
            "compliant": {"type": "boolean"},
            "attr": {"type" : "string"},
            "sourceTag": {"type" : "integer"},
            "paymentId":{"type" : "string","minlength": 1, "maxlength": 100},
            "secret": {"type" : "string", "minlength": 29, "maxlength": 29},
            "signatureId": {"type" : "string", "minlength": 36, "maxlength": 36},            
            "senderNote":{"type" : "string","minlength": 1, "maxlength": 500},
            "issuerAccount": {"type" : "string", "minlength": 33, "maxlength": 34},
            "token": {"type" : "string", "minlength": 40, "maxlength": 40}
        }
    v.validate(body_params, body_schema)
    erros_print(v)
    check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])
    if 'token' in body_params.keys():
        check_allowed_chars('^[a-zA-Z0-9]{1,12}$', 'token', body_params['token'])


def create_xrp_based_asset(body_params):
    v = cerberus.Validator()
    body_schema = {
            "issuerAccount": {"required": True, "type" : "string", "minlength": 33, "maxlength": 34},
            "token": {"required": True, "type" : "string", "minlength": 40, "maxlength": 40},
            "basePair" : {"required": True, "type" : "string", "minlength": 3, "maxlength": 5}
        }
    v.validate(body_params, body_schema)
    erros_print(v)
    check_allowed_chars('^[a-zA-Z0-9]{1,12}$', 'token', body_params['token'])
    currencies = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BAT", "BBD", "BCH", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTC", "BTN", "BWP", "BYN", "BYR", "BZD", "CAD", "CDF", "CHF", "CLF", "CLP", "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "ETH", "EUR", "FJD", "FKP", "FREE", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LEO", "LINK", "LKR", "LRD", "LSL", "LTC", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MKR", "MMK", "MMY", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PAX", "PAXG", "PEN", "PGK", "PHP", "PKR", "PLN", "PLTC", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TUSD", "TWD", "TZS", "UAH", "UGX", "USD", "USDC", "USDT", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XCD", "XCON", "XDR", "XLM", "XOF", "XPF", "XRP", "YER", "ZAR", "ZMK", "ZMW", "ZWL"]
    check_correct_value_from_define_list(currencies, 'basePair', body_params['basePair'])

# ___________________________________BLOCKCHAIN_________________________________________


def generate_wallet(query_params):
    v = cerberus.Validator()
    if query_params != {}:
        query_schema = {
                "index": {"type" : "integer"},
            }

        v.validate(query_params, query_schema)
        erros_print(v)

def generate_deposit_address_from_extended_public_key(path_params):
    v = cerberus.Validator()
    path_schema = {
            "xpub": {"required": True, "type" : "string"},
            "index": {"required": True, "type" : "integer", "min": 0}
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def generate_private_key(body_params):
    v = cerberus.Validator()
    body_schema = {
            "mnemonic": {"required": True, "type" : "string", "minlength": 1, "maxlength": 500},
            "index": {"required": True, "type" : "integer", "max": 4294967295}
        }

    v.validate(body_params, body_schema)
    erros_print(v)

def get_block_hash(path_params):
    v = cerberus.Validator()
    path_schema = {
            "i": {"required": True, "type" : "number"},
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def ethereum_get_block_hash(path_params):
    v = cerberus.Validator()
    path_schema = {
            "hash": {"required": True, "type" : "string"},
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def get_block_by_hash_or_height(path_params):
    v = cerberus.Validator()
    path_schema = {
            "hash": {"required": True, "type" : "string"},
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def get_transaction_by_address(path_params, query_params):
    v = cerberus.Validator()
    page_size_query_params(query_params)
    path_schema = {
            "address": {"required": True, "type" : "string"},
        }

    v.validate(path_params, path_schema)
    erros_print(v)


def get_utxo_of_transaction(path_params):
    v = cerberus.Validator()
    path_schema = {
            "hash": {"required": True, "type" : "string", "minlength": 64, "maxlength": 64},
            "index": {"required": True, "type" : "number", "min": 0}
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def send_bitcoin_to_blockchain_addresses(body_params):
    v = cerberus.Validator()
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
    v = cerberus.Validator()
    body_schema = {
            "txData": {"required": True, "type" : "string", "minlength": 1, "maxlength": 500000},
            "signatureId": {"type" : "string", "minlength": 24, "maxlength": 24},
        }
    v.validate(body_params, body_schema)
    erros_print(v)

def get_ethereum_account_balance(path_params):
    v = cerberus.Validator()
    path_schema = {
            "address": {"required": True, "type" : "string"},
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def get_ethereum_erc20_account_balance(path_params, query_params):
    v = cerberus.Validator()
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
    v = cerberus.Validator()
    path_schema = {
            "address": {"required": True, "type" : "string", "minlength": 42, "maxlength": 42 },
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def bitcoin_cash_get_block_hash(path_params):
    v = cerberus.Validator()
    path_schema = {
            "hash": {"required": True, "type" : "string"},
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def get_bitcoin_cash_transaction_by_address(path_params, query_params):
    v = cerberus.Validator()
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
    v = cerberus.Validator()
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
    v = cerberus.Validator()
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
    v = cerberus.Validator()
    path_schema = {
            "i": {"required": True, "type" : "number", 'min': 0},
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def get_account_info(path_params):
    v = cerberus.Validator()
    path_schema = {
            "account": {"required": True, "type" : "string"},
        }

    v.validate(path_params, path_schema)
    erros_print(v)

def send_xrp_to_blockchain_addresses(body_params):
    v = cerberus.Validator()
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
    v = cerberus.Validator()
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
    v = cerberus.Validator()
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