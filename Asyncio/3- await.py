import asyncio

# 3- Using Await 
# In example 2 , we didn't see the hello returned from async_hello function 
# In order to get the value returned from an async function, we use the keyword ```await``` before the function call

async def hello_async():
    print('running hello coroutine')
    return 'hello'

async def main():
    x = await hello_async()
    print(x)

asyncio.run(main()) 

# try :
#     def test():
#         x = await hello_async()
#     test()
# except SyntaxError as e:
#     print(e)