import requests

query = input('输入一个你喜欢的明星')

url = f'https://www.sogou.com/web?query={query}'


dic = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

# 加一个请求头
# 使用 User-Agent 来伪装爬虫程序
resp = requests.get(url, headers=dic) # 处理一个反爬

print(resp)
print(resp.text)