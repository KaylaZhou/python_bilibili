# 装饰器(有参,多参函数)

import time


def decorator(func):
    def wrapper(*args):  # 可变参数(*+任意参数名,可以支持不同个数参数列表的函数)下面函数有参时,需要增加参数
        print(time.time())
        # func(func_name)  # 以下函数是一个参数时
        func(*args)

    return wrapper


@decorator
def f1(func_name):  # 有参函数
    print('This is a function')


@decorator
def f2(func_name1, func_name2):  # 多参函数
    print('This is a function' + func_name1)
    print('This is a function' + func_name2)


f1('test func')
f2('test func1', 'test func2')
