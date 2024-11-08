import requests
from bs4 import BeautifulSoup
import re
import csv

def Get_Url(headers):
    href = []
    for i in range(0, 251, 25):
        # 访问每个主页面
        url = f"https://movie.douban.com/top250?start={i}&filter="

        resp = requests.get(url, headers=headers)

        # 提取每个子页面的 url
        main_page = BeautifulSoup(resp.text, "lxml")
        urls = main_page.find('ol', class_='grid_view').find_all("a", class_="")
        # print(f"{num}")
        for url in urls:
            if '<a class="" ' in str(url):
                href.append(url['href'])
        resp.close()
    return href



# 获取单个页面的的信息
def Get_Mess(url_son):
    url_son = url_son

    url_son_resp = requests.get(url_son, headers=headers)
    # print(url_son_resp.text)

    son_page = BeautifulSoup(url_son_resp.text, "html.parser")

    # 获取网页信息
    # 排名 名字
    rank = son_page.find('span', {'class': 'top250-no'}).text
    name = son_page.find('span', {'property': 'v:itemreviewed'}).text
    # print(rank, name)

    datas = son_page.find('div', {'id': 'info'})
    # print(datas)

    # 得到data的key 电影关键字
    data_key = ['导演', '编剧', '主演', '类型', '制片国家/地区', '语言', '上映日期', '片长', 'IMDb']

    # data_keys = datas.find_all('span', {'class': 'pl'})
    # data_key = []
    # for key in data_keys:
    #     data_key.append(key.text)
    # print(data_key)

    # 得到data的value
    data_values = datas.find_all("span", {"class": "attrs"})
    # print(len(data_values))
    # 导演
    leader = data_values[0].text
    # print(leader)
    # 编剧
    screenwriter = data_values[1].text
    # 主演
    video_actor = data_values[2].text
    # 剧情类型
    video_type = datas.find_all('span', {'property': 'v:genre'})
    video_types = ''
    for type in range(len(video_type)):
        video_types = video_types + ',' + video_type[type].text
    # print(video_types)
    # 地区国家 语言 又名 IMDb
    obj = re.compile(
        r'制片国家/地区:</span> (?P<location>.*?)<br/>.*?语言:</span> (?P<language>.*?)<br/>.*?IMDb:</span> (?P<IMDb>.*?)<br>',
        re.S)
    result = obj.finditer(url_son_resp.text)
    for match in result:
        location = match.group('location')
        language = match.group('language')
        # rename = match.group('rename')
        IMDb = match.group('IMDb')
        # print(location, language, rename, IMDb)
    # 上映日期
    time = datas.find_all('span', {'property': 'v:initialReleaseDate'})
    times = ''
    for tm in range(len(time)):
        times = times + ',' + time[tm].text
    # print(times)
    # 时长
    runtime = datas.find_all('span', {'property': 'v:runtime'})[0].text
    # print(runtime)

    mess = [leader, screenwriter, video_actor, video_types, location, language, times, runtime, IMDb]
    # print(mess)

    # 合成键值对信息表
    details = {}

    # 剧情梗概
    summary = son_page.find_all('span', {'property': 'v:summary'})[0].text.split()
    # print(summary)

    # 豆瓣评分
    rating_num = son_page.find_all('strong', {'class': 'rating_num'})[0].text

    # 评价人数
    votes = son_page.find_all('span', {'property': 'v:votes'})[0].text

    # 评价权重
    rating_weight = son_page.find('div', {'class': 'ratings-on-weight'})

    weights = {}
    for num in range(5):
        exp = rating_weight.find_all('div', {'class': 'item'})[num].text.split()
        weights[exp[0]] = exp[1]
    # print(weights)

    details['rank'] = rank
    details['name'] = name
    details['summary'] = summary
    details['rating_num'] = rating_num
    details['votes'] = votes
    details['weights'] = weights

    n = 0
    for key in data_key:
        details[key] = mess[n]
        n += 1

    url_son_resp.close()
    return details


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
}




if __name__ == '__main__':
    # 得到子页面的url
    get_url = Get_Url(headers)


    # 将所有内容写入
    for i in range(len(get_url)):
        if i == 234:
            continue

        get_mess = Get_Mess(get_url[i])
        # print(get_mess)

        with open(f'movies/{get_mess['rank']}.csv', mode='w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(get_mess.keys())
            writer.writerow(get_mess.values())

        print(f'提取“{get_mess["name"]}”完毕')