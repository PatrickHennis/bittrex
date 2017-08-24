from bittrex import bittrex

# replace with actual info from bittrex
api = bittrex('dad26eb421d04941b2fc3bcf27d25a38', 'dee88d50c7394e2d82e8fe9ad65bc192')

trade = 'BTC'
currency = 'ZEN'
market = '{0}-{1}'.format(trade, currency)

zensummary = api.getmarketsummary(market)
price_of_zen = zensummary[0]['Last']
