TempStr = input("请输入带有符号的温度值:")
if TempStr[-1] in ['F','f']:
    #评估函数eval() 去掉参数最外侧的引号并执行余下的语句
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转换后的温度为{:.2f}F".format(F))  #格式话
else:
    print("输入格式错误")
