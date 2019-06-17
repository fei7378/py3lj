import requests
# from bs4 import BeautifulSoup
import bs4
import GetHtml
import re
import time
from SQLAlchemyOEM import OrmTest
from SQLStatusListOEM import StatusList
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

            # 获取房屋头部标签
            htoptag = []
            resblockName = tag.find(name='div', attrs={'class': 'resblock-name'})
            for ht in resblockName('span'):
                htoptag.append(ht.string.strip())

            house.append("/".join(htoptag))
            # print(tag.prettify(),end="\n")
            # 获取房屋地址  180632491871760384
            area = []
            areaTag = tag.find(name='div',attrs={'class':'resblock-location'})
            # print(areaTag('span'))
            for a in areaTag('span'):
                area.append(a.string)
            # print(areaTag.find('a').string)
            area.append(areaTag.find('a').string)
            # 打印房屋地址
            # print(area,end="  ")
            house.append("/".join(area))
            # 获取房屋价格
            # print(tag.find(name='span',attrs={'class':'number'}).string,end=" ")
            house.append(tag.find(name='span',attrs={'class':'number'}).string.strip())
            # 获取房屋价格单位
            # print(tag.find(name='span',attrs={'class':'desc'}).string,end="\n")
            try:

                house.append(tag.find(name='span',attrs={'class':'desc'}).string.strip())
            except:
                house.append("")
            # 获取房屋底部标签
            htag = []
            resblockTag = tag.find(name='div',attrs={'class':'resblock-tag'})
            for ht in resblockTag.children:
                if isinstance(ht, bs4.element.Tag):
                    htag.append(ht.string.strip())

            house.append("/".join(htag))
            # print()
            # print("房屋".center(80, "-"))

            # 打印房屋首页信息
            # print(house)

            # 获取下一页的跳转链接
            dataOther = tag.a.get("data-other-action")

            patternid = re.compile(r'\"fb_expo_id\":\"\d+\"')
            fbid = re.findall(patternid, dataOther)
            # pattern = re.compile(r'\d+')
            patternid = re.compile(r'\d+')
            houseid = re.findall(patternid, fbid[0])
            # 房屋的id
            # print(houseid[0])
            # print()

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
            # 打印房屋列表解析数据
            print(house)
            house.append(getOtherText(pn,houseid[0]))
            # 打印房屋全部信息
            # print(house)
            allhouser.append(house)

    return allhouser
# 判断数据库是否存在此数据
def parserUpdateList(html):
    global numberall

    soup = bs4.BeautifulSoup(html, "html.parser")
    # print(type(soup))
    all_tag = soup.find(name='ul', attrs={'class': 'resblock-list-wrapper'})
    ormTest = OrmTest()
    # 获取的信息遍历房屋
    allhouser = []
    for tag in all_tag.children:
        if isinstance(tag, bs4.element.Tag):



            numberall = numberall + 1
            house = []
            house.append(numberall)

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
            print(pn)

            # 判断数据库是否存在   存在就跳过
            if len(ormTest.selectBySonUrl(pn)):
                continue




            patternid = re.compile(r'\"fb_expo_id\":\"\d+\"')
            fbid = re.findall(patternid, dataOther)
            # pattern = re.compile(r'\d+')
            patternid = re.compile(r'\d+')
            houseid = re.findall(patternid, fbid[0])


            # print("{}  >>> {}".format(numberall,tag.a.attrs['title']),end="  ")
            house.append(tag.a.attrs['title'])

            # 获取房屋头部标签
            htoptag = []
            resblockName = tag.find(name='div', attrs={'class': 'resblock-name'})
            for ht in resblockName('span'):
                htoptag.append(ht.string.strip())

            house.append("/".join(htoptag))
            # print(tag.prettify(),end="\n")
            # 获取房屋地址  180632491871760384
            area = []
            areaTag = tag.find(name='div', attrs={'class': 'resblock-location'})
            # print(areaTag('span'))
            for a in areaTag('span'):
                area.append(a.string)
            # print(areaTag.find('a').string)
            area.append(areaTag.find('a').string)
            # 打印房屋地址
            # print(area,end="  ")
            house.append("/".join(area))
            # 获取房屋价格
            # print(tag.find(name='span',attrs={'class':'number'}).string,end=" ")
            house.append(tag.find(name='span', attrs={'class': 'number'}).string.strip())
            # 获取房屋价格单位
            # print(tag.find(name='span',attrs={'class':'desc'}).string,end="\n")
            try:

                house.append(tag.find(name='span', attrs={'class': 'desc'}).string.strip())
            except:
                house.append("")
            # 获取房屋底部标签
            htag = []
            resblockTag = tag.find(name='div', attrs={'class': 'resblock-tag'})
            for ht in resblockTag.children:
                if isinstance(ht, bs4.element.Tag):
                    htag.append(ht.string.strip())

            house.append("/".join(htag))
            # print()
            # print("房屋".center(80, "-"))

            # 打印房屋首页信息
            # print(house)
            house.append(pn)


            # 房屋的id
            # print(houseid[0])
            # print()


            # 打印房屋列表解析数据
            print(house)
            house.append(getOtherText(pn, houseid[0]))
            # 打印房屋全部信息
            # print(house)
            allhouser.append(house)

    return allhouser

    # print(tag.attrs["href"])
    # print(all_tag)
    # for tag in bs4.BeautifulSoup(all_tag,"html.parser").childred:
    #     print(tag)
    # print(type(tag.string))
    # 循环tbody的子孙节点
    # for tr in soup.find('tbody').children:
    #     if isinstance(tr,bs4.element.Tag):
    #         # 获取td标签内容
    #         tds = tr('td')
    #         # print(tds)
    #         ulist.append([tds[0].string,tds[1].string,tds[2].string])

