import time
# 打印函数的时间
# 用非装饰器实现


def f1():
    print('This is a function')

# 对修改时封闭的, 对扩展式开放的


def f2():
    print('This is a function')


# print(time.time())
# f1()
# print(time.time())
# f2()

def print_current_time(func):  # 函数可以作为另外一个函数的参数被传递进来
    print(time.time())
    func()


print_current_time(f1)
print_current_time(f2)

# 如何解决:让新添加的业务逻辑依然可以和老函数绑定在一起, 体现出是对原来函数功能的增加, 同时又不更改函数内部的实现?
# 使用装饰器
