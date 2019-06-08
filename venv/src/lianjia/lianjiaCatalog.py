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
    all_tag = soup.find(name='ul',attrs={'class':'resblock-list-wrapper'})
    # 获取的信息遍历房屋

    allhouser = []
    for tag in all_tag.children:
        if isinstance(tag, bs4.element.Tag):
            numberall=numberall+1
            house = []
            house.append(numberall)
            # print("{}  >>> {}".format(numberall,tag.a.attrs['title']),end="  ")
            house.append(tag.a.attrs['title'])

            # 获取下一页的跳转链接
            dataOther = tag.a.get("data-other-action")


            patternpro = re.compile(r'\&project_name=[a-zA-Z0-9]+\&')
            # print(dataOther[10:60])
            project_name_all = re.findall(patternpro, dataOther[10:60])
            # print(project_name_all)
            project_name = project_name_all[0].split("=")
            pn = project_name[1][:-1]
            # print(project_name[1][:-1])
            # 获取房屋详细信息
            # print(house)
            house.append(pn)

            # 打印房屋全部信息
            # print(house)
            allhouser.append(house)

    return allhouser



def main():
    startTime = time.clock()
    for i in range(1,100):
        timeStart = time.perf_counter()
        print(timeStart)
        url = "https://cd.fang.lianjia.com/loupan/pg{}/".format(i)
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

# main()
if __name__ == '__main__':
   main()