import requests

url = 'https://fanyi.baidu.com/sug'

s = input('请输入你要翻译的英文单词')

# 负载中查看插入数据
dat = {
    'kw': s
}

# 发送 post 请求发送的数据必须放在字典中，通过 data 参数进行传递
resp = requests.post(url, data=dat)
print(resp.json()) # 将服务器返回的内容直接处理成 json() ==> dict