#conditional judgement 条件控制
guess = eval((input("请输入猜测的数字\n")))
if guess == 99:
    print("猜对了")
else:
    print("猜错了")
print("二分支结构紧凑形式".center(20,"-"))

print("猜{}了".format("对" if guess==99 else "错"))

print("多分支结构".center(20,"-"))
if guess==99:
    print("猜对了")
elif guess>=90:
    print("数字在90及以上")
else:
    print("猜错了")
'''
条件组合
and  逻辑与
or  逻辑或
not  逻辑非
'''