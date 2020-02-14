import re


def x1():

    lanuage = 'PythonC#JaveC#PHPC#'

    r1 = re.sub('C#', 'GO', lanuage, 1)  # 实现超强的复杂替换,使用re.sub
    r2 = lanuage.replace('C#', 'GO')  # 常规的替换,使用replace

    print(r1)
    print(r2)


# x1()


def x2():
    # sub强大功能(第二个参数可以是函数)

    lanuage = 'PythonC#JaveC#PHPC#'

    def convert(value):
        matched = value.group()  # 调用value.group方法,拿到结果C#
        # print(value)  #value是一个对象,并不是简单的字符串
        # return '!!' + value + '!!'  #报错,不会直接将字符串传入函数
        return '!!' + matched + '!!'

    s1 = re.sub('C#', convert, lanuage, 2)  # 第四个参数数字,表示替换数量.

# 问题: convert被sub调用的流程?
# 1.如果把一个函数做为sub的第二个参数,传到sub参数列表之后
# 2.当正则表达式匹配到一个结果后(比如:sub中的C#匹配到第一个C#时,),
# 3.会将结果传到函数(value就是正则表达式所匹配的结果)
# 4.最终返回结果,将是一个新的字符串(也就是说,convert函数的返回结果,将被替替换为新的字符串)

    print(s1)


# x2()


# 把函数作为参数传递
# 练习:找出所有数字,把>=6的替换为9,反之替换为0
def x3():

    c = 'AB3C72D1D8E67'

    def convert(Value):
        matched = Value.group()
        if int(matched) >= 6:
            return '9'
        else:
            return '0'

    r = re.sub('\d', convert, c)
    print(r)


x3()
