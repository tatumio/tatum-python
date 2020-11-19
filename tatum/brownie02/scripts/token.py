from brownie import Token, accounts


def main():
    Token.deploy("Test Token", "TST", 18, 1e23, {'from': accounts[0]})