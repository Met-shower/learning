# 创建空列表
list1 = []
list2 = []

# 输入列表
n = int(input("列表长度: "))
for i in range(n):
    num = input(f'输入第{i + 1}个列表元素：')
    list1.append(num)
print(list1)

# 输入下标
for i in range(2):
    num = input(f'输入第{i + 1}个下标：')
    list2.append(num)
print(list2)

lit = list1[int(list2[0]) : int(list2[1]) + 1]
print(lit)