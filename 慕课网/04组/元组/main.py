print((1, 2, 3, 4, 5,))
print((1, 2, 3) + (4, 5, 6))
print((1, 2, 3) * 2)
print((1, 2, 3, 4, 5)[3])
print((1, 2, 3, 4, 5)[0:3])
print((-1, '3', 'kayla', 'True', '3.8', ['北京'], {'你好'}))


print(type((1, 2, 3, 4, 5)))
# <class 'tuple'>
print(type(()))  # 表示空的元组
# <class 'tuple'>
print(type((2,)))  # 加个逗号后,会识别为元组
# <class 'tuple' >

print(type((2)))  # 系统会将()识别为数学运算符类处理
# <class 'int' >

print(type('hello'))
# <class 'str'>
