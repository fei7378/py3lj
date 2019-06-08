#WeekNamePrintV1

weekStr = "星期一星期二星期三星期四星期五星期六星期日"
weekId = eval(input("请输入星期数字(1-7):\n"))
pos = (weekId -1)*3
print(weekStr[pos:pos+3])

# 简单版
weekStrSimple = "一二三四五六日"
weekIdSimple = eval(input("请输入星期数字(1-7):\n"))
print("星期"+weekStrSimple[weekIdSimple-1])