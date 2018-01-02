temp,sum = 1,0
for i in range(1,11):
    temp *= i
    sum += temp
print("一到十的阶乘为：{}".format(sum))
