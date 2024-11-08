from idlelib.iomenu import encoding
from urllib.request import urlopen

url = 'http://www.baidu.com'

# 得到响应
resp = urlopen(url)

# # 读取网址内容 # print(resp.read())

# 使用 encoding 对open 进行编码
with open('mybaidu.html', mode='w', encoding='utf-8') as f:
    f.write(resp.read().decode('utf-8'))
print('over')


