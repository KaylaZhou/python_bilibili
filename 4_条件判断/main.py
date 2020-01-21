def term_1():

    a = input()  # print(type(a))
    a = int(a)  # 动态语言的缺点就是:python中input默认的是字符串,需要转换为int

    if a == 1:
        print('hello')
    elif a == 2:
        print('I\'m fine')
    elif a == 3:
        print('thanks')
    else:
        print('bye')


# term_1()


def criteria_1():
    # 练习: 打印结果为: a和b不可能同时为False
    # 方法一:
    a = 1
    b = 0

    if a == b:
        print(True)
    if a != b:
        print(False)
    else:
        pass


# criteria_1()


def criteria_2():
    # 练习: 打印结果为: a和b不可能同时为False
    # 方法一:
    a = 1
    b = 0
    # print(a or b)

    a or b


criteria_2()
