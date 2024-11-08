# 给出一个三位数，输出每一位数字


# 方法一：整除求余
def split1(num):

    fir_num = num % 10
    sec_num = int((num / 10) % 10)
    last_num = int(num / 100)

    print(f'百分位数：{last_num}，十位数：{sec_num}，个位数：{fir_num}')

num = int(input('输入一个三位数：'))
a1 = split1(num)



# 方法二：列表
def split2(num):
    list = []
    for i in num:
        list.append(i)
    print(f'百分位数：{list[0]}，十位数：{list[1]}，个位数：{list[2]}')

num = input('输入一个三位数：')
a2 = split2(num)



# 方法三：切片
def split3(num):
    list1 = list(num)
    print(f'百分位数：{list1[:1]}，十位数：{list1[1:2]}，个位数：{list1[2:3]}')


num = input('输入一个三位数：')
split3(num)




