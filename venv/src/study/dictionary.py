#dictionary 字典数据类型   (集合数据类型之三)
#字典类型使用{}或dict()创建
#d[key] 可索引可赋值
d = {'中国':'北京','美国':'华盛顿','法国':'巴黎'}
print(d["中国"])
# in  判读键是否在d中
print("法国" in d)
print("巴黎" in d)
#如果当中没有这个键则出异常
try:
    print(d["中"])
except KeyError:
    print("KeyError")
# 查看所有键
print(d.keys())
# 查看所有值
print(d.values())
# 新建空字典
de = {}
print(type(de))
de["a"] = 1;de["b"] = 2
de["b"] = 3
print("c" in de)
# de.clear()
print(de)
# de += {"中国":"北京","美国":"华盛顿"}
# print(de)
'''
d.get(k,<default>) 如存在时取出相应值  如键不存在则返回默认值
d.pop(k,<default>) 存在时取出并从原字典中删除 不存在时返回默认值
d.popitem(随机取出一个键值对 以元祖形式返回
d.clean() 删除所有键值对
len(d) 返回字典d中的元素的个数
'''
print(d.get("中国","伊斯兰堡"))
print(d.popitem())
print(d)
print(len(d))
#循环取出键
for k in d:
    print(k)
    print(d.get(k))