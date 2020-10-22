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

# ___________________________________OFFCHAIN/ ACCOUNT_________________________________________


def create_new_deposit_address(path_params, query_params):
    result = True
    result = result & id_path_param(path_params)

    if query_params != {}:
        query_schema = {
                "index": {"type" : "integer"},
            }

        v.validate(query_params, query_schema)
        result = result & erros_print(v)
    return result

def check_if_deposit_address_is_asigned(path_params, query_params):
    result = True
    path_schema = {
            "address": {"required": True, "type" : "string"},
            "currency": {"required": True, "type" : "string"}
        }
    v.validate(path_params, path_schema)
    result = result & erros_print(v)

    if query_params != {}:
        query_schema = {
                "index": {"type" : "integer"},
            }

        v.validate(query_params, query_schema)
        result = result & erros_print(v)
    return result

def remove_address_for_account(path_params):
    path_schema = {
            "address": {"required": True, "type" : "string"},
            "id": {"required": True, "type" : "string"}
        }
    v.validate(path_params, path_schema)
    return erros_print(v)

# ___________________________________OFFCHAIN/ WITHDRAWAL_________________________________________


def store_withdrawal(body_params):
    result = True
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
    result = result & erros_print(v)
    if result:
        if 'amount' in body_params.keys():
            result = result & check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'amount', body_params['amount'])
        if 'fee' in body_params.keys():
            result = result & check_allowed_chars('^[+]?((\d+(\.\d*)?)|(\.\d+))$', 'fee', body_params['fee'])
        return result

def broadcast_signed_transaction_and_complete_withdrawal(body_params):
    body_schema = {
            "currency": {"required": True, "type" : "string", "minlength": 2, "maxlength": 40},
            "txData": {"required": True, "type" : "string", "minlength": 1, "maxlength": 500000},
            "withdrawalId": {"type" : "string", "minlength": 24, "maxlength": 24},
            "signatureId": {"type" : "string", "minlength": 24, "maxlength": 24},
        }
    v.validate(body_params, body_schema)
    return erros_print(v)

# ___________________________________OFFCHAIN/ BLOCKCHAIN_________________________________________

def send_from_tatum_account_to_address(body_params):
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
    path_schema = {
            "address": {"required": True, "type" : "string", "minlength": 1, "maxlength": 100},
            "name": {"required": True, "type" : "string", "minlength": 1, "maxlength": 30},
        }
    v.validate(path_params, path_schema)
    erros_print(v)
    check_allowed_chars('^[a-zA-Z0-9_]+$', 'name', path_params['name'])

def transfer_ethereum_erc20_from_tatum_ledger_to_blockchain(body_params):
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
