import requests
from bs4 import BeautifulSoup
# bs4库默认utf-8编码
r = requests.get("https://python123.io/ws/demo.html")
# r = requests.get("https://cn.bing.com/")
r.encoding = r.apparent_encoding
# print(r.text)
demo = r.text
# 使用解析器解析html
soup = BeautifulSoup(demo,"html.parser")
# 为标签添加换行符
# print(soup.prettify())

# print("分割线".center(70,"-"))
# print(soup.a.parent.parent.name)
tag = soup.a
# print(tag.attrs)
# print(tag.attrs['href'])
# print(type(tag))
# print(soup.a.string)

# print(soup.body.contents)
# print(len(soup.body.contents))
# print(soup.body.contents[1])
# for child in soup.body.contents:
#     print(">>>{}".format(child))
print(soup.a)
print("平行遍历".center(70,"-"))
# 标签的平行节点可能是字符串
print(type(soup.a.next_sibling))
# print(soup.html.parent)

print(soup.a.previous_sibling)