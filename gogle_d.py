from bs4 import BeautifulSoup as bs
import requests as re
import pandas as pd

contes=re.get('https://www.google.com/finance/markets/gainers?authuser=0').text
soup=bs(contes,'lxml')