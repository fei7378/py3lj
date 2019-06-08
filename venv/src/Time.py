'''
时间获取 time() ctime() gmtime() localtime()  本地 转时间戳时使用
时间格式话 strftime() strptime()
程序计时 sleep(),perf_counter()
'''
import time
print(time.time())
print(time.ctime())
print(time.gmtime())
print(time.localtime())
timeStr = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(timeStr)
# print(time.strptime(timeStr,"%Y-%m-%d %H:%M:%S"))
# print(time.perf_counter())
