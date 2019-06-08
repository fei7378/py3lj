import requests
from bs4 import BeautifulSoup
r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
print("打印所有a标签中的链接".center(70,"-"))
for link in soup.find_all("a"):
    print(link.get("href"))
print("BeautifulSoup库的find_all函数".center(70,"-"))
# 查询所有的a或b标签   返回列表类型
# print(soup.find_all(['a','b']))
# 返回所有标签
# print(soup.find_all(True))
