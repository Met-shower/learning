# 创建空列表
pri_lis = [1]
def PRI(n):
    for i in range(2, n + 1):
        # 判断素数
        a = 2
        while i % a != 0:
            if a == i - 1:
                pri_lis.append(i)
                break
            a += 1
pri = PRI(1000)
print(pri_lis)
