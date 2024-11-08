import requests
from bs4 import BeautifulSoup

url = "http://www.shucai123.com/price/"
resp = requests.get(url)


# 解析数据
# 1.把页面源代码交给BeautifulSoup处理，生成bs对象
page = BeautifulSoup(resp.text, "html.parser") # 指定 html 解析器
# print(page)

# 2.从bs对象中查找数据
# find(标签， 属性=值)
# find_all(标签, 属性=值)
table = page.find("table", {"class": "bjtbl"})
print(table)
# 拿到所有数据行
trs = table.find_all("tr")[1:]
for tr in trs:
    tds = tr.find_all("td")
    date = tds[0].text # .text 表示拿到被标签标记的内容
    loca = tds[1].text
    kind = tds[2].text
    fut = tds[3].text
    person = tds[4].text
    more = tds[5].text
    print(date, loca, kind, fut, person, more)
