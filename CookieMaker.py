# coding:utf-8
import requests
import time
import random
from urllib import parse
from faker import Factory
import redis
import random
import warnings

warnings.filterwarnings("ignore")

class RedisConn:

    def __init__(self):
        REDIS_URL = "redis://admin:123456@127.0.0.1:6379/0"
        self.pool = redis.ConnectionPool.from_url(REDIS_URL)
        # 连接数据库
        self.db = redis.StrictRedis(connection_pool=self.pool)

    def save_cookie(self, cookie):
        self.db.rpush("HERMES_COOKIES", cookie)

    def get_cookie(self):
        res = self.db.lrange("HERMES_COOKIES", 0, -1)
        return [i.decode("utf-8") for i in res]

    def rem_cookie(self, cookie):
        self.db.lrem("HERMES_COOKIES", 1, cookie.encode())


class CookieGenerate:

    def __init__(self):
        self.proxies = self.my_proxies()
        self.redis = RedisConn()

    def my_proxies(self):
        # 代理服务器
        proxyHost = "u6372.5.tp.16yun.cn"
        proxyPort = 6445

        # 代理隧道验证信息
        proxyUser = "16UBSUQA"
        proxyPass = "789143"

        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }

        proxies = {
            "http": proxyMeta,
            "https": proxyMeta
        }
        return proxies

    def home_page_visit(self):
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "origin": "https://www.hermes.cn",
            "referer": "https://www.hermes.cn/",
            "sec-ch-ua": "\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
        }
        resp_0 = requests.get(
            "https://bck.hermes.com/products?locale=pl_en&category=WOMENSILKSCARVESETC&sort=relevance&pagesize=36",
            proxies=self.proxies, headers=headers, verify=False, timeout=30)

        cookies = resp_0.cookies.get("datadome")
        return cookies

    def cookie_generate(self, datadome, product_url):
        _1 = int(time.time() * 1000)
        _2 = _1 + random.randint(50, 80)
        _3 = _2 + random.randint(50, 80)
        _4 = _3 + random.randint(50, 80)
        _5 = _4 + random.randint(50, 80)
        _6 = _5 + random.randint(50, 80)
        _7 = _6 + random.randint(50, 80)
        _8 = _7 + random.randint(50, 80)
        _9 = _8 + random.randint(50, 80)
        _10 = _9 + random.randint(50, 80)
        ua = Factory.create()
        post_data = {
            "jsData": {
                "ttst": 27.905001770704985,
                "ifov": "false",
                "wdifts": "false",
                "wdifrm": "false",
                "wdif": "false",
                "br_h": 943,
                "br_w": 959,
                "br_oh": 824,
                "br_ow": 1536,
                "nddc": 1,
                "rs_h": 864,
                "rs_w": 1536,
                "rs_cd": 24,
                "phe": "false",
                "nm": "false",
                "jsf": "false",
                "ua": ua,
                "lg": "zh-CN",
                "pr": 1,
                "hc": 8,
                "ars_h": 824,
                "ars_w": 1536,
                "tz": -480,
                "str_ss": "true",
                "str_ls": "true",
                "str_idb": "true",
                "str_odb": "true",
                "plgod": "false",
                "plg": 3,
                "plgne": "true",
                "plgre": "true",
                "plgof": "false",
                "plggt": "false",
                "pltod": "false",
                "lb": "false",
                "eva": 33,
                "lo": "false",
                "ts_mtp": 0,
                "ts_tec": "false",
                "ts_tsa": "false",
                "vnd": "Google Inc.",
                "bid": "NA",
                "mmt": "application/pdf,application/x-google-chrome-pdf,application/x-nacl,application/x-pnacl",
                "plu": "Chrome PDF Plugin,Chrome PDF Viewer,Native Client",
                "hdn": "false",
                "awe": "false",
                "geb": "false",
                "dat": "false",
                "med": "defined",
                "aco": "probably",
                "acots": "false",
                "acmp": "probably",
                "acmpts": "true",
                "acw": "probably",
                "acwts": "false",
                "acma": "maybe",
                "acmats": "false",
                "acaa": "probably",
                "acaats": "true",
                "ac3": "",
                "ac3ts": "false",
                "acf": "probably",
                "acfts": "false",
                "acmp4": "maybe",
                "acmp4ts": "false",
                "acmp3": "probably",
                "acmp3ts": "false",
                "acwm": "maybe",
                "acwmts": "false",
                "ocpt": "false",
                "vco": "probably",
                "vcots": "false",
                "vch": "probably",
                "vchts": "true",
                "vcw": "probably",
                "vcwts": "true",
                "vc3": "maybe",
                "vc3ts": "false",
                "vcmp": "",
                "vcmpts": "false",
                "vcq": "",
                "vcqts": "false",
                "vc1": "probably",
                "vc1ts": "false",
                "dvm": 8,
                "sqt": "false",
                "so": "landscape-primary",
                "wbd": "false",
                "wbdm": "true",
                "wdw": "true",
                "cokys": "bG9hZFRpbWVzY3NpYXBwcnVudGltZQ==L=",
                "ecpc": "false",
                "lgs": "true",
                "lgsod": "false",
                "bcda": "false",
                "idn": "true",
                "capi": "false",
                "svde": "false",
                "vpbq": "true",
                "xr": "true",
                "bgav": "true",
                "rri": "true",
                "idfr": "true",
                "ancs": "true",
                "inlc": "true",
                "cgca": "true",
                "inlf": "true",
                "tecd": "true",
                "sbct": "true",
                "aflt": "true",
                "rgp": "true",
                "bint": "true",
                "spwn": "false",
                "emt": "false",
                "bfr": "false",
                "dbov": "false",
                "glvd": "Google Inc.",
                "glrd": "ANGLE (Intel(R) UHD Graphics Direct3D11 vs_5_0 ps_5_0)",
                "tagpu": 14.045000076293945,
                "prm": "true",
                "tzp": "Etc/GMT-8",
                "cvs": "true",
                "usb": "defined",
                "mp_cx": 956,
                "mp_cy": 198,
                "mp_tr": "true",
                "mp_mx": 6,
                "mp_my": -5,
                "mp_sx": 764,
                "mp_sy": 229,
                "dcok": ".hermes.cn",
                "ewsi": "false",
                "tbce": 63
            },
            "events": [
                {
                    "source": {
                        "x": 958,
                        "y": 252
                    },
                    "message": "mouse move",
                    "date": _1,
                    "id": 0
                },
                {
                    "source": {
                        "x": 577,
                        "y": 328
                    },
                    "message": "mouse move",
                    "date": _2,
                    "id": 0
                },
                {
                    "source": {
                        "x": 453,
                        "y": 349
                    },
                    "message": "mouse move",
                    "date": _3,
                    "id": 0
                },
                {
                    "source": {
                        "x": 682,
                        "y": 364
                    },
                    "message": "mouse move",
                    "date": _4,
                    "id": 0
                },
                {
                    "source": {
                        "x": 856,
                        "y": 321
                    },
                    "message": "mouse move",
                    "date": _5,
                    "id": 0
                },
                {
                    "source": {
                        "x": 906,
                        "y": 247
                    },
                    "message": "mouse move",
                    "date": _6,
                    "id": 0
                },
                {
                    "source": {
                        "x": 950,
                        "y": 119
                    },
                    "message": "mouse move",
                    "date": _7,
                    "id": 0
                },
                {
                    "source": {
                        "x": 816,
                        "y": 232
                    },
                    "message": "mouse move",
                    "date": _8,
                    "id": 0
                },
                {
                    "source": {
                        "x": 805,
                        "y": 245
                    },
                    "message": "mouse move",
                    "date": _9,
                    "id": 0
                },
                {
                    "source": {
                        "x": 805,
                        "y": 246
                    },
                    "message": "mouse click",
                    "date": _10,
                    "id": 1
                }
            ],
            "eventCounters": {
                "mouse move": 9,
                "mouse click": 1,
                "scroll": 0,
                "touch start": 0,
                "touch end": 0,
                "touch move": 0,
                "key press": 0,
                "key down": 0,
                "key up": 0
            },
            "jsType": "le",
            "cid": "",
            "ddk": "2211F522B61E269B869FA6EAFFB5E1",
            "Referer": "",
            "request": "",
            "responsePage": "origin",
            "ddv": "4.1.45"
        }
        referer = parse.quote(product_url).replace("/", "%2F")
        requestStr = parse.quote(parse.urlparse(product_url).path).replace("/", "%2F")
        post_data["Referer"] = referer
        post_data["request"] = requestStr
        post_data["cid"] = datadome
        js_url = "https://api-js.datadome.co/js/"
        headers_js = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-type": "application/x-www-form-urlencoded",
            "Host": "api-js.datadome.co",
            "Origin": "https://www.hermes.cn",
            "Referer": "https://www.hermes.cn/",
            "sec-ch-ua": "\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
        }

        resp = requests.post(js_url, headers=headers_js, data=post_data, proxies=self.proxies, timeout=30)
        cookie = resp.json().get("cookie").split(";")[0].replace("datadome=", "")
        return cookie

    def sku_check(self, cookie, sku_url):
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "origin": "https://www.hermes.cn",
            "referer": "https://www.hermes.cn/",
            "sec-ch-ua": "\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
        }
        headers["cookie"] = cookie
        resp2 = requests.get(sku_url, headers=headers, proxies=self.proxies, timeout=30)
        return resp2.text

    def sku_check_use_cookie(self, sku_url):
        cookie_list = self.redis.get_cookie()
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "origin": "https://www.hermes.cn",
            "referer": "https://www.hermes.cn/",
            "sec-ch-ua": "\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
        }
        headers["cookie"] = random.choice(cookie_list)
        resp2 = requests.get(sku_url, headers=headers, proxies=self.proxies, timeout=30).text
        # if resp2.startswith('{"url":"'):
        #     self.redis.rem_cookie(headers["cookie"])
        return resp2

    def start(self, product_url, sku_url):
        home_cookie = self.home_page_visit()
        # home_cookie = "5h8SWcV_su7Bnv3nHmIY_rRSonO1X.QAegm7BV5s_jAA.eLTK6KNxwVEIvWzlxFyvk3jhniaNw0rfl_uFOL5sq9JIF~LY6.beeb3eGqlAn"
        sku_cookie = self.cookie_generate(home_cookie, product_url)
        sku_result = self.sku_check(sku_cookie, sku_url)
        print(home_cookie)
        if not sku_result.startswith('{"url":"'):
            self.redis.save_cookie(sku_cookie)
            print("【cookie存储成功：{}】".format(sku_cookie))
        else:
            print("【失效cookie：{}】".format(sku_cookie))
        return sku_result

if __name__ == '__main__':
    app = CookieGenerate()
    url = "https://www.hermes.com/pl/en/product/voitures-exquises-twilly-H063429Sv06"
    sku_url = "https://bck.hermes.cn/product?locale=pl_en&productsku=H063429S%252006"
    # sku_url = "https://bck.hermes.cn/product?locale=cn_zh&productsku=H1199448%252001"
    index = 1
    while True:
        print(f"【第{index}次测试结果】")
        try:
            result = app.start(url, sku_url)
            # result = app.sku_check_use_cookie(sku_url)
            print(result)
            print('-' * 100)
            index += 1
        except:
            pass
