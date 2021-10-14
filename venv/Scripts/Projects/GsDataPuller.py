import quickstart
import auth
import aiohttp
from pprint import pprint
import asyncio

# Sheets auth from quickstart.py / sheetId and SheetRange
x = '1WTSfd11rji1QJQiBrkV8WbE_vK8GXpxhHwlBffSASCY'
y = 'Names!C1:C394'

# Get change% from  api(getQuote) and sort the list
headers = {
    'Accept': 'application/json',
    'x-session-token': auth.token()
}

# pull all the name from the sheet store in "Names"
sheet_res = quickstart.authentication(x, y)
NamesBefore = sheet_res["values"]
NamesCount = len(NamesBefore)

# loop for getting the name only in list format(without nse:)
count = 0
list = []
while count < NamesCount:
    result = " ".join(NamesBefore[count])
    result = result.split(":")
    list.append(result[1])
    count += 1


async def symbol(i,count):
   async with  aiohttp.ClientSession() as session:
     while i < count :
         r = await session.get('https://api.stocknote.com/quote/getQuote', params={'symbolName': list[i]}, headers=headers)
         print(await r.json())
         i += 1



loop = asyncio.get_event_loop()
loop.run_until_complete(symbol(0,20))