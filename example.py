#!/usr/bin/env python
from bittrex import bittrex
import time

# Get these from https://bittrex.com/Account/ManageApiKey
api = bittrex('dad26eb421d04941b2fc3bcf27d25a38', 'dee88d50c7394e2d82e8fe9ad65bc192')

# Market to trade at
trade = 'BTC'
currency = 'ZEN'
market = '{0}-{1}'.format(trade, currency)

# numbers from my account, just using to play around wiyh
start_price = 0.00211000
start_vol = 11.03003696
balance = api.getbalance(currency)
sell_price = 0.0


def findOrderType():
    open_orders = api.getopenorders(market)
    return open_orders[0]['OrderType']


# Getting the BTC price for ZEN
while(1):
    if len(api.getopenorders(market)) > 0:
        print "open order found"
        orderType = findOrderType()
        # if orderType == "LIMIT_SELL":
            # deal with open sell order
        # if orderType == "LIMIT_BUY":
            # deal with open buy order
    else:
        print "no open order found"

        # set up some vars that will be needed later
        zen_summary = api.getmarketsummary(market)
        zen_price_last = zen_summary[0]['Last']
        # *****************************************

        # check if there is a balance in zen in wallet

        if (balance > 0): # currently have zen
            # see if sell or hold
            # when price falling: sell if it drops 50%
            # when price rising: sell if it raises 30%
            if ((zen_price_last / start_price) <= 0.5):
                print 'CRASHING: selling out zen at {0}'.format(zen_price_last)
                sell_price = zen_price_last
                balance = 0
                # shits falling, sell out now fam, cut losses
                # set sell price
            elif (((zen_price_last - start_price) / start_price) >= 0.3):
                print 'EXPLODING: selling zen at {0}'.format(zen_price_last)
                sell_price = zen_price_last
                balance = 0
                # shit exploded, grab profits and run
                # set sell price
            else:
                print 'do nothin'
        else: # no zen in wallet
            # see if buy by checking if current buying power can raise the previous volume
            if (zen_price_last < sell_price * 0.3):
                print 'BUYING in at {0}'.formay(zen_price_last)
                start_price = zen_price_last
                balance = 1 #fix eventually to be correct balance
                # make limit buy with max bitcoin

    time.sleep(3)
