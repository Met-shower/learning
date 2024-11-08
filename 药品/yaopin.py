import asyncio

import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

async def Get_Url():
    # 所有子页面代码
    urls = []

    for num in range(100):   # 最后范围改成100
        # 4 为查找药品种类编号
        url = f'https://www.dayi.org.cn/list/4/{num + 1}'
        resp = requests.get(url, headers=headers)
        resp.encoding = 'utf-8'
        main_page = etree.HTML(resp.text)
        for i in range(19):
            tag = main_page.xpath(f'//*[@id="global"]/div[2]/div[3]/div[1]/div[1]/div/div[{i + 1}]/div[1]/div/a/@href')[0]
                                    # //*[@id="global"]/div[2]/div[3]/div[1]/div[1]/div/div[1]/div[1]/div/a
            # 拼接子页面代码
            son_page = 'https://www.dayi.org.cn' + tag
            urls.append(son_page)
        print(urls)
        resp.close()

    return urls


# 得到每个药品信息
async def Get_Content(url):
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    main_page = etree.HTML(resp.text)
    # 成分
    comp = main_page.xpath('//*[@id="global"]/div[2]/div[3]/div[1]/div/article/div[3]/div[1]/div/div[3]/p/text()')
    # 性状
    chara = main_page.xpath('//*[@id="global"]/div[2]/div[3]/div[1]/div/article/div[3]/div[2]/div/div[3]/p/text()')
    # 主要功效
    main_bene = main_page.xpath('//*[@id="global"]/div[2]/div[3]/div[1]/div/article/div[3]/div[4]/div/div[3]/p/text()')
    # 适应病症
    adap_ill = main_page.xpath('//*[@id="global"]/div[2]/div[3]/div[1]/div/article/div[3]/div[5]/div/div[3]/p/text()')
    # 用法用量
    usage = main_page.xpath('//*[@id="global"]/div[2]/div[3]/div[1]/div/article/div[3]/div[9]/div/div[3]/p/text()')
    # 注意事项
    pre_cares = main_page.xpath('//*[@id="global"]/div[2]/div[3]/div[1]/div/article/div[3]/div[12]/div/div[3]/p/text()')
    # 贮藏方法
    store = main_page.xpath('//*[@id="global"]/div[2]/div[3]/div[1]/div/article/div[3]/div[16]/div/div[3]/p/text()')
    # 保质期
    time = main_page.xpath('//*[@id="global"]/div[2]/div[3]/div[1]/div/article/div[3]/div[17]/div/div[3]/text()')
    # 执行标准
    stand = main_page.xpath('//*[@id="global"]/div[2]/div[3]/div[1]/div/article/div[3]/div[18]/div/div[3]/p/text()')
    # 含量测定
    hplc = main_page.xpath('//*[@id="global"]/div[2]/div[3]/div[1]/div/article/div[3]/div[22]/div/div[3]/p/text()')

    all = [comp, chara, main_bene, adap_ill, usage, pre_cares, store, time, stand, hplc]
    key = ['comp', 'chara', 'main_bene', 'adap_ill', 'usage', 'pre_cares', 'store', 'time', 'stand', 'hplc']
    dic = {key[i]: all[i] for i in range(len(key))}

    print(f'完成{url}')

async def Down_Load(urls):
    tasks = []
    for i in range(len(urls)):
        url = urls[i]
        # 准备异步任务
        tasks.append(asyncio.create_task(Get_Content(url)))
    await asyncio.wait(tasks)

if __name__ == '__main__':

    get_url = asyncio.run(Get_Url())

    asyncio.run(Down_Load(get_url))

