from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# 使用线程池进行执行
def fn(name):
    for i in range(1000):
        print(name, i)

if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(max_workers=50) as t:  # 线程池中最多的线程
         for i in range(100):
             t.submit(fn, name=f"线程{i}")
    # 等待线程池中的任务全部执行完毕，才继续执行（守护）
    print("123")
