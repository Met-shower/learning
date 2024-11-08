# python编写协程的程序
import asyncio
import time



#
# async def func():
#     print("hello,my name is 协程")
#
# if __name__ == '__main__':
#     g = func()  # 此时函数是异步协程函数，函数执行得到的是一个协程对象
#     asyncio.run(g)  # 协程程序运行需要 asyncio 模块的支持




# async def func():
#     print("hello, my name is Mike")
#     # time.sleep(3)  # 当程序出现了同步操作的时候，异步就中断了
#     await asyncio.sleep(3)  # 异步操作的代码
#     print("hello, my name is Mike")
#
# async def func2():
#     print("hello, my name is ------")
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print("hello, my name is Mike")
#
# async def func3():
#     print("hello, my name is ^^^^^^")
#     # time.sleep(4)
#     await asyncio.sleep(4)
#     print("hello, my name is Mike")
#
# if __name__ == '__main__':
#     # f1 = func()
#     # f2 = func2()
#     # f3 = func3()
#     tasks = [
#         # asyncio.create_task(func()),
#         asyncio.create_task(func2()),
#         asyncio.create_task(func3()),
#     ]
#     t1 = time.time()
#     # 一次性启动多个任务（协程）
#
#     # 以下代码因为版本太新，出现报错
#     asyncio.run(asyncio.wait(tasks))  # 固定搭配
#     # 使用下面的进行异步协程
#     # asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
#
#     t2 = time.time()
#     print(t2-t1)





async def func():
    print("hello, my name is Mike")
    await asyncio.sleep(3)  # 异步操作的代码
    print("hello, my name is Mike")

async def func2():
    print("hello, my name is ------")
    await asyncio.sleep(2)
    print("hello, my name is Mike")

async def func3():
    print("hello, my name is ^^^^^^")
    await asyncio.sleep(4)
    print("hello, my name is Mike")

# 协程对象
async def main():
    # # 第一种写法（）不推荐
    # f1 = func()
    # # 一般await挂起操作放在协程对象前
    # await f1 # await 一般在函数里

    # 将协程对象包装创建为协程任务
    tasks = [
        asyncio.create_task(func()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    # await asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())







