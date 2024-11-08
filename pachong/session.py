import requests

# session ：会话
session = requests.Session()

data = {"do": "submit"
        ,'action': 'login'
        ,"usecookie":1
        ,'username': '666over'
        ,'password': '123456'
        }

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"}

# 1、登录
url = "https://www.biqooge.com/login.php?do=submit&action=login&usecookie=1&jumpurl="

# url = 'https://www.biqooge.com/'
session.post(url, data=data, headers=headers)
# print(resp.json())


# 2、拿书架上的数据

a = session.get("https://www.biqooge.com/")
a.encoding = "utf-8"

print(a.json())
