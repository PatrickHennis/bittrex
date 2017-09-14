from bittrex_v2 import Bittrex
b = Bittrex()

trade = 'BTC'
currency = 'ZEN'
market = '{0}-{1}'.format(trade, currency)

zen_summary = b.get_market_summary(market)
zen_price_last = zen_summary['result']['Last']

ticks = b.get_ticks(market, "thirtyMin")

length_of_ticks = len(ticks['result'])

num_of_days = 20
curr_day = 1

running_ave = 0
num = 0
# calc sma
while(curr_day < num_of_days):
    current = length_of_ticks - curr_day - 1
    running_ave += ticks['result'][current]['C']
    curr_day += 1
    num += 1

running_ave += zen_price_last


sma = running_ave/num_of_days

print(sma)

# calc standard deviation
curr_day = 0
squared_deviations = 0

# while(curr_day < num_of_days):
