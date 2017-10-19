import requests


header = {
    "Host": "www.kuaidaili.com",
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

#免费代理页面
FREE_PROXY_TARGET_URL = ("http://www.kuaidaili.com/free/inha/1")


html = requests.get(url=FREE_PROXY_TARGET_URL, headers=header, timeout=30).content
print(html)
