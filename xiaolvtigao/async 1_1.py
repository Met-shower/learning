# request
import asyncio
import aiohttp

urls = [
    "https://umei.ojbkcdn.com/file/bizhi/20220927/joakkzevt3p.jpg",
    "https://umei.ojbkcdn.com/file/bizhi/20220927/cdaiva3dshz.jpg",
    "https://umei.ojbkcdn.com/file/bizhi/20220927/wvt0jrnt04u.jpg"
]

async def download(url):
    name = url.split('/')[-1]
    # 发送请求，得到图片内容，保存图片
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # 请求之后写入文件
            with open("imgs/" + name, "wb") as f:
                f.write(await resp.content.read())  # 读取内容是异步的，需要await挂起

    print(name, "搞定")

async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(download(url)))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())
