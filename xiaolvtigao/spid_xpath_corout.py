import csv
import aiofiles
import requests
from lxml import etree
import asyncio
import aiohttp


# 得到子页面的url
async def Get_Son_Url(headers):
    href = []
    for i in range(0, 251, 25):
        url = f"https://movie.douban.com/top250?start={i}&filter="

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as resp:
                main_page = etree.HTML(await resp.text())
                for num in range(1, 26):
                    href += main_page.xpath(f'//*[@id="content"]/div/div[1]/ol/li[{num}]/div/div[1]/a/@href')
                print(f'爬取{i}')
            resp.close()
    return href


# 得到子页面的数据并写入文件
async def Get_Mess(herders, url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            lxml = etree.HTML(await resp.text())

            # 所有的信息
            all_dic = {}
            rank = lxml.xpath(f'//*[@id="content"]/div[1]/span[1]/text()')
            all_dic['rank'] = rank[0]
            name = lxml.xpath(f'//*[@id="content"]/h1/span[1]/text()')
            all_dic['name'] = name[0]

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
                all_dic[f'{5 - win}星'] = \
                lxml.xpath(f'//*[@id="interest_sectl"]/div[1]/div[3]/div[{win + 1}]/span[2]/text()')[0]


            # 写入.csv文件
            async with aiofiles.open(f'movies/{all_dic['rank']}.csv', mode='w', encoding='utf-8') as file:
                writer = csv.writer(file)
                await writer.writerow(all_dic.keys())
                await writer.writerow(all_dic.values())
                print(f'提取{all_dic['rank']}完毕')
        resp.close()

# 将子页面的数据存入为.csv
async def DownLoad(headers, href):
    tasks = []
    # 先拿一个数据进行测试
    for i in range(len(href)):
        url = href[i]
        # 准备异步任务
        tasks.append(asyncio.create_task(Get_Mess(headers, url)))

    await asyncio.wait(tasks)

# 主线程
if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
    }

    href = asyncio.run(Get_Son_Url(headers))
    print(href)
    asyncio.run(DownLoad(headers, href))
