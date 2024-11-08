import re
import requests
from lxml import etree

num = 1
url = f'https://s.weibo.com/weibo?q=%E6%9D%A8%E5%88%A9%E4%BC%9F%E7%9A%84%E5%A4%AA%E7%A9%BA%E4%B8%80%E6%97%A5&page={num}'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'Cookie': 'PC_TOKEN=8c0baf0513; _s_tentry=security.weibo.com; appkey=; Apache=9277284148470.64.1729681539203; SINAGLOBAL=9277284148470.64.1729681539203; ULV=1729681539205:1:1:1:9277284148470.64.1729681539203:; SCF=AtxSdASbuNk4W6NqKIjU-m3zxpFxVcQd6BTJuWI5_9X_BZV09Tt74-6aM9dm302cWbw3PhhOOFeT-f-IhGFGTvc.; SUB=_2A25KHKitDeRhGeFM7FIV-SzMwzSIHXVpU6RlrDV8PUNbmtB-LWTckW9NQK8mznOH5HL4oRWLG5grpA-fiKExn5hs; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5gThUMvnI0kK8s7aBj0LuM5NHD95QNeoM7Sh.EehnRWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0zNehB4eo5R15tt'
}

resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'

# print(resp.text)

# ip名字
# obj = re.compile(r'<div class="from"  >.*?">(?P<time>.*?)</a>.*?<p class="txt" node-type="feed_list_content" nick-name="(?P<name>.*?)"')
obj = re.compile(r'wb_time">(?P<time>.*?)</a>')

result = obj.findall(resp.text)
print(result)
# for match in result:
#     time = match.group('time')
#     print(time)


resp.close()
