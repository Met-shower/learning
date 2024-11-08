import requests
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'}

url = ('https://search.cnki.com.cn/api/search/listresult')

page = 1

# 创建空列表
data_list = []

# 得到的数据元素
header = ['dbType', 'assignType', 'tutor', 'cDNo', 'authorCode', 'articleUrl', 'title', 'quoteCount', 'publishTime', 'downloadCount', 'dbSource', 'fileName', 'allowDownload', 'author', 'range', 'articleStatus', 'tutorCode', 'year', 'content', 'keyWord', 'originate', 'zTCode', 'summary', 'magaAssignCode', 'period', 'deptCode', 'dbName', 'arcitleType', 'versionCode', 'articleAssignCode', 'publishPYName', 'publishCode']

for i in range(10):
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
        'Smarts': '',
    }


    resp = requests.post(url, data=data)
    resp.encoding = 'utf-8'

    # print(resp.json())

    all = resp.json()['articleList']
    print(len(all))

    # 爬取每一栏的数据
    num = 0
    for element in all:
        data_list.append(element)
        print(len(element), f'爬取第{page}页{num}栏数据')
        num += 1

    page += 1
    resp.close()

# 写入csv文件中
with open('result.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, header)
    writer.writeheader()

    for row in data_list:
        writer.writerow(row)
f.close()


print(data_list)