import requests
# from bs4 import BeautifulSoup
import bs4
import GetHtml
import re
import time
from SQLStatusListOEM import StatusList
from SQLHouseListOEM import HouseList
# 计数变量
numberall = 0
# 获取html的数据

# 使用beautifulsoup库解析html
def parserList(html):
    global numberall

    soup = bs4.BeautifulSoup(html, "html.parser")
    # print(type(soup))
    all_tag = soup.find(name='ul',attrs={'class':'item-list clear'})
    # 获取的信息遍历房屋
    # print(all_tag)
    houseList = []


    # allhouser = []
    for tag in all_tag.children:
        if isinstance(tag, bs4.element.Tag):
            # print("house[".center(180, "-"))

            houseItem = []
            for tag1 in tag.children:
                # print(tag1)
                if isinstance(tag1, bs4.element.Tag):

                    for tag2 in tag1:
                        if isinstance(tag2, bs4.element.Tag):
                            # 获取标签名字
                            if len(tag2)>0:
                                tag2name = tag2.name
                                if tag2name == "span":
                                    # 获取名称价格状态
                                    # print("span[".center(80,"-"))
                                    spanPrice = ''
                                    for tag2span in tag2:
                                        spanPrice += tag2span.string
                                        # print(tag2span.string)

                                    houseItem.append(spanPrice)

                                    # print(tag2)
                                    # print("]span".center(80, "-"))
                                elif tag2name == "div":
                                    # 获取图片
                                    # print("div[".center(80, "-"))
                                    for tag2div in tag2:
                                        # print("div[".center(80, "-"))
                                        # print(tag2div)
                                        # print(type(tag2div))
                                        # print("]div".center(80, "-"))
                                        if isinstance(tag2div, bs4.element.Tag):

                                            # 获取图片链接
                                            #
                                            # print(tag2div)
                                            # print(tag2div['src'])
                                            try:
                                                houseItem.append(tag2div['src'])
                                            except KeyError:
                                                print()
                                            # print(type(tag2div))
                                    # print("]div".center(80, "-"))
                                elif tag2name == "ul":
                                    # print("ul[".center(80, "-"))
                                    for tag2ul in tag2:

                                        if len(tag2ul.string)>1:
                                            houseItem.append(tag2ul.string)
                                            # print(tag2ul.string)

                                    # print(tag2)
                                    # print("]ul".center(80, "-"))
                            #     else:
                            #         houseItem.append(tag2name)
                            #         print(tag2name)
                            # else:
                            #     houseItem.append(tag2)
                            #     print(tag2)
            houseList.append(houseItem)
    return houseList



                    #
                    #         for tag3 in tag2:
                    #             if isinstance(tag3, bs4.element.Tag):
                    #
                    #                 for tag4 in tag3:
                    #                     if isinstance(tag4, bs4.element.Tag):
                    #
                    #                         for tag5 in tag4:
                    #                             if isinstance(tag5, bs4.element.Tag):
                    #                                 print(tag5)
                    #
                    #
                    #                             else:
                    #                                 if len(tag5) > 1:
                    #                                     print(tag5)
                    #
                    #
                    #                     else:
                    #                         if len(tag4)>1:
                    #                             print(tag4)
                    #
                    #
                    #             else:
                    #                 if len(tag3)>1:
                    #                     print(tag3)





    #         numberall=numberall+1
    #         house = []
    #         house.append(numberall)
    #         # print("{}  >>> {}".format(numberall,tag.a.attrs['title']),end="  ")
    #         house.append(tag.a.attrs['title'])
    #
    #         # 获取下一页的跳转链接
    #         dataOther = tag.a.get("data-other-action")
    #
    #
    #         patternpro = re.compile(r'\&project_name=[a-zA-Z0-9]+\&')
    #         # print(dataOther[10:60])
    #         project_name_all = re.findall(patternpro, dataOther[10:60])
    #         # print(project_name_all)
    #         project_name = project_name_all[0].split("=")
    #         pn = project_name[1][:-1]
    #         # print(project_name[1][:-1])
    #         # 获取房屋详细信息
    #         # print(house)
    #         house.append(pn)
    #
    #         # 打印房屋全部信息
    #         # print(house)
    #         allhouser.append(house)

    # return all_tag



def main():
    slistObj = StatusList()
    result = slistObj.test_search()
    for son in result:
        print(son.SonUrl)

        url = "https://cd.fang.lianjia.com/loupan/p_{}/huxingtu/".format(son.SonUrl)
        # 获取url的html
        html = GetHtml.getHTMLTest(url)

        houseList = []
        if len(html) > 1:
            print("请求到数据")

            # 解析html
            houseList = parserList(html)
        else:
            print("不存在户型数据")
        print(houseList)
        for house in houseList:
            house.append(son.SonUrl)
            house.append(son.name)
            # print(len(house))
            # print(house)
            # print(house[0])
            HouseObj = HouseList()
            HouseObj.add_one(house)





# main()
if __name__ == '__main__':
   main()