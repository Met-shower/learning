import csv

import requests
from lxml import etree

def Get_Url():
    # 所有子页面的代码
    urls = []
    for num in range(100):  # 页数
        url = f'https://mzyp.yilianmeiti.com/category/17/0/{num}.html'
        resp = requests.get(url)
        main_page = etree.HTML(resp.text)
        for i in range(20):  # 每页药品数
            son_page = main_page.xpath(f'/html/body/section[2]/div/div/dl[{i}]/dt/div[2]/b/a/@href')
            urls.append(son_page)
            print(num, '+', i)

        resp.close()

    print(len(urls))
    return urls

# 得到每个药品信息
def Get_Content(url, nu):
    resp = requests.get(url[0])
    main_page = etree.HTML(resp.text)

    # 名字
    if main_page.xpath('/html/body/section[2]/div/dl/dd/b/text()') != []:
        name = main_page.xpath('/html/body/section[2]/div/dl/dd/b/text()')[0]
    else:
        name = ['无']
    # 功能
    if main_page.xpath('/html/body/section[5]/div[1]/div[2]/div[1]/p/text()') != []:
        comp = main_page.xpath('/html/body/section[5]/div[1]/div[2]/div[1]/p/text()')[0]
    else:
        comp = ['无']
    # 规格
    if main_page.xpath('/html/body/section[2]/div/dl/dd/p[1]/text()') != []:
        chara = main_page.xpath('/html/body/section[2]/div/dl/dd/p[1]/text()')[0]
    else:
        chara = ['无']
    # 成分
    if main_page.xpath('/html/body/section[3]/div[2]/div/dl[4]/dd/text()') != []:
        main_bene = main_page.xpath('/html/body/section[3]/div[2]/div/dl[4]/dd/text()')[0]
    else:
        main_bene = ['无']
    # 副作用
    if main_page.xpath('/html/body/section[5]/div[3]/div[2]/p/text()') != []:
        adap_ill = main_page.xpath('/html/body/section[5]/div[3]/div[2]/p/text()')[0]
    else:
        adap_ill = ['无']
    # 用法用量
    if main_page.xpath('/html/body/section[5]/div[2]/div[2]/p/text()') != []:
        usage = main_page.xpath('/html/body/section[5]/div[2]/div[2]/p/text()')[0]
    else:
        usage = ['无']
    # 注意事项
    if main_page.xpath('/html/body/section[5]/div[4]/div[2]/p/text()') != []:
        pre_cares = main_page.xpath('/html/body/section[5]/div[4]/div[2]/p/text()')[0]
    else:
        pre_cares = ['无']

    all = [name, comp, chara, main_bene, adap_ill, usage, pre_cares]
    key = ['name', 'comp', 'chara', 'main_bene', 'adap_ill', 'usage', 'pre_cares']
    dic = {key[i]: all[i] for i in range(len(key))}

    # 写入文件
    with open("所有药品/西药17.csv", 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(dic.values())
        f.close()

    print(f'完成{nu}')


if __name__ == '__main__':
    get_urls = Get_Url()
    print(get_urls)
    title = ['name', 'comp', 'chara', 'main_bene', 'adap_ill', 'usage', 'pre_cares']
    with open(f"所有药品/西药17.csv", 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(title)
        f.close()

    # 进行计数
    nu = 1
    for url in get_urls:
        if url != []:
            Get_Content(url, nu)
            nu += 1