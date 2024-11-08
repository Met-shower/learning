import requests


url  = 'https://www.pkulaw.com'

session = requests.Session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'Cookie': "1b94db2c-d875-e711-934a-5254ec69a56d_case=false; xCloseNew=20; div_display=none; 1b94db2c-d875-e711-934a-5254ec69a56d_law=false; 067ef732-118e-ef11-bbb3-cedfe031168f_law=false; isTip_topSub=true; 067ef732-118e-ef11-bbb3-cedfe031168f_case=false; Hm_lvt_8266968662c086f34b2a3e2ae9014bf8=1729333896,1729340964; HMACCOUNT=CAD33A6FBF6531C8; cookieUUID=cookieUUID_1729340964488; referer=; WEIXIN_APP_LOGIN_KEY=20e0a312-cc5d-46d0-b819-a91c61fe7ab9; kc_locale=zh-CN; __RequestVerificationToken=nOEO0tBctIea_At0F6gwTbsTGAdBI7kXEBHl5GooeK75XDOWw3c8SBpfnHzaQBvVNgkRv4V2258p9PbHpM9EYgdYbgs1; pkulaw_v6_sessionid=kby0b0sd3zuzyou2sebfj4wq; Hm_up_8266968662c086f34b2a3e2ae9014bf8=%7B%22ysx_yhqx_20220602%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22ysx_hy_20220527%22%3A%7B%22value%22%3A%2206%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22067ef732-118e-ef11-bbb3-cedfe031168f%22%2C%22scope%22%3A1%7D%2C%22ysx_yhjs_20220602%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%7D; Hm_lpvt_8266968662c086f34b2a3e2ae9014bf8=1729344726",
    # 'library': 'pfnl',
    # # 'Aggs': {"CategoryIntegration":"","CaseGrade":"","CaseClass":"","SubjectClassSpecialType":"","CourtGrade":"","LastInstanceCourt":"","TrialStep":"","DocumentAttr":"","LastInstanceDate":"","TrialStepCount":"","NoPublicReason":"","WordNum":"","AnocsInfoList":""},
    # 'QueryBase64Request':'',
    # 'keyword':'',
    # 'advDic':'',
    # 'SearchInResult':'',
    # 'ClassFlag': 'pfnl',
    # 'ExtCondition':'',
    # 'KeywordType': 'Title',
    # 'MatchType': 'Exact'
}

resp = session.post(url, headers=headers)


print(resp.text)

resp.close()