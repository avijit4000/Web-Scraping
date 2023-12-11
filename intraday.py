import requests
from datetime import datetime
from time import sleep
import pandas as pd

class MControlAPI:
    def __int__(self,symbol,resolution=1,data_from=None,date_to=datetime.now())->None:
        self.symbol=symbol
        self.resolution=resolution
        self.date_to=int(date_to.timestamp())
        self.resolution_df={
            "1":60,"3":180,"5":300,"15":900,"30":1800,
            "60":3600,"300":18000,"D":24*3600,"W":7*24*3600,
            "M":30*24*3600,"45":45*24*3600,"120":120*24*3600,"240":240*24*3600

        }
        self.delta_time=self.resolution_df[str(self.resolution)]
        if data_from==None:
            self.data_from=self.data_to-self.delta_time*400
        else:
            self.data_from=int(data_from.timestamp())
        self.session=requests.session.Session()
        self.session.headers['User-Agent']: 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'
        self.session.get('https://www.moneycontrol.com/stocksmarketsindia/')
        self.symbol_meta=None
        self.dataframe=[]
    def fetch_symbol_meta(self):
        if self.symbol_meta==None:
            self.symbol_meta=self.session.get('https://priceapi.moneycontrol.com/techCharts/indianMarket/stock/symbols?symbol='+self.symbol)
        return self.symbol_meta
    def fetch_intraday_data(self,countback=None):
        new_data=0
        try:
            if countback == None:
                countback=int((self.data_to-self.data_from)/self.delta_time)
                if countback>330:
                    countback=330
            resp=self.session.get('https://priceapi.moneycontrol.com/techCharts/indianMarket/stock/history?'+
                                  'symbol={0}&resolution={1}&from={2}&to={3}&countback={4}'.format(
                                      self.symbol,self.resolution,self.data_from,self.date_to,countback))
            data=resp.json()
            if data['s']=='no_data':
                return -1
            df=pd.DataFrame.from_dict(data)
            df['dt']=pd.to_datetime(df['t']+19800,unit='s')

            if len(self.dataframe)==0:
                self.dataframe=df.copy()
                new_data=n
            else:
                df=pd.concat([self.dataframe,df[df['t'].isin(self.dataframe['t'])==False]]).reset_index(drop=True)
                self.dataframe=df.copy()
                new_data=len(self.dataframe)-n
            self.data_from=self.data_to
            self.data_to+=self.delta_time


        except Exception as ex:
            new_data=-1
            print(ex)
        return  new_data
if __name__=='__main__':
    from pprint import pprint
    obj=MControlAPI('SBIN')
    nd=0
    while nd>-1:
        nd=obj.fetch_intraday_data()
        if nd>0:
            pprint(obj.dataframe)
            last=obj.dataframe.iloc[-1:].iloc[0]['dt']
            if (last.hour+last.minute/60)>15.5:
                print('Market is closed')
                break
        sleep(obj.delta_time)
