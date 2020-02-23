
def c():

    list_x = [1, 0, 0, 1, 0, 1]
    # 过滤剔除掉0
    r = filter(lambda x: True if x == 1 else False, list_x)
    r1 = filter(lambda x: x, list_x)

    # 与map一样, 最终得到的都是一个集合, 所以打印时需要list转换一下
    print(list(r))
    print(list(r1))


c()
