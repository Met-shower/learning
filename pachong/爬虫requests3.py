import requests

url = 'https://movie.douban.com/j/chart/top_list'

# 重新封装参数
param = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': ',',
    'limit': '20'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

resp = requests.get(url=url, params=param, headers=headers)

# print(resp.request.headers)
# # {'User-Agent': 'python-requests/2.27.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
# # 这个不是用户标头

print(resp.text)
resp.close()