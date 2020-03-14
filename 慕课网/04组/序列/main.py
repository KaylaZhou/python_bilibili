# str, list, tuple

# print('how are you ')
# print(['how are you'])
# print(('how are you'))


def all():
    # 序号:
    # 每个list, str, tuple元素都对应一个序号
    print(['how', 'are', 'you'][1])  # are
    print('how are you'[2])  # o
    print((1, 2, 3, 4, 5)[4])  # 5

# all()


def all_1():

    print('what\'s your name'[9])
    print(['what\'s your name'[9]])
    print(('what\'s your name')[9])


# all_1()


def num():
    # len,求序列中有多少个元素

    print(len([1, 2, 3, 4, 5, 6]))
    print(len('hello world'))
    print(len(('hello world')))

# num()


def value():
    # max,min
    print(max([1, 2, 3, 6, 8, 10, 7]))
    print(min([1, 2, 3, 6, 8, 10, 7]))
    print(max('hello world'))

    print(min('hello world'))  # 为空值,涉及到字符编码 ascll码
    print(min('helloworld'))  # 去掉空格后 ,输出 d


# value()


def x():
    # ord 查看ascll码
    print(ord('u'))
    print(ord('k'))
    print(ord('w'))
    print(ord(' '))  # 空字符串,对应的ascll码值为32


x()


def cc():
    # 逻辑判断 in,not in
    print(3 in [1, 2, 3, 4, 5, 6])        # True
    print(3 not in [1, 2, 3, 4, 5, 6])    # False
    print(len(['hello', 1, 2, 3, 4, 5]))  # 6


# cc()
