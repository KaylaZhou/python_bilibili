# map
def c():

    list_a = [1, 2, 3, 4, 5, 6, 7, 8]

# 已知x, 求x的平方

    def f(x):
        return x * x

    r = map(f, list_a)

    print(list(r))


# c()


# map 与lambda结合使用
list_a = [1, 2, 3, 4, 5, 6, 7, 8]
list_b = [1, 2, 3, 4, 5, 6]

# lambda表达式替换函数
r = map(lambda a, b: a * b+b, list_a, list_b)

print(list(r))
