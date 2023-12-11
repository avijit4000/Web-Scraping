# print('avijit')
# print('_____________________________________')
import requests
session = requests.Session()
# session.max_redirects = 60
# session.get('http://www.amazon.com')


from nsepy import get_history as gh
import datetime as dt
import dateutil.relativedelta as dr
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
tradingsymbol='NIFTY BANK'
end=dt.date.today()
start=end-dr.relativedelta(days=30)

data=gh(tradingsymbol,start,end,index=True)

data.max_redirects = 2

data['Close'].plot()
plt.show()