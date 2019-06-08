import random
random.seed(10)#设置随机数种子   相同的随机数种子的随机数也相同 默认的随机数是系统当前时间
print(random.random())
print(random.randint(1,60))#生成一个在指定范围的整数
print(random.uniform(10,100))#生成一定范围的随机小数
print(random.choice([12,34,"test","678"]))#从列表中随机选择一个元素
s = [1,2,3,4,5,6,7]
random.shuffle(s)#将序列中的元素打乱顺序
print(s)
