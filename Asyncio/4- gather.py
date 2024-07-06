import asyncio

# 4- Using asyncio.gather to run multiple coroutines concurrently

async def hello(period_in_secs):
    print('start')
    print(f'sleeping {period_in_secs} seconds')
    await asyncio.sleep(period_in_secs)
    print('end')

async def main():
    await asyncio.gather(hello(1), hello(2), hello(3))

asyncio.run(main())

#start
#sleeping 1 seconds
#start
#sleeping 2 seconds
#start
#sleeping 3 seconds
#end
#end
#end

# threads weren't allowed to end , hello(1) had to wait for hello(2) to finish , and hello(2) had to wait for hello(3) to finish
