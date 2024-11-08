from lxml import etree

import requests

url = 'https://mzyp.yilianmeiti.com/category/1/0/1.html'
resp = requests.get(url)
resp.encoding = 'utf-8'
main_page = etree.HTML(resp.text)
print(main_page.xpath('/html/body/section[2]/div/div/dl[1]/dt/div[2]/b/a/@href'))
# print(main_page.xpath('/html/body/section[3]/div[2]/div/dl[4]/dd/text()'))
resp.close()

print([]==[])

print(main_page.xpath('/a/b/c') == [])