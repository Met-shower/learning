import csv
import requests
from lxml import etree
import asyncio
import aiohttp
import aiofiles

# 网页源代码
def Get_Url(headers):
    href = []
    for i in range(0, 251, 25):
        # 访问每个主页面
        url = f"https://movie.douban.com/top250?start={i}&filter="
        resp = requests.get(url, headers=headers)

        # 提取每个子页面的xpath
        main_page = etree.HTML(resp.text)

        for num in range(1, 26):
            href += main_page.xpath(f'//*[@id="content"]/div/div[1]/ol/li[{num}]/div/div[1]/a/@href')

        print(f'爬取{i}')
        resp.close()
    return href


# 提取网页信息
def Get_Mess(headers, url):

    resp = requests.get(url, headers=headers)

    # print(resp.text)
    lxml = etree.HTML(resp.text)

    all_dic = {}

    # 提取排名和名字
    '//*[@id="content"]/div[1]/span[1]'
    rank = lxml.xpath(f'//*[@id="content"]/div[1]/span[1]/text()')
    all_dic['rank'] = rank[0]
    name = lxml.xpath(f'//*[@id="content"]/h1/span[1]/text()')
    all_dic['name'] = name[0]

    # 主要细节信息 导演 编剧 主演
    label = []
    message = []
    for fun in range(1, 4):
        # 标签
        label = lxml.xpath(f'//*[@id="info"]/span[{fun}]/span[1]/text()')
        message = lxml.xpath(f'//*[@id="info"]/span[{fun}]/span[2]/a/text()')
        messages = '、'.join(message)
        all_dic[label[0]] = messages

    # 剩余细节信息
    all = lxml.xpath('//*[@id="info"]/span[@class="pl"]')
    # print(all)

    mess = lxml.xpath('//*[@id="info"]/span/text()')
    # 提取表头
    label2 = []
    for eve in range(len(all) + 1):
        label2 += lxml.xpath(f'//*[@id="info"]/span[@class="pl"][{eve}]/text()')

    # 数据写入字典
    for i in range(len(all)):
        index1 = mess.index(label2[i])
        if i != len(all) - 1:
            index2 = mess.index(label2[i + 1])
        else:
            index2 = len(all)

        # 将合并后的数据写入字典
        all_dic[label2[i]] = '、'.join(mess[index1 + 1: index2])

    # 故事简介
    summary = lxml.xpath('//*[@id="link-report-intra"]/span[1]/text()')
    # end = ''
    # for sum in range(len(summary)):
    #     summary = summary[sum]
    #     end = ','.join(summary)
    all_dic['summary'] = summary

    # 评分
    rating = lxml.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
    all_dic['rating'] = rating

    # 评价人数
    votes = lxml.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()')
    all_dic['votes'] = votes

    # 星级人数
    for win in range(5):
        all_dic[f'{5 - win}星'] = lxml.xpath(f'//*[@id="interest_sectl"]/div[1]/div[3]/div[{win + 1}]/span[2]/text()')[0]

    resp.close()

    return all_dic

def download():
    pass



if __name__ == '__main__':

    headers =  {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
    }

    # 每一部电影的url
    get_url = Get_Url(headers)  # 列表形式
    print(get_url)


    # 提取网页信息
    # for url in get_url:
    get_mess = Get_Mess(headers, get_url[2])
    print(get_mess)

    num = 1
    for url in get_url:
        get_mess = Get_Mess(headers, url)

        # 写入文件
        header = ['rank', 'name', 'summary', 'rating', 'votes', 'weights', '导演', '编剧', '主演', '类型:',
                  '制片国家/地区:', '语言:', '上映日期:', '片长:', '又名:', 'IMDb:', '1星', '2星', '3星', '4星', '5星', '官方网站:']
        with open(f'movies/{get_mess['rank']}.csv', 'w', encoding='utf-8') as f:
            get_mess = [get_mess]
            writer = csv.DictWriter(f, header)
            writer.writeheader()

            for row in get_mess:
                writer.writerow(row)

            f.close()

        # 记录电影数
        num += 1
        print(f'{num}------------over')