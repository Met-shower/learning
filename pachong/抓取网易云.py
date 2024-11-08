# 1. 找到未加密的参数
# 2. 想办法把参数进行加密（参考网易的逻辑），params, encSecKey
# 3. 请求到网易，拿到评论信息

# 需要安装pycrypto : pip install pycrypto
# python 高版本安装：pip install pycryptodome
from Crypto.Cipher import AES
from base64 import b64encode
import requests
import json

# url = "https://music.163.com/#/song?id=2631278592"

# 请求 url
url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

# 请求方式 post
data = {
"csrf_token":""
,"cursor":"-1"
,"offset":"0"
,"orderType":"1"
,"pageNo":"1"
,"pageSize":"20"
,"rid": "R_SO_4_2631278592"
,"threadId": "R_SO_4_2631278592"
}

# 服务于window.asrsea
e = "01001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "zwFPR4XcwFPgWxIV"   # 手动固定的 -> 网页函数是随机的

def get_encSecKey():   # 由于 i 是固定的，则 encSecText 也是固定的
    return "6e9e97800224d23f4c66f368f79e04940ad57c7ecf663bc964c1702f263adabe091d501f84154b60c51fc4eeb438488356ca6b3f63c61467c04ed932cbc8ded7535de53cbd2d80e0579f710559849695122506a183c37306215bc758a364029d3e199491e48d27dcf833441e6350fafc96d466b430a150c6f6c2dfa7f510592f"

def get_params(data):  # 默认这里收到的是字符串
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second  # 返回的就是params

def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data

def enc_params(data, key): # 加密过程
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)  # 创造加密器
    bs = aes.encrypt(data.encode("utf-8"))  # 加密, 加密的内容的长度必须是16的倍数，
    return str(b64encode(bs), encoding="utf-8")  # 转换成字符串返回


resp = requests.post(url, data={
    "params":get_params(json.dumps(data)),
    "encSecKey":get_encSecKey(),
})

print(resp.text)


# 处理加密过程
"""
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,  # 随机数
            e = Math.floor(e),  # 取整
            c += b.charAt(e);  # 去字符串中的xxx位置 b
        return c
    }
    function b(a, b) {   # a 是要加密的内容，
        var c = CryptoJS.enc.Utf8.parse(b)   # b是密钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)   # e是数据
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,     # 偏移量
            mode: CryptoJS.mode.CBC  # 加密模式：cbc
        });
        return f.toString()
    }
    function c(a, b, c) {    # c里面不产生随机数
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {    # d：数据， e：01001， f：很长， 0CoJUm6Qyw8W8jud
        var h = {}  # 空对象
          , i = a(16);    # i 就是一个16位的随机值，把i设置成定值
        return h.encText = b(d, g),    # g 是密钥
        h.encText = b(h.encText, i),  # 返回的就是params      i 也是密钥
        h.encSecKey = c(i, e, f),   # 得到的就是encSecKey，e和f都是定死的，i固定得到的key一定是固定的
        h
    }
"""


