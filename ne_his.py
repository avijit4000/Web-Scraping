#Stock history
from nsepy import get_history
from datetime import date
sbin = get_history(symbol='SBIN',
                    start=date(2015,1,1),
                    end=date(2015,1,10))
sbin[[ 'VWAP', 'Turnover']].plot(secondary_y='Turnover')

"""	Index price history
	symbol can take these values (These indexes have derivatives as well)
	"NIFTY" or "NIFTY 50",
	"BANKNIFTY" or "NIFTY BANK",
	"NIFTYINFRA" or "NIFTY INFRA",
    	"NIFTYIT" or "NIFTY IT",
    	"NIFTYMID50" or "NIFTY MIDCAP 50",
    	"NIFTYPSE" or "NIFTY PSE"
	In addition to these there are many indices
	For full list refer- https://www.nseindia.com/products/content/equities/indices/historical_index_data.htm
"""
nifty = get_history(symbol="NIFTY",
                    start=date(2015,1,1),
                    end=date(2015,1,10),
					index=True)
nifty[['Close', 'Turnover']].plot(secondary_y='Turnover')