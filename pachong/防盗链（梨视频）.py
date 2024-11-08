import requests

# 爬取视频的网址
url = "https://www.pearvideo.com/video_1796529"
contID = url.split("_")[1]

videoStatueUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.8174682461343399"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
           # 溯源（防盗链）
           ,"Referer": url}

resp = requests.get(videoStatueUrl, headers=headers)
dic = resp.json()
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']

# https://video.pearvideo.com/mp4/short/20240928/cont-1796529-16037705-hd.mp4    真实地址
# https://video.pearvideo.com/mp4/short/20240928/1728268853073-16037705-hd.mp4   srcUrl得到的
# 拼接真实的视频链接
srcUrl = srcUrl.replace(systemTime, f"cont-{contID}")

# 下载视频
with open("a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl, headers=headers).content) # .content 将文件的内容写入mp4