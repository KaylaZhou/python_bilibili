# 装饰器 进一步优化
import time


def decorator(func):
    def wrapper(*args, **kw):  # (单*无法兼容f3里面的关键字参数,需要加入**kw)
        print(time.time())
        func(*args, **kw)
        # 在python中,若使用(单*args,双**kw)的调用形式,不管函数定义的参数是几个或者什么类型,都可以调用
    return wrapper


@decorator
def f1(func_name):
    print('This is a function')


@decorator
def f2(func_name1, func_name2):
    print('This is a function' + func_name1)
    print('This is a function' + func_name2)


@decorator
def f3(func_name1, func_name2, **kw):  # 关键字参数(**+任意参数名)
    print('This is a function' + func_name1)
    print('This is a function' + func_name2)
    print(kw)


f1('test func')
f2('test func1', 'test func2')
f3('test func1', 'test func2', a=1, b=2, c='123')  # 装饰器,适用于任何的参数列表
