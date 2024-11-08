import requests

url = 'https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}'

resp = requests.get(url).json()

# print(resp.text)

with open('novel.csv', mode='w', encoding='utf-8') as f:
    # f.write(resp.text)
    f.write(resp['data']['novel']['content'])
    # content = resp["data"]['novel']['content']
    # f.write(content)