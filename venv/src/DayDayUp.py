dayfactor = 0.005
dayup = pow(1+dayfactor,365)
daydown = pow(1-dayfactor,365)
print("向上:{:.2f},向下:{:.2f}".format(dayup,daydown))
dayup1 = 1.0
dayfactor1 = 0.01
for i in range(365):
    # 计算是否是是周末
    if i % 7 in [6,0]:
        dayup1 = dayup1*(1-dayfactor1)
    else:
        dayup1 = dayup1*(1+dayfactor1)
print(dayup1)