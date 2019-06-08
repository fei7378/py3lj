#Sequence  序列类型  (组合数据类型二)
#元素类型可以不同 可以使用下标访问
#序列类型是基类类型   使用时使用它的衍生类型 如字符串 元祖 列表
'''
六个操作符   在其的衍生类型中都适用
x in s 如果 x是序列s 返回True或False
x not in s 与上面相反
s+t 连接两个序列
s*n 或n*s 将序列复制n次
s[i]  索引返回值
s[i:j] s[i:j:k] 切片  k为步长

'''
print("x" in "xyz")
'''
五个通用函数和方法
len(s)  返回序列s的长度
min(s) 返回序列s的最小元素
max(s) 返回序列s的最大元素
s.index(x) 或 s.index(x,i,j)   返回序列s中第一此出现x的位置 可以使用i,j指定位置
s.count(x) 返回序列s中出现x的总次数
'''
#元祖类型  一旦创建就不能被修改
#使用 () 或 tuple()创建 亦可以不使用() 元素间用,分隔  可以使用tuple(x)将其他类型转换为元祖类型 防止数据被程序修改

s = 1,2
print(s)
print(s[::-1])
print(s)

#列表类型 []  使用[] 或list()创建  可以随意修改

'''
ls[i] = x 替换元素
ls[i,j,k] = lt 将列表lt替换切片
del ls[i] 删除列表
del ls[i,j,k] 删除切片
ls += lt 将lt增加到ls中
ls *= n 更新ls重复n次
方法
ls.append(x) 在列表最后增加一个元素x
ls.clean() 删除列表中的所有元素
ls.copy() 复制一个列表
ls.insert(i,x) 在列表i位置插入x
ls.pop(i) 将列表i位置的元素取出并删除
ls.remove(x) 删除列表中第一个出现的元素x
ls.reverse() 将列表ls中的元素反转
'''

bb = ['a','c','e']
ee = bb  #内存地址相同
bb1 = bb.copy() #复制了一份
del ee[2]
del bb1[0]
print(bb)
print(bb)


print("切片替换".center(20,"-"))
bb = ['a','c','e']
bb[1:2] = [1,2,3]
print(bb)
print("切片增加".center(20,"-"))
bb = ['a','c','e']
bb[1:2] += [1,2,3]
print(bb)
print("列表嵌套".center(20,"-"))
bb = ['a','c','e']
bb[1] = [1,2,3]
print(bb)
print("列表增加".center(20,"-"))
bb = ['a','c','e']
bb += [1,2,3]
print(bb)






print("题目".center(20,"-"))
lt = list()
lt +=[1,2,"s",3,4]
print(lt)
lt[1]="a"
print(lt)
lt.insert(1,2)
print(lt)
lt.remove(lt[0])
print(lt)
del lt[1:4]
print(lt)
print(0 in lt)
lt.append(0)
print(lt)
print(lt.index(0))
print(len(lt))
lt.remove(0)
print(max(lt))
lt.clear()
print(lt)