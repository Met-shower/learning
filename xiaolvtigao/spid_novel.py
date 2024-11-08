
# https://dushu.baidu.com/api/pc/getCatalog?data={"22book_id":"4306063500"}  # => 得到所有章节的内容（名称，cid）

# 小说的具体内容
# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}

import requests
import asyncio
import aiohttp
import json
import aiofiles

async def aiodownload(cid, book_id, title):
    data = {
        "book_id":book_id,
        "cid":f"{book_id}|{cid}",
        "need_bookinfo":1
    }
    data = json.dumps(data)  # 将 data 变成 json 字符串
    url = f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = resp.json()

            async with aiofiles.open("novels/" + title, 'w', encoding='utf-8') as f:
                # await f.write(dic["data"]['novel']['content'])  # 把小说内容写入
                content = dic['data']['novel']['content']
                await f.write(content)

                # await f.write(dic['data']['novel']['content'])

async def getCatalog(url):
    resp = requests.get(url, verify=False)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:
        title = item['title']
        cid = item['cid']
        # 准备异步任务
        tasks.append(asyncio.create_task(aiodownload(cid, book_id, title)))

    await asyncio.wait(tasks)

if __name__ == '__main__':
    book_id = "4306063500"
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+ book_id +'"}'
    asyncio.run(getCatalog(url))
