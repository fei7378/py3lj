#exception handling 异常处理
try:
    num =eval(input("请输入一个整数\n"))
    print(num**2)
except:
    print("输入的不是整数")
else:
    print("成功后执行")
finally:
    print("无论是否出现异常都要执行")

try:
    num = eval(input("请输入第二个整数-\n"))
    print("num**2")
except NameError:
    print("捕获到NameError")