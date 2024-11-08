import requests

url = "https://zrys1.icu/index.php/vod/play/id/61952/sid/1/nid/1/"

resp= requests.get(url)

# print(resp.text)

url_url = "https://cdn.zyc888.top/?url=https://v.cdnlz22.com/20241008/6079_93857a3c/index.m3u8"

resp2 = requests.get(url_url)

print(resp2.text)