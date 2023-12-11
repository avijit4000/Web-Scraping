import requests, pandas as pd
from io import BytesIO

class NSE():
    def __init__(self, timeout=10) ->None:
        self.base_url='https://www.nseindia.com'
        self.headers={
            "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"
        }
        self.timeout=timeout
        self.cookies=[]
    def __getCookies(self,renew=False):
        if len(self.cookies) > 0 and renew == False:
            return self.cookies

        r=requests.get(self.base_url,timeout=self.timeout,headers=self.headers)
        self.cookies=dict(r.cookies)
        return self.__getCookies()
    def getHistoricalData(self, symbol , series, from_date, to_date):
        try:
            url='/api/historical/cm/equity?symbol={0}&series=[%22{1}%22]&from={2}&to={3}&csv=true'.format(symbol.replace('&','%26'),series,from_date.strftime('%d-%m-%Y'))
            response=requests.get(self.base_url+url,headers=self.headers,timeout=self.timeout,cookies=self.__getCookies())
            if response.status_code !=200:
                response=requests.get(self.base_url+url,headers=self.headers,timeout=self.timeout,cookies=self.__getCookies(True))

            df=pd.read_csv(BytesIO(response.content),sep=',',thousands=',')
            df=df.rename(columns={'Date':'date','series':'series','OPEN':'open','HIGH':'high','LOW':'low',
                                  'PREV.CLOSE':'prev_close','ltp':'ltp','close':'close','52W H':'hi_52_wk','52W L':'lo_52_wk',
                                  'VOLUME':'volume','VALUE':'value','No of trades':'trades'})
            df.date=pd.to_datetime(df.date).dt.strftime('%Y-%m-%d')
            return df
        except:
            print('Exception occur while fetching historical data from NSE ')
            return None
if __name__=='__main__':
    from datetime import date
    from nse_data import NSE
    api=NSE()
    df=api.getHistoricalData('SBIN','EQ',date(2023,4,6),date(2023,8,23))
    print(df)