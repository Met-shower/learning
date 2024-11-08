import requests
import re

obj = re.compile(r'id="bfurl" href="(?P<url>.*?)"', re.S)  # 用来提取 m3u8 的url地址

url = "https://zrys1.icu/index.php/vod/play/id/61952/sid/1/nid/1/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
}
resp = requests.get(url, headers=headers)
# print(resp.text)

m3u8_url = obj.search(resp.text).group('url')
# print(m3u8_url)

# 下载 m3u8 文件
resp2 = requests.get(m3u8_url, headers=headers, verify=False)
# print(type(resp2.text))
with open("video.m3u8", mode="wb") as f:
    f.write(resp2.content)

resp2.close()
print("下载完毕")



n = 1
# 解析 m3u8 文件
with open("video.m3u8", mode="r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()  # 先去掉空格空白换行符
        if line.startswith("#"):  # 跳过以 # 号开头的行
            continue

        # 下载视频片段

        resp3 = requests.get(line)
        f = open(f"video/{n}.ts", mode="wb", encoding="utf-8")
        f.write(resp3.content)
        n += 1

        f.close()
        resp3.close()

