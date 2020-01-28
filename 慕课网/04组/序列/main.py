# str, list, tuple

# print('how are you ')
# print(['how are you'])
# print(('how are you'))


def all():
    # 序号:

    print(['how', 'are', 'you'][1])  # are
    # 每个list元素都对应一个序号
    print('how are you'[2])  # o
    # 每个str元素都对应一个序号
    print((1, 2, 3, 4, 5)[4])  # 5

    # 每个tuple元素都对应一个序号
# all()


def all_1():

    print('what\'s your name'[9])
    print(['what\'s your name'[9]])
    print(('what\'s your name')[9])


# all_1()


# len,求序列中有多少个元素
def num():

    print(len([1, 2, 3, 4, 5, 6]))
    print(len('hello world'))
    print(len(('hello world')))


# 输出结果:6
#         11
#         11


# num()


def value():
    # max,min
    print(max([1, 2, 3, 6, 8, 10, 7]))
    print(min([1, 2, 3, 6, 8, 10, 7]))
    print(max('hello world'))
    print(min('hello world'))  # 为空值,涉及到字符编码 ascll码
    print(min('helloworld'))  # 去掉空格后


value()
# print(ord('u'))
# print(ord('k'))
# print(ord('w'))
# print(ord(' '))  # 空字符串,对应的ascll码值为32
