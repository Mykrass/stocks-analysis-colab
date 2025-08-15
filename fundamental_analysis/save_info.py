from yfinance3 import YFinance3
import json

# https://finance.yahoo.com/lookup
#SYMBOLS = ['INTU','CDNS','WDAY','ROP','TEAM','ADSK','DDOG','ANSS','ZM','PTC',\
#           'BSY','GRAB','SSNC','APP','AZPN','MANH','ZI','NICE']

# Data Centers https://www.youtube.com/watch?v=Od6_Val6C5g
# https://www.google.com/search?q=data+centers+company+tickers&rlz=1C5CHFA_enCH1007CH1007&oq=data+centers+company+tickers&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigAdIBCTI0NzY2ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8
SYMBOLS = ['MSFT', 'ORCL', 'NVDA', 'AVGO', 'VRT', 'GDS', 'DTST', 'AMT', 'IRM', 'EQIX', 'DLR'] # 'COR', 'QTS', 'CONE'

for symbol in SYMBOLS:
    data = YFinance3(symbol)
    file_name = f'out/info/{symbol}.json'
    # Use a context manager to open the file and write the JSON data to it
    with open(file_name, 'w') as file:
        json.dump(data.info, file)
    print('saved to {}'.format(file_name))
