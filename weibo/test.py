from lxml import etree

import requests
import re

num = 1
url = f'https://s.weibo.com/weibo?q=%E6%9D%A8%E5%88%A9%E4%BC%9F%E7%9A%84%E5%A4%AA%E7%A9%BA%E4%B8%80%E6%97%A5&page={num}'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'Cookie': 'PC_TOKEN=8c0baf0513; _s_tentry=security.weibo.com; appkey=; Apache=9277284148470.64.1729681539203; SINAGLOBAL=9277284148470.64.1729681539203; ULV=1729681539205:1:1:1:9277284148470.64.1729681539203:; SCF=AtxSdASbuNk4W6NqKIjU-m3zxpFxVcQd6BTJuWI5_9X_BZV09Tt74-6aM9dm302cWbw3PhhOOFeT-f-IhGFGTvc.; SUB=_2A25KHKitDeRhGeFM7FIV-SzMwzSIHXVpU6RlrDV8PUNbmtB-LWTckW9NQK8mznOH5HL4oRWLG5grpA-fiKExn5hs; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5gThUMvnI0kK8s7aBj0LuM5NHD95QNeoM7Sh.EehnRWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0zNehB4eo5R15tt'
}

resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'

#  <a href="//weibo.com/2713131601/OBBZEhdai?refer_flag=1001030103_" target="_blank" suda-data="key=tblog_search_weibo&value=seqid:172982273693001398122|type:1|t:0|pos:1-0|q:%E6%9D%A8%E5%88%A9%E4%BC%9F%E7%9A%84%E5%A4%AA%E7%A9%BA%E4%B8%80%E6%97%A5|ext:cate:26,mpos:1,click:wb_time">
obj = re.compile(r' <a href="(?P<url>.*?)" target="_blank" .*?click:wb_time">')
result = obj.findall(resp.text)

# 组合子页面的url
urls = []
for i in result:
    url = 'https:' + i
    urls.append(url)
# print(urls)


# https://weibo.com/ajax/statuses/show?id=OBBZEhdai&locale=zh-CN  -> 目标
# https://weibo.com/2713131601/OBBZEhdai?refer_flag=1001030103_  -> urls
# 拼接请求头
req_urls = []
for url in urls:
    tag = re.findall(r'weibo.com/.*?/(?P<label>.*?)\?', url)
    req_urls.append(f'https://weibo.com/ajax/statuses/show?id={tag[0]}&locale=zh-CN')
# print(req_urls)


# 访问第一个页面内容
re_url = req_urls[0]
response = requests.get(re_url, headers=headers)
element = response.json()
print(element)

screen_name = element['user']['screen_name']  # 人民日报数字传播
time = element['created_at']
content = element['text_raw']

print(content)

# 图片爬取不到


resp.close()
response.close()