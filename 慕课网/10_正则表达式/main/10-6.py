import re


def x1():

    lanuage = 'PythonC#JaveC#PHPC#'

    r1 = re.sub('C#', 'GO', lanuage, 1)  # 实现超强的复杂替换,使用re.sub
    r2 = lanuage.replace('C#', 'GO')  # 常规的替换,使用replace

    print(r1)
    print(r2)


# x1()

# sub强大功能(第二个参数可以是函数)

lanuage = 'PythonC#JaveC#PHPC#'
r = re.sub('C#', 'GO ', lanuage, 1)

print(r)
