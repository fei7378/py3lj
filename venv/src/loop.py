# loop 循环
print("计数循环".center(20,"-"))
'''
range()函数产生数字序列
'''
for i in range(5):
    print(i)
print("特定次数计数循环".center(20,"-"))

for i in range(1,6):
    print(i)

print("配置步长的特定计数循环".center(20,"-"))

for i in range(1,6,2):
    print(i)

print("遍历字符串中的字符".center(20,"-"))

for c in "Python123":
    print(c,end=",") #end=是每个字符打印后的结尾 如不指定默认换行


print()

print("列表遍历循环".center(20,"-"))
for item in [123,"PY",456]:
    print(item,end=",")

print()
print("文本遍历循环,暂无".center(20,"-"))
# for line in fi:
#     print(line)

print("无限循环 while".center(40,"*"))
a = 3
while a>0 :
    print(a)
    a -= 1
print("循环控制保留字".center(40,"-"))
'''
break 跳出当前循环 执行循环后的语句
continue 结束当次循环 继续执行后续次数循环
'''
for c in "PYTHON":
    if c == "T":
        continue
    print(c,end="")

print()
for cc in "PYTHON":
    if cc == "T":
        break
    print(cc,end="")
print()
print("循环的扩展 else".center(20,"-"))
'''在没有遇到break的循环结束执行else'''
for c in "PYTHON":
    if c == "T":
        break
    print(c,end="")
else:
    print("正常退出")