# 获取详细数据
def getOtherText(projectName,id):
    global numberall
    startTime = time.perf_counter()
    # print("房屋id>>>>{}".format(id))
    # 获取房屋的详细数据
    otherHtml = GetHtml.getHTMLTest("https://cd.fang.lianjia.com/loupan/p_{}/?fb_expo_id=".format(projectName,id))
    # 将房屋的详细数据进行解析
    resultSoup = bs4.BeautifulSoup(otherHtml, "html.parser")
    # 获取详细数据的div标签
    allResultTag = resultSoup.find(name='div', attrs={'class': 'box-loupan'})
    # print("房屋详情".center(40, "-"))
    otherlist = []
    for tagitem in allResultTag:
        if isinstance(tagitem, bs4.element.Tag):
            for tag in tagitem:
                # 内容开始
                if isinstance(tag,bs4.element.Tag):
                    # print("{} >>> {}".format(tag.string, type(tag)))
                    for t1 in tag:
                        if isinstance(t1, bs4.element.Tag):
                            for t2 in t1:
                                if isinstance(t2, bs4.element.Tag):
                                   for t3 in t2:
                                       if isinstance(t3, bs4.element.Tag):
                                           for t4 in t3:
                                               # print(type(t4))
                                               # print("{}----{}".format(len(t4.string), t4.replace(' ', '').replace('\n', '').replace(';', '')))
                                               # print(t4.string.strip(),end=" ")
                                               otherlist.append(t4.replace(' ', '').replace('\n', '').replace(';', ''))

                                       elif isinstance(t3, bs4.element.NavigableString):
                                           if len(t3.string) > 1:
                                               # 有效数据
                                               # print("{}---{}".format(len(t3.string), t3.string.replace(' ', '').replace('\n', '').replace(';', '')))
                                               # print(t3.string.strip(),end=" ")
                                               otherlist.append(t3.string.replace(' ', '').replace('\n', '').replace(';', ''))




                        elif isinstance(t1, bs4.element.NavigableString):
                            if len(t1.string) > 1:
                                # 有效数据
                                # print("{}-{}".format(len(t1.string),t1.string.replace(' ', '').replace('\n', '').replace(';', '')))
                                # print(t1.string.strip(),end=" ")
                                otherlist.append(t1.string.replace(' ', '').replace('\n', '').replace(';', ''))
    print("第{}条,耗时{}秒".format(numberall,time.perf_counter()-startTime))

    return otherlist
                # elif isinstance(tag,bs4.element.NavigableString):
                #     print(tag.string)
                # else:
                #     print(type(tag))






# 爬取链家列表获取详细数据
def main():
    # startTime = time.clock()
    # for i in range(1,100):
    #     timeStart = time.perf_counter()
    #     print(timeStart)
    url = "https://cd.fang.lianjia.com/loupan/pg{}/".format(1)
    # 获取url的html
    html = GetHtml.getHTMLTest(url)
    # 将html数据放入uinfo
    allhouser = parserList(html)
    print(allhouser)
    for houser in allhouser:
        # print(len(houser[8]))
        print(houser)
        # 集中写入数据库
        # obj = OrmTest()
        # rest = obj.add_one(houser)
        # print(rest.id)
        # print(time.perf_counter() - timeStart)

    # endTime = time.clock()-startTime
    # print("爬取完毕,爬取时长{}".format(endTime))


# 遍历列表条件获取列表/nht1nht2nht4nht3nht5
#     for i in range(1,6):
#         condition = "nht{}".format(i)
#         print(condition)

def mainStatusList():
    startTime = time.clock()
    for i in range(1,39):
        timeStart = time.perf_counter()
        url = "https://cd.fang.lianjia.com/loupan/nht{}pg{}/".format(5,i)
        # 获取url的html
        html = GetHtml.getHTMLTest(url)
        # 将html数据放入uinfo
        allhouser = parserUpdateList(html)
        # allhouser = parserList(html)
        print(allhouser)
        for houser in allhouser:
            # print(len(houser[8]))
            print(houser)
            # 集中写入数据库
            obj = OrmTest()
            rest = obj.add_one(houser)
            print(rest.id)
            print(time.perf_counter() - timeStart)
    endTime = time.clock()-startTime
    print("爬取完毕,爬取时长{}".format(endTime))



# main()
if __name__ == '__main__':
   # main()
    mainStatusList()