# from nsepy import get_history
# from datetime import date
# data = get_history(symbol="SBIN", start=date(2023,7,29), end=date(2015,8,29))
# data[['Close']].plot()
# print('avijit')


import pandas as pd
from nsedatapynew.history import get_price_list
from datatime import date
bhavcopy=get_price_list(dt=date(2023,8,29))
bhavcopy["AVG_PRICE"]=bhavcopy["TOTTRDVAL"]/bhavcopy["TOTTRDOTY"]
data=pd.read_csv("sec_bhavdata_full_30082022.csv",skipinitialspace=True)
data=date[date['SERIES']=='EQ']
date['CHANGE']=data["CLOSE_PRICE"]-data["PREV_CLOSE"]
desired_width=320
pd.set_option('display.width',desired_width)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
print(data.head())
print(bhavcopy)