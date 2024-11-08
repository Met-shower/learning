import requests
from lxml import etree

# 使用太原租房网平替
url = "https://ty.zu.anjuke.com/?pi=baidu-cpchz-ty-tyong1&utm_source=baidu&utm_medium=cpc&kwid=575932794530&utm_term=%e7%a7%9f%e6%88%bf%e7%bd%91%e7%ab%99&opxID=921dfe7a269afebac289e505997819cd&opxSEID=138&opxCAMPAIGNID=67"
resp = requests.get(url)
# print(resp.text)

# 解析成 html
html = etree.HTML(resp.text)

# 拿到每一个服务商的 div
divs = html.xpath('//*[@id="list-content"]/div')
for div in divs:
    price = div.xpath("./div/strong/text()")
    print(price)
    title = div.xpath("./div/h3/a/b/text()")
    print(title)
    mark = div.xpath("./div/p/span/text()")[2:]
    print(mark)
    location = div.xpath("./div/address/a/text()")
    print(location)