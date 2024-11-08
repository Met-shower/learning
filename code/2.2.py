# 千分位转换：从数字个位数每三位加一个逗号。（考虑小数情况，尽量使用多种方法，每种方法用一个函数）
# 54,005.123,4


# 方法一
def change(num):
    lit = str(num).split('.')

    # 对整数位进行千分
    int_lis = []
    n = 1
    for i in lit[0][::-1]:
        int_lis.append(i)
        if n % 3 == 0:
            int_lis.append(',')
        n += 1
    int_lis.reverse()
    new_int = ''.join(int_lis)

    # 对小数位进行千分
    # 出现重复数字下标会保持前一个数字下标
    flo_lis = [i if (lit[1].index(i) + 1) % 3 != 0 else i + ',' for i in lit[1]]
    new_flo = ''.join(flo_lis)
    '''
    flo_lis = []
    n = 1
    for i in lit[1]
        flo_lis.append(i)
        if n % 3 == 0:
            flo_lis.append(',')
        n += 1
    new_flo = ''.join(flo_lis)
    '''
    return new_int + '.' + new_flo

a = 54005.123456789
print(change(a))





# 方法二 ：切片
def change2(num):
    lit = str(num).split('.')

    int_num = lit[0]
    float_num = lit[1]

    # 整数部分
    last_num = ''
    while len(int_num) > 3:
        last_num = ',' + int_num[-3:] + last_num
        int_num = int_num[:-3]

    int_part = int_num + last_num

    # 小数部分
    first_num = ''
    while len(float_num) > 3:
        first_num = first_num + float_num[:3] + ','
        float_num = float_num[3:]

    float_part = first_num + float_num

    return int_part + '.' + float_part

print(change2(a))