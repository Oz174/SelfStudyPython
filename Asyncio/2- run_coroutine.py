import asyncio 

# 2- What is a coroutine ? 
# A coroutine is a special function — a function that can be paused and resumed when other tasks are being executed. 
# A coroutine can also temporarily hand over control to some other coroutine.
# Which allows us to execute more than one task at one time concurrently.


async def hello_async():
    # to define a function as asynchronous, we use the keyword ```async``` before the function definition
    print("Running hello_async coroutine ...")
    return 'hello'

# the correct way to run an async function is doing the following 

asyncio.run(hello_async()) # prints 'Running hello_async coroutine ...' only , and not hello 
