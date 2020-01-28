c = 50


def add(x, y):
    c = x + y  # 此时的变量c和c=50的这个变量不同(虽然名字相同,但是作用范围不同)
    print(c)

# 变量的作用域


# add(1, 2)
# print(c)


def demo():

    c = 10  # 局部变量(相对于函数时局部变量,但对于for循环时全局变量)

    # print(c)
    for i in range(0, 9):
        a = 'a'
        c += 1
    print(c)    # python中没有块级作用域
    print(a)   # python中在for循环外部可以引用for循环内部的变量


# demo()


c = 1


def func1():
    # c = 2

    def func2():
        # c = 3
        print(c)
    func2()


func1()
