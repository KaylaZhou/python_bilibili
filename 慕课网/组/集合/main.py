def all_1():
    # 集合是无序的:
    print({1, 2, 3, 4, 5, 6})   # {1, 2, 3, 4, 5, 6}
    print({'hello world'})     # {'hello world'}


# all_1()


# def all_2():
#   # 错误的练习:不支持切片,下标索引
#     print({1, 2, 3, 4, 5, 6}[3:])
#     # print({1, 2, 3, 4, 5, 6}[3])


# # all_2()


def repetition():
  # 集合不重复
    print({1, 2, 3, 4, 5, 3, 3, 4, 4})
    print({'kayla', 'kayla', 'name'})


# repetition()


def trait():

    print(len({1, 2, 4, 6, 8, 9, }))
    print(len({'kayla', 'kayla', 'love', 'you'}))
    print(7 not in {1, 4, 7, 9, 0})
    print(7 in {1, 4, 7, 9, 0})
    print({1, 2, 3, 4} - {2, 3})
    print({1, 2, 3, 4} & {2, 3})
    print({1, 2, 3, 4} | {2, 3})


# trait()

print(type({}))
# <class 'dict'>
print(type(set()))
# <class 'set'>
print(len(set()))
# o
