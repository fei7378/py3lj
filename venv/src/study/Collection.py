#cellection 集合类型 不存在相同元素 (组合数据类型一)
'''
集合类型,序列类型(元祖类型,列表类型),字典类型
集合数据类型:
1.集合之间无序,每个元素唯一,不存在相同元素
2.集合元素不可被修改,是不可变数据类型
3.{a,b} 空集合的建立必须用set() 注意:使用{}表示创建字典类型  与字典类型相同使用大括号
'''
# A = {"python",123,"python",123}
# print(A)
# for i in A:
#     print(i)
# #字符会被拆分
# B = set("python")
# for i in B:
#     print(i)
C = {"p","y",123}
D = set("pypy123")
print("C-D",C-D)#减去在后者的所有元素 差
print("D-C",D-C)
print("C&D",C&D)#二者中的相同元素 交
print("D&C",D&C)
print("C|D",C|D)#二者中的所有元素 并
print("D|C",D|C)
print("C^D",C^D)#二者中的非相同元素 补
print("D^C",D^C)
print("C<=D",C<=D)#判断子集

print("增强操作符改变前者(|=,-=,&=,^=)".center(40,"-"))
C|=D
print(C)
print("集合处理方法".center(40,"-"))
C.add("qwer") #增加一个元素
print(C)
C.discard(123) #删除一个元素 如不存在不报错
print(C)
try:
    C.remove(123) #删除一个元素 不存在时报错
    print(C)
except KeyError:
    print("没有这个元素,出现KeyError异常")
C.clear() #删除集合中的所有元素
print(C)
try:
    c1 = C.pop() #随机删除一个元素 如为空产生KeyError异常
    print("删除的元素为{}".format(c1))
    print(C)
except KeyError:
    print("集合元素为空 出现KeyError异常")
'''
其他集合方法
S.copy()返回集合S的一个副本
len(S) 返回集合元素个数
x in S 判断x是否在集合中   返回True False
x not in S 判断x是否不在集合中   返回True False
set(x) 将其他数据类型转为集合类型

'''
#集合去重
A = [123,"测试",123]
print(A)
B = set(A) #将列表类型转换为集合
print(B)
A = list(B) #将集合类型转换为列表
print(A)