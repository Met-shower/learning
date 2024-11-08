# 单线程程序
def func():
    for i in range(1000):
        print("func", i)

if __name__ == '__main__':
    func()
    for i in range(1000):
        print("main", i)



# 实现多线程 第一个写法
from threading import Thread  # 线程类

def func():
    for i in range(1000):
        print("func", i)

if __name__ == '__main__':
    t = Thread(target=func)  # 创建线程并给线程安排任务
    t.start()   # 开始执行单线程：给计算机添加一个状态，可以开始工作
                # t.start() 多线程状态为可以开始工作的状态，具体执行时间由CPU决定
    t2 = Thread(target=func)  # 创建第二个线程
    t2.start()

    for i in range(1000):
        print("main", i)



# 实现多线程的第二个方法
from threading import Thread

class MyThread(Thread):
    def run(self):           # 当线程被执行的时候，被执行的就是run()
        for i in range(1000):
            print("子线程", i)

if __name__ == '__main__':
    t = MyThread()
    # t.run()  # 方法的调用 -> 单线程
    t.start()  # 开启线程

    for i in range(1000):
        print("主线程", i)
