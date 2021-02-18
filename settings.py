# 线程数
SEMNUM = 4

# 代理
PROXIES = {
    "A(10次/秒)": {"proxyUser": "HL8DHM82N5WP3E9D", "proxyPass": "4FABA9DCDFE545A9"},
    "B(5次/秒)": {"proxyUser": "H8998HH56D840AJD", "proxyPass": "9058C022C5237535"},
}

# 钉钉消息

DINGDING = {
    "A": {"secret": "SEC55a76e7d3e923076fd952ce240f8a73134b6f221f58942d0a59a9da78cb79e35",
          "webHook": "https://oapi.dingtalk.com/robot/send?access_token=c84273a577d00af3dd82f0ba2f6bc44ef02d3dbf331b7f170bbab5e467c8fea7"},
    "B": {"secret": "SECc4ef18a624c885d7f31cc785e3f42e6f74777d3aaa18dda693ec784b6e6ab2b5",
          "webHook": "https://oapi.dingtalk.com/robot/send?access_token=0c18a87c2ae3b9c640929c26d97b1d4667096142564e727a41be92315d7e88bc"},
}

# 发现有货后, 暂停时间设置
SLEEPTIME = 5 * 60

# 购买藏账号设置
HERMES_INFO = {
    "A": {"user": "libo985989982@hotmail.com",
          "passwd": "libo19930728"},
    "B": {"user": "libo985989982@hotmail.com",
          "passwd": "libo19930728"},
    "C": {"user": "libo985989982@hotmail.com",
          "passwd": "libo19930728"},
}

# 重新登陆时间设置
RESTARTSLEEPTIME = 4 * 60

# 是否加载浏览器图片
LOAD_IMAGES = True

