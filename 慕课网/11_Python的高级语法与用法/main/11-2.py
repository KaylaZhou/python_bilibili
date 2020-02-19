def f1():
    a = 10

    def f2():
        a = 20
    # return a
    #     print(a)  # 20
    # print(a)  # 10
    # f2()
    # print(a)  # 10


# f1()
# print(f1)
# print(f1.__closure__)


origin = 0


def go(step):
    global origin  # 全局变量声明
    new_pos = origin + step
    origin = new_pos  # 局部变量
    return new_pos


print(go(2))
print(go(3))
print(go(6))
