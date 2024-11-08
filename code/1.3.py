# 导入随机数模块
import random

# 创建随机数组
list = []
for i in range(20):
    list.append(random.randint(-20, 20))
print(list)

new_list = []

# 前十个升序排列
n = 0
for i in range(10):
    min_num = min(list[:10 - n])
    list.remove(min_num)
    new_list.append(min_num)
    n += 1

# 后十个降序排序
for i in range(10):
    max_num = max(list[:])
    list.remove(max_num)
    new_list.append(max_num)

print(new_list)