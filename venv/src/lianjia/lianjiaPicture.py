import GetHtml
import bs4

def parserList(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    all_tag = soup.find(name='div', attrs={'class': 'all-list'})
    # print(all_tag)
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
                                            print(srcs[0])
                                        # else:
                                        #     print(tag4)
                                else:
                                    if len(tag3.string)>1:
                                        # print("不同类型的楼盘图片".center(70, ">"))
                                        print(tag3)








def main():
    HtmlText = GetHtml.getHTMLTest("https://cd.fang.lianjia.com/loupan/p_{}/xiangce/".format("hdwlcaftcw"))
    parserList(HtmlText)




if __name__ == '__main__':
    main()