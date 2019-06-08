import time
scale = 50
print("执行开始".center(scale//2,"-"))
start = time.perf_counter()
for i in  range(scale+1):
    # \r使光标回到行首  end=""使输出后不追加
    a = '#' * i
    b = '.' * (scale-i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,"-"))