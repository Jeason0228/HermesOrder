# coding: utf-8
import requests

from datetime import datetime






def my_proxies():
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


def sku_check_use_cookie(sku_url):
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
    headers["cookie"] = "LomTxpRfKRUn0-lavkFZNdxOcyldGMxrxn-0qWbr~M_itQ5Cjn4Z9sjRt2334OyDfHH8a9eR7pMhjtHkRX8T2zj577F.2baMHRyIp3I30Y"
    resp2 = requests.get(sku_url, headers=headers, proxies=my_proxies(), timeout=30).text
    # if resp2.startswith('{"url":"'):
    #     self.redis.rem_cookie(headers["cookie"])
    return resp2

if __name__ == '__main__':
    while True:
        checkurl = "https://bck.hermes.com/product?locale=cn_zh&productsku=H003748S%252002"
        try:
            res = sku_check_use_cookie(checkurl)
            print(datetime.now())
            print(res)
            print('-'*100)
        except:
            pass
