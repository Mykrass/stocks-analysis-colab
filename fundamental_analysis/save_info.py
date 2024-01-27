from yfinance3 import YFinance3
import json

#SYMBOLS = ['INTU','CDNS','WDAY','ROP','TEAM','ADSK','DDOG','ANSS','ZM','PTC',\
#           'BSY','GRAB','SSNC','APP','AZPN','MANH','ZI','NICE']
# https://www.six-group.com/en/products-services/the-swiss-stock-exchange/market-data/statistics/intraday-activity-swissatmid/blue-chip-shares.html
#SYMBOLS = ['NESN', 'NOVN', 'SCMN', 'UHR', 'ABBN', 'SIKA', 'GEBN', 'KNIN']
# https://uk.wikipedia.org/wiki/NASDAQ-100
SYMBOLS = ['FB','GOOGL', 'AMZN', 'AAPL', 'CSCO', 'INTU', 'MSFT', 'ADSK']

for symbol in SYMBOLS:
    data = YFinance3(symbol)
    file_name = f'out/info/{symbol}.json'
    # Use a context manager to open the file and write the JSON data to it
    with open(file_name, 'w') as file:
        json.dump(data.info, file)
    print('saved to {}'.format(file_name))
