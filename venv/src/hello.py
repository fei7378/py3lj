# 单行注释
'''
多行注释
'''
import requests
r = requests.get("http://www.baidu.com")
print(r.status_code)
print(r.encoding)
r.encoding = 'utf-8'
print(type(r))
print(r.text)
str = 'fei'
print(str in ['fei','yang'])
'''
整数
0B开头  二进制binary
0O开头  八进制octal
0X开头  十六进制hexadecimal
pow(2,100) 表示2的100次方
使用int(param)转换为整数
'''
'''
浮点类型
使用round(0.1+0.2,1)==0.3   后一个1是小数截取位数  表示对前一个参数进行四舍五入
通常在第16位小数后才会出现不确定小数
使用float(param)转换为浮点 
'''
'''
/可能结果是浮点数 //是其他语言的整数除/
x%y 余数   模运算  10%3结果是1
x**y幂运算 y为小数是开方运算
'''