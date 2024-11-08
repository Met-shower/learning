import requests
from lxml import etree

url="https://www.pkulaw.com/case?way=topGuid"
t_url="https://www.pkulaw.com"
session=requests.session()
dic={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'connection': 'keep-alive',
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    "Cookie" : "Hm_up_8266968662c086f34b2a3e2ae9014bf8=%7B%22ysx_yhqx_20220602%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22ysx_hy_20220527%22%3A%7B%22value%22%3A%2206%22%2C%22scope%22%3A1%7D%7D; xCloseNew=20; pkulaw_v6_sessionid=b1ruwspilgymo43xywobtkoo; referer=; Hm_lvt_8266968662c086f34b2a3e2ae9014bf8=1729338846,1729343656; Hm_lpvt_8266968662c086f34b2a3e2ae9014bf8=1729343656; HMACCOUNT=5797425F7C0EEE1F; cookieUUID=cookieUUID_1729343655988"
}
resp = session.get(url,headers=dic)

print(resp.text)
