import asyncio
import time

async def func1():
    print("my name is mike")
    await asyncio.sleep(2)
    print("MY NAME IS MIKE")

async def func2():
    print("my name is bob")
    await asyncio.sleep(3)
    print("MY NAME IS alice")

async def func3():
    print("my name is bob")
    await asyncio.sleep(4)
    print("MY NAME IS ALICE")

async def main():
    tasks = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    await asyncio.wait(tasks)

if __name__ == "__main__":
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)