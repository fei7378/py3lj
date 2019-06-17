import GetHtml
import bs4

import re

from SQLPictureOEM import PictureBean
from SQLPictureOEM import Picture
from SQLCatalogOEM import CatalogBean
import SQLCatalogOEM
from SQLStatusListOEM import StatusList
import time



def parserList(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    all_tag = soup.find(name='div', attrs={'class': 'all-list'})
    # print(all_tag)
    images = []
    items = []
    try:
        for tag in all_tag:
            if isinstance(tag, bs4.element.Tag):

                for tag1 in tag:
                    if isinstance(tag1, bs4.element.Tag):

                        for tag2 in tag1:
                            if isinstance(tag2, bs4.element.Tag):

                                for tag3 in tag2:
                                    if isinstance(tag3, bs4.element.Tag):

                                        for tag4 in tag3:
                                            if isinstance(tag4, bs4.element.Tag):

                                                src = tag4.get("src")
                                                srcs = src.split("!")
                                                # print(srcs[0])
                                                images.append(srcs[0])
                                            # else:
                                            #     print(tag4)
                                    else:
                                        if len(tag3.string)>1:
                                            # print("不同类型的楼盘图片".center(70, ">"))
                                            if(len(images)>0):
                                                items.append(images)
                                            images = []
                                            # print(tag3)
                                            items.append(tag3)
        items.append(tag3.string)
    except:
        print("异常内容   {}".format(items))
    # print(items)

    return items


def itemToNews(items):
    images_obj = PictureBean()
    for i in range(0, len(items), 2):
        # print(items)
        title = ['效果图', '实景图', '样板间', '区位', '小区配套', '项目现场', '预售许可证']
        for pid in range(0, 7):
            patternpro = re.compile(title[pid])
            # print(items[i])
            name = re.findall(patternpro, items[i])

            # print(len(name))
            if len(name) == 1:
                # print(pid)
                if pid == 0:
                    images_obj.designImages = ','.join(items[i + 1])
                elif pid == 1:
                    images_obj.realImages = ','.join(items[i + 1])
                elif pid == 2:
                    images_obj.sampleImages = ','.join(items[i + 1])
                elif pid == 3:
                    images_obj.locationImages = ','.join(items[i + 1])
                elif pid == 4:
                    images_obj.matchImages = ','.join(items[i + 1])
                elif pid == 5:
                    images_obj.sceneImages = ','.join(items[i + 1])
                elif pid == 6:
                    images_obj.licenseImages = ','.join(items[i + 1])
    return images_obj

def test():
    HtmlText = GetHtml.getHTMLTest("https://cd.fang.lianjia.com/loupan/p_{}/xiangce/".format(item.SonUrl))
    # 获取全部图片
    items = parserList(HtmlText)


def main():
    startTime = time.clock()
    # 查询目录
    # catalog_obj = SQLCatalogOEM.OrmTest()
    # result = catalog_obj.test_search()
    staList_obj = StatusList()
    result = staList_obj.test_search()

    obj = Picture()
    for item in result:

        status = obj.selectBySonUrl(item.SonUrl)
        # print(status)
        if not status:
            # print("当前不存在,进行爬取")
            timeStart = time.perf_counter()
            # print(item.SonUrl,item.name)
            HtmlText = GetHtml.getHTMLTest("https://cd.fang.lianjia.com/loupan/p_{}/xiangce/".format(item.SonUrl))
            # 获取全部图片
            items = parserList(HtmlText)
            if len(items) > 0:
                # print(items)
                # print(len(items))
                print(item.SonUrl,item.name)
                images_obj = itemToNews(items)
                images_obj.name = item.name
                images_obj.SonUrl = item.SonUrl
                # images_obj.ImageBackup = ','.join(items)
                # print(images_obj.licenseImages)
                # 集中写入数据库
                obj = Picture()
                rest = obj.add_one(images_obj)
                print("第{}条爬取完成,用时 {}".format(rest.id, time.perf_counter() - timeStart))
        else:
            print("数据重复,重复Url:{}".format(item.SonUrl))

    endTime = time.clock()-startTime
    print("爬取完毕,爬取时长{}".format(endTime))









if __name__ == '__main__':
    main()