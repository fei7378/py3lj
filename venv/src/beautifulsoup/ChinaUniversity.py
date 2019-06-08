import requests
# from bs4 import BeautifulSoup
import bs4

def getHTMLTest(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist,html):
    soup = bs4.BeautifulSoup(html,"html.parser")
    # 循环tbody的子孙节点
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            # 获取td标签内容
            tds = tr('td')
            # print(tds)
            ulist.append([tds[0].string,tds[1].string,tds[2].string])


def printUnivList(ulist,num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    # 使用中文空格chr(12288)填充空白区域 {3}为指定使用第三个参数的字符填充
    print(tplt.format("排名","学校","位置",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

    # print("Suc" + str(num))





def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    # 获取url的html
    html = getHTMLTest(url)
    # 将html数据放入uinfo
    fillUnivList(uinfo,html)
    # 打印学校数据
    printUnivList(uinfo,20)
main()
