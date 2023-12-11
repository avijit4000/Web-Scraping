from bs4 import BeautifulSoup as bs
import requests as re
import pandas as pd
con=re.get('https://www.google.com/finance/markets/gainers?authuser=0').text
soup=bs(con,'lxml')
box=soup.find_all("li")
name=[]
price=[]
increase=[]
pseincre=[]
for i in box:
    name.append(i.find("div",class_="ZvmM7").text)
    price.append(i.find("div",class_="YMlKec").text)
    increase.append(i.find("span",class_="P2Luy Ez2Ioe").text)
    pseincre.append(i.find("span",class_="V53LMb").text)
df=pd.DataFrame({"name":name,"price":price,"increase":increase,"pseincre":pseincre})
print(df)




