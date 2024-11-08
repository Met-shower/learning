import aiofiles
import requests
import csv
import asyncio
import aiohttp



async def Mess(headers, data, url):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as resp:
            resp.encoding = 'utf-8'
            list_row = (await resp.json())['articleList']
            num = 0
            data_list = []
            for element in list_row:
                data_list.append(element)
                print(len(element), f'爬取第{data['Page']}页{num}栏数据')
                num += 1

                # 写入.csv文件
                async with aiofiles.open(f'zhihu/{data["Page"]}and{num}.csv', mode='w', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    await writer.writerow(data_list)
        resp.close()


async def Main(headers, url):
    tasks = []
    page = 1
    for i in range(10):
        # 设置每一页的参数
        data = {
            'searchType': 'MulityTermsSearch',
            'ArticleType': '0',
            'ReSearch': '',
            'ParamIsNullOrEmpty': 'false',
            'Islegal': 'false',
            'Content': '',
            'Theme': '机器学习',
            'Title': '',
            'KeyWd': '',
            'Author': '',
            'SearchFund': '',
            'Originate': '',
            'Summary': '',
            'PublishTimeBegin': '',
            'PublishTimeEnd': '',
            'MapNumber': '',
            'Name': '',
            'Issn': '',
            'Cn': '',
            'Unit': '',
            'Public': '',
            'Boss': '',
            'FirstBoss': '',
            'Catalog': '',
            'Reference': '',
            'Speciality': '',
            'Type': '',
            'Subject': '',
            'SpecialityCode': '',
            'UnitCode': '',
            'Year': '',
            'AcefuthorFilter': '',
            'BossCode': '',
            'Fund': '',
            'Level': '',
            'Elite': '',
            'Organization': '',
            'Order': '1',
            'Page': f'{page}',
            'PageIndex': '',
            'ExcludeField': '',
            'ZtCode': '',
            'Smarts': ''
        }
        tasks.append(asyncio.create_task(Mess(headers, data, url)))
        page += 1
    await asyncio.wait(tasks)

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }
    url = 'https://search.cnki.com.cn/api/search/listresult'
    asyncio.run(Main(headers, url))

