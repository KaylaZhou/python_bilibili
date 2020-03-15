# # Value = 11 % 3
# # print(Value)


# # 打印1-100之间的奇数
# # num = 1
# # while num <= 100:
# #     val = num % 2
# #     if val == 1:
# #         print(num)
# #     num = num+1

# # 打印1-100之间的偶数
# # num_1 = 1
# # while num_1 <= 100:
# #     val = num_1 % 2
# #     if val != 1:
# #         print(num_1)

# #     num_1 = num_1+1

# # 打印1-100之间的偶数
# # num_2 = 1
# # while num_2 <= 100:
# #     val = num_2 % 2
# #     if val == 1:
# #         pass
# #     else:
# #         print(num_2)

# #     num_2 = num_2+1


# # 打印 1-100之间所有的数相加


# # 打印 1-2+3-4+5-6+7....100的结果


# # 布尔值转换:
# # value = 1 or 9
# # print(value)
# # 打印结果:1

# # value = 0 or 9
# # print(value)
# # 打印结果:9

# # value = 9 or 0
# # print(value)
# # 打印结果: 9


# # def funName():
# #     value = 0 or 9 or 8
# #     print(value)

# # funName()


# # def funName2():
# #     value = 0 or 9 or 8
# #     print(value)


# # funName2()

# def mmm():

#     v1 = 1 and 8      # 当 and 前面的值为真时,打印的结果为:and后面的值
#     v2 = 1 and 0
#     v3 = 0 and 1       # 当 and 前面的值为假时,不用看and 后面的值
#     v4 = 0 and ""
#     v5 = 1 and 0 and 9   # 从左到右依次比较

#     print(v1)
#     print(v2)
#     print(v3)
#     print(v4)
#     print(v5)


# # mmm()


# # 综合: and or(先看and,再看or)
# # nn = 1 and 0 or 9 and 8

# # print(nn)
# # 结果为: 8


# mm = 0 or 1 and 9 or 0  # 先看and,再看or
# 0 or 9 or 0
# print(mm)
# # 结果为: 9


# # value = 0 or ""
# # print('-->', value, '<--')
# # 结果为: - -> <--


# # if 1 > 0 and 1 > 2:
# #     print('666')

# b = 1
# b += b >= 1
# print(b)

def judge():
    # 成员运算符,字典的用法:

    b = '1'
    print(b in {'a': 2})  # False

    b = 2
    print(b in {'a': 2})  # False

    b = 'a'
    print(b in {'a': 2})  # True  字典中以key为判断依据


# judge()


def judge_1():
    # 身份运算符;

    # a = {1, 2, 3}
    # b = {2, 1, 3}
    # print(a is b)   # False a和d的id()函数不同
    # print(a == b)  # True 集合是无序的,值相等

    c = (1, 2, 3)
    e = (2, 1, 3)
    print(c is e)  # False c和e的 id()函数不同
    print(c == e)  # False 元组是有序的,值不相等


# judge_1()

def mold():
    # 判断变量的值,身份与类型
    a = 'kayla'

    print(type(a) == int)  # False
    print(type(a) == str)  # True
    print(isinstance(a, str))  # True
    print(isinstance(a, int))  # False
    print(isinstance(a, (int, str, float)))  # True
    print(isinstance(a, (int,  float)))  # False


# mold()

# 位运算符 &
# 先转换成十进制;再转换为二进制;最后把二进制的数字做比较;得出结果
# 比较方法:如果, 2和 3 的二进制分别是10,11, 两组数字纵向比较,相对应的都为 1, 结果为1; 有一个为0, 结果则为o.
# a = 2
# b = 3
# print(a & 3)  # 2  a的二进制数位1 0, b的二进制数位1 1,
# print(a | b) ctrl + '~'
# 3 只要有一个为1,得到的结果是1,最终结果是而二进制的1,转换位十进制就是3

# 10
# 11
'''
b = 1
b += b >= 1
print(b)
'''

a = {1, 2, 3}  # 集合 无序的
b = {2, 1, 3}
print(a == b)
print(a is b)


c = (1, 2, 3)  # 元组 有序的
d = (2, 1, 3)
print(c == d)
print(c is d)
