#!/usr/bin/env python
from bittrex import bittrex
import time

# Get these from https://bittrex.com/Account/ManageApiKey
api = bittrex('dad26eb421d04941b2fc3bcf27d25a38', 'dee88d50c7394e2d82e8fe9ad65bc192')

# Market to trade at
trade = 'BTC'
currency = 'ZEN'
market = '{0}-{1}'.format(trade, currency)


start_price = 0.00211000
start_vol = 11.03003696

print (api.getopenorders(market) == None)
print api.getopenorders(market)

# Getting the BTC price for ZEN
while(1):
    zensummary = api.getmarketsummary(market)
    zenprice = zensummary[0]['Last']
    print 'The price for {0} is {1:.8f} {2}.'.format(currency, zenprice, trade)
    time.sleep(3)



# while(1):
#     amount = 100
#     multiplier = 1.5
#
#     zensummary = api.getmarketsummary(market)
#     zenprice = zensummary[0]['Last']
#     print 'The price for {0} is {1:.8f} {2}.'.format(currency, zenprice, trade)
#
#     print 'Buying {0} {1} for {2:.8f} {3}.'.format(amount, currency, zenprice, trade)
#
#     dogeprice = round(zenprice*multiplier, 8)
#
#     print 'Selling {0} {1} for {2:.8f} {3}.'.format(amount, currency, zenprice, trade)
#
#     zenbalance = api.getbalance(currency)
#     print "Your balance is {0} {1}.".format(zenbalance['Available'], currency)
#
#     time.sleep(3)
