import time

num = 90000000

st = time.time()
startTime = int(round(st * 1000))

for i in range(num, 0, -1):
    pass
    # print(i)

et = time.time()
endTime = int(round(et * 1000))

print(endTime-startTime)
