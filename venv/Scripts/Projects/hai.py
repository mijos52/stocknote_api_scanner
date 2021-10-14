import asyncio


async def main():
    print('hello')
    task = asyncio.create_task(sec('how are you '))
    await task
    print('finished')

# second funtction with something in that you would want to run simultanioulsy


async def sec(text):
  for i in  range(100):
      print(text)




asyncio.run(main())

