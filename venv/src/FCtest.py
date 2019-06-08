#测试
for i in range(5):
    TempStr = input("请输入温度")
    if TempStr[-1] in ['F','f']:
        C = (eval(TempStr[0:-1])-32)/1.8
        print("计算后的温度{:.2f}C".format(C))
    elif TempStr[-1] in ['C','c']:
        F = eval(TempStr[0:-1])*1.8+32
        print("计算后的温度{:.2f}F".format(F))
    else:
        print("格式错误")