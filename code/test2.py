from code.test import int_lis

num = 54005.1234
lit = str(num).split('.') # ['54005', '1234']

# 对整数进行千分位转换
int_lis = ''
n = 1
for i in str(lit[0])[::-1]:
    int_lis.(i)
    if n % 3 == 0:
        int_lis.append(',')
    n += 1
int_lis.reverse()


