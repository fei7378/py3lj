#file 文件的操作
'''
open()  文件的打开
打开模式:
"r" 只读模式  默认值   如文件不存在返回FileNotFoundError
"w" 覆盖写模式,文件不存在时创建 存在时覆盖
"x" 创建写模式 文件不存在时报错 存在返回FileExistsError
"a" 追加写模式 不存在时创建 存在时在文件的最后追加内容
"b" 二进制文件模式
"t" 文本文件模式  默认值
"+" 与r/w/x/a一同使用 在原基础上增加同时读写的能力
'''
# tf = open("f.txt") #使文件处于打开状态  等价与tf = open("f.txt","rt")
tf = open("f.txt","a+")
print(tf.readline())
ls = ['中国','美国','日本']
# tf.write(' '.join(ls))

tf.close() # 如没有关闭 在程序正常退出时会关闭