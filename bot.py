from bittrex_v2 import Bittrex
import sys

def main():
    help()
    option = input("> ")
    parse_option(option)

def parse_option(option):
    if option == "o":
        orders()
    elif option == "w":
        wallet()
    elif option == "n":
        new_orders()
    elif option == "h":
        help()

def orders():
    print("orders")

def wallet():
    print("wallet")

def new_orders():
    print("new")

def help():
    print("**************** BITTREX BOT ****************")
    print("press 'o' to view open orders on account")
    print("press 'w' to view wallet balances on account")
    print("press 'n' to set new buy and sell orders")
    print("press 'h' to view this screen again")

if __name__ == '__main__':
    main()
