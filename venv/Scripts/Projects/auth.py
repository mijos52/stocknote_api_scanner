import requests
import json

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

requestBody={
  "userId": "DM40435",
  "password": "^!U3DTnCfv*",
  "yob": "1996"
}

r = requests.post('https://api.stocknote.com/login'
, data=json.dumps(requestBody)
, headers = headers)

def token():
  auth_response = r.json()
  key = auth_response['sessionToken']
  return key