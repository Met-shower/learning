# 拿到页面源代码
# 通过re提取内容

import requests
import re
# 存储数据为 csv 格式
import csv

url = "https://movie.douban.com/chart"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
}

resp = requests.get(url, headers=headers)

# 页面源代码
page_content = resp.text

# 解析数据
obj = re.compile(r'</table>.*?<div class=.*? class="">(?P<name>.*?)'
                 r' / <span.*?<p class="pl">(?P<year>\d+).*?'
                 r'<span class="rating_nums">(?P<score>.*?)</span>', re.S)

# 开始匹配
result = obj.finditer(page_content)

# 准备写入数据
f = open('data.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(f)

for i in result:
    # print(i.group("name"), i.group("year"), i.group("score"))
    dic = i.groupdict()
    dic['year'] = dic['year'].strip()
    csv_writer.writerow(dic.values())

f.close()
resp.close()
print('over')