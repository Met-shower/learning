# 抓取单个页面数据
# 线程池同时抓取多个页面数据

import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor


f = open("data.csv", mode='w', encoding='utf-8')
csv_writer = csv.writer(f)

def download_one_page(url):
    resp = requests.get(url)
    resp.encoding = "utf-8"
    html = etree.HTML(resp.text)
    # 将列表中的数据拿出来
    div_one_page = html.xpath('//*[@id="infinite_scroll"]')[0]
    # print(div_one_page)
    one_blank_div = div_one_page.xpath('./div')
    # print(len(one_blank_div))

    # 拿到每个div
    for div in one_blank_div:
        # 使用 position() 来获取除去第一个div外的其他div
        txt = div.xpath("./div[position()>1]/div/span/a/text()")
        # 把列表分割开
        txt = txt[0].split('，')
        # print(txt)
        # 把数据存放在文件中
        csv_writer.writerow(txt)

    print(url, " 提取完毕！")

if __name__ == '__main__':
    # # 效率低下的处理方式
    # for i in range(1, 539):
    #     download_one_page(f"https://www.umei.cc/bizhitupian/fengjingbizhi/index_{i}.htm")  # 传入网站的 url

    # 创建线程池
    with ThreadPoolExecutor(max_workers=50) as t:
        for i in range(1, 200):
            # 把下载任务提交给线程池
            t.submit(download_one_page, f"https://www.umei.cc/bizhitupian/fengjingbizhi/index_{i}.htm")

    print("全部下载完毕")