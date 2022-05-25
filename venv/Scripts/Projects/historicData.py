import requests
import auth
from datetime import date
from pprint import  pprint

headers = {
  'Accept': 'application/json',
  'x-session-token': auth.token()
}

# Get todays date and convert it into string
# day = (str(date.today()))
from_day = "2020-03-01"
to_day = "2020-03-25"


'''intrady candle data is limited to time apis dose not provide full data but could be used to make scanner '''

r = requests.get('https://api.stocknote.com/intraday/candleData', params={
  'symbolName': ['WIPRO'],  'fromDate': '%s 09:15:00'%from_day , 'toDate': '%s 09:15:00'%to_day , 'interval': '5' ,
}, headers = headers)

pprint (r.json())
