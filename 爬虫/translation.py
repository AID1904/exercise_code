import requests, random, time
from hashlib import md5


class Yd_Spider(object):
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Content-Length': '238',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'JSESSIONID=abc2fCmUbssL5cWnFrtXw; _ntes_nnid=b6d31eb207d41a6cd6feb4794683d10a,1564765173633; OUTFOX_SEARCH_USER_ID_NCOO=489358794.9066813; OUTFOX_SEARCH_USER_ID="1040105857@10.168.11.69"; UM_distinctid=16c8a1f7050178-0e5b0c3f7e881d-c343162-144000-16c8a1f70511bc; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; ___rl__test__cookies=1565701019374',
            'Host': 'fanyi.youdao.com',
            'Origin': 'http://fanyi.youdao.com',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }

    def get_salt_sign_ts(self, work):
        # 用老师给的js代码转puyhon代码
        ts = str(int(time.time() * 1000))
        salt = ts + str(random.randint(0, 9))
        string = ("fanyideskweb" + work + salt + "n%A-rKaT5fb[Gy?;N5@Tj")
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()

        return ts, salt, sign

    def parse_work(self, work):
        ts, salt, sign = self.get_salt_sign_ts(work)
        # 将参数对应的填好
        data = {
            'i': work,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'ts': ts,
            'bv': '53539dde41bde18f4a71bb075fcf2e66',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }

        res = requests.post(url=self.url, data=data, headers=self.headers).json()   # 输出为列表，方便后面的提取

        # 提取结果
        result = res['translateResult'][0][0]['tgt']
        # {'translateResult': [[{'tgt': '老虎', 'src': 'tiger'}]]....}
        print(result)   # 输出结果


if __name__ == '__main__':
    spider = Yd_Spider()
    spider.parse_work('tiger')