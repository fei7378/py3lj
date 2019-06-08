#CalPiV2.py 蒙特卡罗计算法
from random import random

from time import perf_counter
DARTS = 1000*1000
hits = 0.0
start = perf_counter()
for i in range(1,DARTS):

    x,y = random(),random()
    dist = pow(x ** 2 + y ** 2, 0.5)#判断随机撒的点是否在园内
    if dist <=1.0:
        hits +=1
pi = 4 * (hits/DARTS)
print("圆周率的值是:{}".format(pi))
print("运行时间是:{:.5f}s".format(perf_counter() - start))
