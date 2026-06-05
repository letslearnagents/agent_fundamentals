import asyncio

# Defining a coroutine
async def task1():
    print("1")
    await asyncio.sleep(10)
    print("2")

# Defining another coroutine
async def task2():
    print("3")
    await asyncio.sleep(5)
    print("4")

async def main():
    await asyncio.gather(
        task1(),
        task2()
    )

asyncio.run(main())