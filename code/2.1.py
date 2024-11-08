# 输入： ‘aaa      bb    c   d   e    fff     ’
# 输出： ‘aaa bb c d e fff’
import re



a = 'aaa      bb    c   d   e    fff'

# 方法一：列表
def remo1(exm):

    # 去除空格
    list = []
    for i in exm:
        if i != ' ' or (i ==' ' and i != list[-1]) :
            list.append(i)

    if list[-1] == ' ':
        list.pop()

    # 转换为字符串类型
    str = ''
    for i in list:
        str += i
    return str



# 方法二 join
def remo2(exm):
    list_exm = exm.split()
    new_lit = ' '.join(list_exm)
    return new_lit




# 方法三 正则表达式
def remo3(exm):
    new_lt = re.split('\s+', a)
    back = ' '.join(new_lt)
    return back



# 测试
back = remo3(a)
if back == 'aaa bb c d e fff':
    print('测试成功')
else:
    print('测试失败')
