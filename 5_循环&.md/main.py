
# 1.While练习:
# 练习一,通过循环,给每次输出的结果加 1
'''
num_1 = 1
while True:
    print(num_1)
    num = num_1+1
'''


# 练习二,通过循环,输出1.2.3...10.
'''
num_2 = 1
while num_2 <= 10:
    print(num_2)
    num_2 = num_2+1
'''


# 练习三,通过循环,输出1.2.3.4.5.6.8.9.10.
'''
val_1 = 1
while val_1 <= 10:
    if val_1 != 7:
        print(val_1)
    val_1 = val_1 + 1
'''


'''
# 注: 错误例子
val_1 = 1
while val_1 <= 10 and val_1 != 7:  # 此时会同时满足条件时,停止打印.输出结果为1...6,
    print(val_1)
    val_1 = val_1 + 1
'''


'''
val_2 = 1
while val_2 <= 10:
    if val_2 == 7:  # 同时满足条件等于7时,过pass(不做任何事情,用作占位语句)
        pass
    else:
        print(val_2)
    val_2 = val_2+1
'''


'''
val_3 = 1
while val_3 <= 10:
    val_3 = val_3 + 1
    if val_3 == 7:
        continue     # 跳出本次循环
    else:
        print(val_3)
'''

'''
# 2.While.else练习:

while True:
    print('你好')
    while True:
        print(666)
        break  # 终止第二个循环(输出结果:你好 666 你好 666 .......)
    break   # 终止所有循环(输出结果:你好 666)
'''


def counter():

    counter = 1
    while counter <= 10:
        counter += 1
        print(counter)
    else:
        print('结束')


# counter()


# for循环
# for x in range(1, 10, 2):  # range,表示取值范围.2表示步长
#     # print(x, end='')  # end='',表示将结果打印为一行
#     print(x, end='|')  # '|',用分隔符将结果分隔开

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a[0:len(a):2]
print(b)
