# 主页列表
import requests
# from bs4 import BeautifulSoup
import bs4
import GetHtml
import re
import time
from SQLCatalogOEM import OrmTest
# 计数变量
numberall = 0
# 获取html的数据

# 使用beautifulsoup库解析html
def parserList(html):
    global numberall

    soup = bs4.BeautifulSoup(html, "html.parser")
    # print(type(soup))
    all_tag = soup.find(name='div',attrs={'class':'key-list imglazyload'})
    # 获取的信息遍历房屋

    allhouser = []
    for tag in all_tag.children:
        if isinstance(tag, bs4.element.Tag):
            for tag1 in tag.children:
                if isinstance(tag1, bs4.element.Tag):
                    for tag2 in tag1.children:
                        if isinstance(tag2, bs4.element.Tag):
                            for tag3 in tag2.children:
                                if isinstance(tag3, bs4.element.Tag):
                                    print(type(tag3))

                                else:
                                    if len(tag3) > 1:
                                        print(tag3)

                        else:
                            if len(tag2) > 1:
                                print(tag2)

                else:
                    if len(tag1) > 1:
                        print(tag1)

        else:
            if len(tag) > 1:
                print(tag)


    return allhouser



def main():
    startTime = time.clock()
    for i in range(1,100):
        timeStart = time.perf_counter()
        print(timeStart)
        url = "https://cd.fang.anjuke.com/loupan/all/p{}/".format(i)
        # 获取url的html
        html = GetHtml.getHTMLTest(url)


        # 将html数据放入uinfo
        allhouser = parserList(html)
        # print(allhouser)
        for houser in allhouser:

            print(houser)
            # # 集中写入数据库
            # obj = OrmTest()
            # rest = obj.add_one(houser)
            # print(rest.id)
        print(time.perf_counter() - timeStart)



    endTime = time.clock()-startTime
    print("爬取完毕,爬取时长{}".format(endTime))

def maintest():
    url = "https://cd.fang.anjuke.com/loupan/all/p1/"
    # 获取url的html
    html = GetHtml.getHTMLTest(url)
    parserList(html)


# main()
if __name__ == '__main__':
   maintest()