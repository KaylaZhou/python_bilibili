'''
a = 1
b = 1
c = 1
a, b, c = 1, 2, 3
# 如何增强阅读性?
d = 1, 2, 3
print(type(d))

a=b=c=1  # 更简洁的写法

'''


'''
# 获取剩余部分:
a, b, *c = 1, 2, 3, 4    #(*获取的值默认为 list)
print(a, b, c)
# 输出结果:1 2 [3, 4]
'''


'''
# 获取中间部分:
a, *b, c = 1, 2, 3, 4
print(a, b, c)

# 输出结果: 1 [2, 3] 4
'''


'''
# 如果左值比右值少，那么带 * 的变量获取多个元素
a, *b = 1, 2, 3
print(a, b)
# 1 [2, 3]
'''


'''
# 如果左值比右值要多，那么带 * 的变量默认为空
a, *b, c = 1, 2
print(a, b)

# 输出结果:1 []
'''

'''
# 嵌套解包:
(a, b), (c, d) = (1, 2), (3, 4)
print(a, b, c, d)
# 输出结果:1 2 3 4
'''

'''
s = '123456789'
while s:
    x, s = s[0], list(s[1:])
    print(x, s)
'''


def add(x, y):
        # x,y叫做 形参(在函数定义的过程中的参数)
    result = x + y
    print(x, y)


# add(x=1)  # 定义多少形参,就要传递多少实参,否则会报错

# c = 50  # 全局变量


def demo():

    c = 10  # 局部变量

    # print(c)
    for i in range(0, 9):
        a = 'a'
        c += 1
    print(c)    # python中没有块级作用域
    print(a)   # python中在for循环外部可以引用for循环内部的变量


# demo()
