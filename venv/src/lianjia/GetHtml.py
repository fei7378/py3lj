import requests

def getHTMLTest(url):
    try:
        # 链家对爬虫有限制
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, timeout=30, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
