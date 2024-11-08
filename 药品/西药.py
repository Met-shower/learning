import asyncio
import csv

import aiofiles
import aiohttp
import requests
from lxml import etree


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

async def Get_Url():
    # 所有子页面代码
    urls = []

    for num in range(100):   # 最后范围改成100
        # if num == 14 or num ==15 or num == 16:
        #    continue
        # 4 为查找药品种类编号
        url = f'https://mzyp.yilianmeiti.com/category/1/0/{num}.html'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                main_page = etree.HTML(await resp.text())
                for i in range(20):
                    # tag = main_page.xpath(f'//*[@id="global"]/div[2]/div[3]/div[1]/div[1]/div/div[{i + 1}]/div[1]/div/a/@href')[0]
                    # 拼接子页面代码
                    son_page = main_page.xpath(f'/html/body/section[2]/div/div/dl[{i}]/dt/div[2]/b/a/@href')
                    urls.append(son_page)
                    print(num, '+', i)
            resp.close()

    # print(urls)
    print(len(urls))
    return urls # 存放的是每个子页面的药品信息


# 得到每个药品信息
async def Get_Content(url, nu):
    async with aiohttp.ClientSession() as session:
        async with session.get(url[0], headers=headers) as resp:
            main_page = etree.HTML(await resp.text())
    # resp = requests.get(url, headers=headers)
    # resp.encoding = 'utf-8'

            # 名字
            name = main_page.xpath('/html/body/section[2]/div/dl/dd/b/text()')[0]
            # 功能
            comp = main_page.xpath('/html/body/section[5]/div[1]/div[2]/div[1]/p/text()')[0]
            # 规格
            chara = main_page.xpath('/html/body/section[2]/div/dl/dd/p[1]/text()')[0]
            # 成分
            main_bene = main_page.xpath('/html/body/section[3]/div[2]/div/dl[4]/dd/text()')[0]
            # 副作用
            adap_ill = main_page.xpath('/html/body/section[5]/div[3]/div[2]/p/text()')[0]
            # 用法用量
            usage = main_page.xpath('/html/body/section[5]/div[2]/div[2]/p/text()')[0]
            # 注意事项
            pre_cares = main_page.xpath('/html/body/section[5]/div[4]/div[2]/p/text()')[0]

            all = [name, comp, chara, main_bene, adap_ill, usage, pre_cares]
            key = ['name', 'comp', 'chara', 'main_bene', 'adap_ill', 'usage', 'pre_cares']
            dic = {key[i]: all[i] for i in range(len(key))}
            # print(dic)

            # 写入文件
            async with aiofiles.open("所有药品/西药.csv", 'a', encoding='utf-8'):
            # with open("所有药品/中药.csv", 'a', encoding='utf-8') as f:
                writer = csv.writer(f)
                # writer.writerow(dic.keys())
                await writer.writerow(dic.values())
                f.close()

            print(f'完成{nu}')
        resp.close()

async def Down_Load(urls):
    tasks = []
    nu = 1
    for i in range(len(urls)):
        if urls[i] != []:
            url = urls[i]
            # 准备异步任务
            tasks.append(asyncio.create_task(Get_Content(url, nu)))
            nu += 1
    await asyncio.wait(tasks)

if __name__ == '__main__':

    get_url = asyncio.run(Get_Url())

    title = ['name', 'comp', 'chara', 'main_bene', 'adap_ill', 'usage', 'pre_cares']
    with open(f"所有药品/西药.csv", 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(title)
        f.close()
    # nu记录爬取网页的个数
    asyncio.run(Down_Load(get_url))