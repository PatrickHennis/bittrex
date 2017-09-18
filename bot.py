from bittrex_v2 import Bittrex
import sys
import time

b = Bittrex("dad26eb421d04941b2fc3bcf27d25a38", "dee88d50c7394e2d82e8fe9ad65bc192")

def main():
    help()
    parse_option()

def parse_option():
    option = input("> ")
    if option == "o":
        orders()
    elif option == "w":
        wallet()
    elif option == "n":
        new_orders()
    elif option == "h":
        help()
    elif option == "q":
        print("Shutdown requested...exiting")
        time.sleep(1)
        sys.exit(0)

def orders():
    print("**************** OPEN ORDERS ****************")
    open_orders = b.get_open_orders()
    for key in open_orders['result']:
        print("Exchange: ", key['Exchange'])
        print("Amount: ", key['Quantity'])
        print("Price: ", key['Limit'], "\n")
    parse_option()

def wallet():
    print("wallet")

def new_orders():
    print("new")

def help():
    print("**************** BITTREX BOT ****************")
    print("press 'o' to view open orders on account")
    print("press 'w' to view wallet balances on account")
    print("press 'n' to set new buy and sell orders")
    print("press 'q' to quit")
    print("press 'h' to view this screen again")

if __name__ == '__main__':
    main()
