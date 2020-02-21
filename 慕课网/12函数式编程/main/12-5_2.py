# 装饰器
import time


def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper


@decorator
def f1():  # 无参函数
    print('This is a function')


f1()  # 不需要改变原来的调用方式

# 接受定义时的复杂,不接受调用时的复杂
