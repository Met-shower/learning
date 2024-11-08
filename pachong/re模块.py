import re

# lst = re.findall(r'\d+', '我的电话号是：10086，我女朋友的电话号是：10010')
# print(lst)
#
# it = re.finditer(r'\d+', '我的电话号是：10086，我女朋友的电话号是：10010')
# print(it)
# for i in it:
#     print(i)
#
# # 使用group返回match内容
# for i in it:
#     print(i.group())

# s = re.search(r'\d+', '我的电话号是：10086，我女朋友的电话号是：10010')
# print(s)
# print(s)


# s = re.match(r'\d+', '我的电话号是：10086，我女朋友的电话号是：10010')
# print(s)
#
# obj = re.compile(r'\d+')
#
# ret = obj.finditer('我的电话号是：10086，我女朋友的电话号是：10010')
# for i in ret:
#     print(i.group())


# # (?P<分组名字>正则)  可以单独从正则匹配的内容中提取到的内容
# s = ('<div class="jay"><span id="1">郭麒麟</span></div>'
#      '<div class="jj"><span id="2">宋轶</span></div>'
#      '<div class="mike"><span id="3">范思哲</span></div>')


s = '''
<div class="jay"><span id="1">郭麒麟</span></div>
<div class="jj"><span id="2">宋轶</span></div>
<div class="mike"><span id="3">范思哲</span></div>
'''

obj = re.compile(r'<div class=".*?"><span id="(?P<id>\d+)">(?P<wahaha>.*?)</span></div>', re.S)

result = obj.finditer(s)

for i in result:
    print(i.group('id'), i.group('wahaha'))

