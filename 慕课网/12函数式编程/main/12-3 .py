from functools import reduce


def a():

    list_x = [1, 2, 3, 4, 5, 6, 7, 8]
# reduce连续计算,连续调用lambda
# ((((1+2)+3)+4)+5) 运算流程
    r = reduce(lambda x, y: x+y, list_x)
    r1 = reduce(lambda x, y: x+y, list_x, 10)  # 初始值10,第一次计算时参与

    print(r)
    print(r1)


a()

# reduce()的初始值
# list_x = ['1', '2', '3', '4']
# r = reduce(lambda x, y: x+y, list_x, 'aaa')
# print(r)
