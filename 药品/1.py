from traceback import print_tb

from lxml import etree

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

url = 'https://www.dayi.org.cn/cmedical/302511.html'
resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'
main_page = etree.HTML(resp.text)
# 功能
comp = main_page.xpath(
    '//*[@id="global"]/div[2]/div[3]/div[1]/div/article/div[3]/div[1]/section/div[2]/div/div[2]/p/text()')
# 主治
chara = main_page.xpath(
    '//*[@id="global"]/div[2]/div[3]/div[1]/div/article/div[3]/div[1]/section/div[3]/div/div[2]/p/text()')
# 药理作用
main_bene = main_page.xpath(
    '//*[@id="global"]/div[2]/div[3]/div[1]/div/article/div[3]/div[1]/section/div[9]/div/div[2]/p/text()')
# 相关配伍
adap_ill = main_page.xpath(
    '//*[@id="global"]/div[2]/div[3]/div[1]/div/article/div[3]/div[2]/section/div[3]/div/div[2]/p[1]/text()')
# 用法用量
usage = main_page.xpath(
    '//*[@id="global"]/div[2]/div[3]/div[1]/div/article/div[3]/div[1]/section/div[4]/div/div[2]/p/text()')
# 注意事项
pre_cares = main_page.xpath(
    '//*[@id="global"]/div[2]/div[3]/div[1]/div/article/div[3]/div[1]/section/div[7]/div/div[2]/p/text()')
print(comp, chara, main_bene, adap_ill, usage, pre_cares)