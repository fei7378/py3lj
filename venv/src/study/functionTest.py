
def fact():
    global y
    print("不带参数的函数{}".format(y))
#当前为可选参数,可选参数有默认值 必须在必选参数前
def fact1(n,m=1):
    s = 1
    for i in range(1,n+1):
        s *=i
    return s//m
#可变参数
def fact2(n,*b):
    s = 1
    for i in range(1,n+1):
        s *= i
    for item in b:
        s*=item
    return s
'''
返回的数据可以多个 返回的类型是元祖类型
return a,b,c
接受时可以 a,b,c = fun()
[a,b,c] 列表类型
(a,b,c) 元祖类型
'''
'''
局部变量与全局变量
基本数据类型:  可以重名 且在函数中使用全局变量需要加保留字globle
组合数据类型:  如果局部变量为组合数据类型且未创建 则等同为全局变量
'''
#定义lambda函数
# x,y=1,5
# fact()
# def fact3():
#     return 2,6,9
# print(y)
# print(fact2(10))
#
# f3 = fact3()
# for i in f3:
#     print(i)
# x1,x2,x3 = fact3()
# print(x1,x2,x3)


#递归

def fact4(n):
    if n == 0:
        return 1
    else:
        return n*fact4(n-1)
print(fact4(5))