import asyncio 

# 1- Regular Function Vs Asychronous Function
def hello():
    return 'hello'

async def hello_async():
    # to define a function as asynchronous, we use the keyword ```async``` before the function definition
    return 'hello'

print("Regular Function Vs Asychronous Function")
print(hello) # prints <function hello at  0x000001E088D69020>
print(hello_async) # prints <function hello_async at 0x000001E088D69120>
print(hello()) # prints 'hello'
print(hello_async()) 
# <coroutine object hello_async at 0x000001E08AB8BB60>
#RuntimeWarning: coroutine 'hello_async' was never awaited print(hello_async())
#RuntimeWarning: Enable tracemalloc to get the object allocation traceback