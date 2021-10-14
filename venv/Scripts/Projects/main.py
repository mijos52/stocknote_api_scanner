import requests
headers = {
  'Accept': 'application/json',
  'x-session-token': '7875f26f40370040ae75db51add5bb23'
}

r = requests.get('https://api.stocknote.com/eqDervSearch/search', params={
  'searchSymbolName': 'INFY'
}, headers = headers)

print (r.json())