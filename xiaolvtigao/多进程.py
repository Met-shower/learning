from threading import Thread

def func(name):
    for i in range(1000):
        print("子进度", i)

if __name__ == '__main__':
    t1 = Thread(target=func, args=("周杰伦",))  # 传递参数必须是元组
    t1.start()

    t2 = Thread(target=func, args=("王力宏",))
    t2.start()