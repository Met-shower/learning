# 规律求和：输入 1~9 的数字 a，与计算次方 b，输出 a^b。(至少两种方法，每种方法用一个函数)。

# 方法一：使用列表推导式(求和）
list = [x ** y for x in range(1, 10) for y in range(1, 10)]

sum = 0
for i in list:
    sum += i

print(sum)



# 方法二
def index1(a, b):
    num = 1
    for i in range(1, b+1):
        num *= a

    return num

print(index1(2, 3))



# 方法三
def index2(a, b):
    return a ** b

print(index2(2, 3))