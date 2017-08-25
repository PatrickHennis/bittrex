#!/usr/bin/env python
from bittrex import bittrex

# Get these from https://bittrex.com/Account/ManageApiKey
api = bittrex('dad26eb421d04941b2fc3bcf27d25a38', 'dee88d50c7394e2d82e8fe9ad65bc192')

# Market to trade at
trade = 'BTC'
currency = 'ZEN'
market = '{0}-{1}'.format(trade, currency)

# Getting the BTC price for ZEN
zensummary = api.getmarketsummary(market)
zenprice = zensummary[0]['Last']
print 'The price for {0} is {1:.8f} {2}.'.format(currency, zenprice, trade)
