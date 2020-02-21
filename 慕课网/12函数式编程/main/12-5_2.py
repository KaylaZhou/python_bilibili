# 装饰器
import time


def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper


@decorator
def f1():
    print('This is a function')


f1()  # 不需要改变原来的调用方式
