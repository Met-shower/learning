import requests

url = "https://www.baidu.com/"

# 111.1.61.47
#proxies = {"https": "https://111.1.61.47"}

proxies = {"https": "https://111.1.61.47"}

resp = requests.get(url, proxies=proxies)
resp.encoding = 'utf-8'
# print(resp.text)