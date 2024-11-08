# 编写函数，接收一个字符串，分别统计大写字母、小写字母、数字、其他字符的个数，并以元组的形式返回结果。
a = input('输入：')

def sum(s):
    int_num = 0
    up_num = 0
    low_num = 0
    oth_num = 0
    for i in s:
        if '1' <= i <= '9':
            int_num += 1
        elif 'A' <= i <= 'Z':
            up_num += 1
        elif 'a' <= i <= 'z':
            low_num += 1
        else:
            oth_num += 1

    return (up_num, low_num, int_num, oth_num)

back = sum(a)
print(back)
