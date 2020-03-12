# 列表推导式
# map filter
# set dict 也可以被推导


def aa():

    a = [1, 2, 3, 4, 5, 6]
    # a = {1, 2, 3, 4, 5, 6}  # 可以是set

    # 用for便利,但是for的前面可以实现for循环的操作
    b = [i**3 for i in a]
    b = [i*i for i in a]
    b = {i**2 for i in a if i >= 5}

    print(b)


aa()
