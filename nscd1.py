# from datetime import date
# from nsepy import get_history
#     # Stock futures (Similarly for index futures, set index = True)
# stock_fut = get_history(symbol="SBIN",
#                             start=date(2023,8,1),
#                             end=date(2023,8,10),
#                             futures=True,
#                             expiry_date=date(2023,8,31))

from nsefinance import NSEFinance
stocks = NSEFinance()

#Available keys :
#['high', 'symbol', 'value', 'deals', 'date','low','units','close','open','change']

#Get closing prices for all the symbols for the trading day.
result = stocks.get_daily_list()
for i in range(len(result)):
	result[i]['close']

#Get the closing price for the last 5 trading day for a symbol
result = stocks.get_by_symbol("OANDO")
for i in range(len(result)):
	result[i]['close']

#Get the closing price for a particular symbol on a particular day
symbol = "OANDO"
result = stocks.get_by_symbol(symbol,"2014-02-06")
result[symbol]['close']