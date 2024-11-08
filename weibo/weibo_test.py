import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'Cookie': 'SINAGLOBAL=9277284148470.64.1729681539203; SCF=AtxSdASbuNk4W6NqKIjU-m3zxpFxVcQd6BTJuWI5_9X_BZV09Tt74-6aM9dm302cWbw3PhhOOFeT-f-IhGFGTvc.; SUB=_2A25KHKitDeRhGeFM7FIV-SzMwzSIHXVpU6RlrDV8PUNbmtB-LWTckW9NQK8mznOH5HL4oRWLG5grpA-fiKExn5hs; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5gThUMvnI0kK8s7aBj0LuM5NHD95QNeoM7Sh.EehnRWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0zNehB4eo5R15tt; WBPSESS=vRFYWl_IsZi6CheWZY8Fct3oGVvRqMew7sPhTJ9wlym9ObLq1G0M5clPpzVKE5_9pf-iGeGDVvgtC_CmhxGSPFTQqCn8ZmytgYNCGV6kG4-dFOILYZCfz4QT9F2cPN76y_Nsclhq3LOm4o4g7imDmA==; XSRF-TOKEN=grjjQYoFWZCMvzXnW2EIc_dx; _s_tentry=weibo.com; Apache=7314229001395.207.1729917844874; ULV=1729917844890:5:5:5:7314229001395.207.1729917844874:1729854601186',

}


url1 = 'https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=5089641864102186&is_show_bulletin=2&is_mix=0&count=10&uid=2713131601&fetch_level=0&locale=zh-CN'

resp = requests.get(url1)
resp.encoding = 'gbk'
print(resp.json())