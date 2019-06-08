#Data
# 二位数据类型通常使用CSV: Comma-Separated Values 格式存储 一般索引习惯ls[row][column] 先行后列 外层列表每一个元素是一行,按行存
ls = [['1','2','3'],['A','B','C'],['q','w','e']]
f = open("ff.csv",'w')
for item in ls:
    f.write(','.join(item)+'\n')
f.close()

fo = open("ff.csv")
ls = []
for line in fo:
    line = line.replace("\n","")
    ls.append(line.split(","))
    # ls.append(list(line.split(",")))
fo.close()
print(ls)