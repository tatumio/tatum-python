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
    page_size_query_params(query_params)

# ___________________________________LEDGER/TRANSACTION____________________________________
def validate_transaction_type(body_params):
    transactionType = ["FAILED", "DEBIT_PAYMENT", "CREDIT_PAYMENT", "CREDIT_DEPOSIT", "DEBIT_WITHDRAWAL", "CANCEL_WITHDRAWAL", "DEBIT_OUTGOING_PAYMENT", "EXCHANGE_BUY", "EXCHANGE_SELL", "DEBIT_TRANSACTION", "CREDIT_INCOMING_PAYMENT"]
    for key in body_params.keys():
        if key == "transactionType":
            resultType = False
            for type in transactionType:
                if type == body_params["transactionType"]:
                    resultType = True
            if resultType == False:
                print(colored('{"transactionType": is not allowed type }','red'))

def validate_op_type(body_params):
    opTypes = ["PAYMENT", "WITHDRAWAL", "BLOCKCHAIN_TRANSACTION", "EXCHANGE", "FAILED", "DEPOSIT", "MINT", "REVOKE"]
    for key in body_params.keys():
        if key == "opType":
            resultOpType = False
            for opType in opTypes:
                if opType == body_params["opType"]:
                    resultOpType = True
                    
            if resultOpType == False:
                print(colored('{"opType": is not allowed type }','red'))

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

    not_allowed_chars = '^[+]?((\d+(\.\d*)?)|(\.\d+))$'
    for i in range(len(not_allowed_chars)-1):
        if not_allowed_chars[i] in body_params['amount']:
            print(colored("{'amount': contains not allowed characters}", 'red'))
            break

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

    validate_transaction_type(body_params)
    validate_op_type(body_params)

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

    validate_transaction_type(body_params)
    validate_op_type(body_params)

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

    validate_transaction_type(body_params)
    validate_op_type(body_params)

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
            "customer": {"type" : "dict", "schema": {'externalId': {"required": True, "type" : "string", "minlength": 1, "maxlength": 100}, "providerCountry": {"type" : "string", "minlength": 2, "maxlength": 2}, "customerCountry": {"type" : "string", "minlength": 2, "maxlength": 2},           "accountingCurrency": {"type" : "string", "minlength": 3, "maxlength": 3} }},
            "description":{"type" : "string", "minlength": 1, "maxlength": 100},
            "accountCode":{"type" : "string", "minlength": 1, "maxlength": 50},
            "accountNumber":{"type" : "string"},
            "accountingCurrency":{"type" : "string", "minlength": 3, "maxlength": 3}
        }

    v.validate(body_params, body_schema)
    erros_print(v)

    not_allowed_chars ='^[a-zA-Z0-9_]+$'
    for i in range(len(not_allowed_chars)-1):
        if not_allowed_chars[i] in body_params['name'][3:]:
            print(colored("{'name': contains not allowed characters}", 'red'))
            break

    not_allowed_chars ='^[+]?((\d+(\.\d*)?)|(\.\d+))$'
    for i in range(len(not_allowed_chars)-1):
        if not_allowed_chars[i] in body_params['supply']:
            print(colored("{'name': contains not allowed characters}", 'red'))
            break

def update_vitual_currency(body_params):
    v = cerberus.Validator()
    body_schema = {
            "name" : {"required": True, "type" : "string", "minlength": 1, "maxlength": 30},
            "basePair" : {"type" : "string", "minlength": 3, "maxlength": 5},
            "baseRate" : {"type" : "number", "min": 0},
        }

    v.validate(body_params, body_schema)
    erros_print(v)

    not_allowed_chars ='^[a-zA-Z0-9_]+$'
    for i in range(len(not_allowed_chars)-1):
        if not_allowed_chars[i] in body_params['name'][3:]:
            print(colored("{'name': contains not allowed characters}", 'red'))
            break

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

    not_allowed_chars ='^[+]?((\d+(\.\d*)?)|(\.\d+))$'
    for i in range(len(not_allowed_chars)-1):
        if not_allowed_chars[i] in body_params['amount']:
            print(colored("{'amount': contains not allowed characters}", 'red'))
            break


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
    for type in types:
        resultType = False
        if body_params['type'] == type:
            resultType = True
            break
    if resultType != True:
        print(colored('{"type": is not allowed type}'))

    not_allowed_chars = '^[+]?((\d+(\.\d*)?)|(\.\d+))$'
    for i in range(len(not_allowed_chars)-1):
        if not_allowed_chars[i] in body_params['attr']['limit']:
            print(colored("{'amount': contains not allowed characters}", 'red'))
            break

    typeOfBalance = ["account", "available"]
    resultTypeOfBalance = False
    for i in range(0, len(typeOfBalance)-1):
        if body_params['attr']['typeOfBalance'] == typeOfBalance[i]:
            resultTypeOfBalance = True
            break
    if resultTypeOfBalance == False:
        print(colored('{"typeOfBalance": is not allowed type}'))

    

# ___________________________________LEDGER/ORDER BOOK_____________________________________