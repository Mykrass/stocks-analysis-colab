from yfinance3 import YFinance3
import json

# https://finance.yahoo.com/lookup
#SYMBOLS = ['INTU','CDNS','WDAY','ROP','TEAM','ADSK','DDOG','ANSS','ZM','PTC',\
#           'BSY','GRAB','SSNC','APP','AZPN','MANH','ZI','NICE']

SYMBOLS = ['ADSK','PTC','NICE', 'ADBE', 'AAPL', 'META']

for symbol in SYMBOLS:
    data = YFinance3(symbol)
    file_name = f'out/info/{symbol}.json'
    # Use a context manager to open the file and write the JSON data to it
    with open(file_name, 'w') as file:
        json.dump(data.info, file)
    print('saved to {}'.format(file_name))
