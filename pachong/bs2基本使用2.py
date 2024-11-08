import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umei.cc/bizhitupian/fengjingbizhi/"
resp = requests.get(url)
resp.encoding = 'utf-8'
# print(resp.text)

# 源代码交给 bs4
main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div", {"class": "item_list infinite_scroll"}).find_all("a", {"class": "img_album_btn"})
# print(alist)

for a in alist:
    # print(a.get('href')) # 直接通过 get 就能拿到属性的值
    href = a.get("href") # 通过get拿到属性值
    href = url + href.split("/")[-1]
    # 拿到子页面源代码
    child_page_resp = requests.get(href)
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text
    # 从子页面拿到图片的下载路径
    # print(child_page_text)
    # break
    child_page = BeautifulSoup(child_page_text, "html.parser")
    div = child_page.find("div", {"class": "big-pic"})
    img = div.find("img")
    # 在属性中找下载路径
    src = img.get("src")
    # 下载图片
    img_resp = requests.get(src)
    img_name = src.split("/")[-1] # 拿到url中最后一个/以后的内容
    with open("imgs/" + img_name, mode="wb") as f: # 放到imgs文件夹中
        f.write(img_resp.content) # img_resp.content拿到字节，图片内容写入文件

    print("over!!!", img_name)
    time.sleep(1)




