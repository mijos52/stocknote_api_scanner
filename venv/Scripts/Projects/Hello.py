# Test code no google sheets libs
import auth
import aiohttp
import asyncio
import stocks_list
import json
from pprint import  pprint
# Get change% from  api(getQuote) and sort the list
headers = {
    'Accept': 'application/json',
    'x-session-token': auth.token()
}

stocks = stocks_list.stocks_list()
stockss =[]
i = 0
while i <5:
    stockss.append(stocks[i])
    i+=1

def get_tasks(session):
    tasks = []
    for i in stockss:
        tasks.append(session.get('https://api.stocknote.com/quote/getQuote', params={'symbolName': i},
                                 headers=headers))
    return tasks


results = []
async def symbol():
    async with  aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses =  await asyncio.gather(*tasks)
        for response in responses:
            print (await response.json())

loop = asyncio.get_event_loop()
loop.run_until_complete(symbol())

# asyncio.run(symbol())

