import requests


headers = {
  'Accept': 'application/json',
  'x-session-token': '10513ba122cedc61cb52685ebb09e0cb'
}

r = requests.get('https://api.stocknote.com/intraday/candleData', params={
  'symbolName': 'INFY',  'fromDate': '2021-09-20 10:00:00' ,  'interval'  : '30'
}, headers = headers)

print(r)