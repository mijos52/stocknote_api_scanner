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
day = "2021-10-01"


r = requests.get('https://api.stocknote.com/intraday/candleData', params={
  'symbolName': ['WIPRO','INFY','CAMS'],  'fromDate': '%s 09:15:00'%day , 'interval': '5' ,
}, headers = headers)

pprint (r.json())
