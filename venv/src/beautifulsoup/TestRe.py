# 引入正则表达式库
import re
import requests
from bs4 import BeautifulSoup

r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
# 使用正则表达式匹配标签
for tag in soup.find_all(re.compile("b")):
    print(tag.name)
print("在p标签中检索带有course的标签".center(70,"-"))
# soup.find_all("p") 可以简写为soup("p")

print(soup.find_all('p','course'))
print("查找id为link的值".center(70,"-"))
print(soup.find_all(id='link'))
print("使用正则表达式来匹配内容".center(70,"-"))
print(soup.find_all(id=re.compile('ink')))
print("检索文本".center(70,"-"))
print(soup.find_all(string=re.compile("Python")))
print(soup(string="Basic Python"))