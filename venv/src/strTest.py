str = "零一二三四五六七八九十"
print(str[-3:])
print(str*3)
print("倒叙:"+str[::-1])

sepStr = str.split(sep="四")
for i in range(len(sepStr)):
    print(sepStr[i])

print(str.center(70,"="))
print(str.strip("零四二十一"))

print(",".join(str))
#可以在槽中添加序号
print("{2} 测试 {0} 测试{1}".format("一号","二号","三号"))

print("{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}".format(425))


print( "ddd"+ "    ddd")
'''
str.lower() str.upper() 返回字符串的全部大写或全部小写
str.split(sep=None)根据sep分割
str.count(sub) 返回sub在str中出现的次数
str.replace(old,new) 将str中的old替换为new 返回副本
str.center(width,[fillchar])  将字符串在输出居中  

str.strip(chars) 从str中去掉其左和右侧chars中列出的字符
str.join(iter) 在iter除最后一个一个元素外的每一个元素后增加一个str

字符串的格式化
'''