# age = "666"
# new_age = age+666
# print(new_age)


# age = "666"
# new_age = age+"666"
# print(new_age)


# age = "anf"
# new_age = age + "fj6"
# print(new_age)


# age = '666'
# new_age = age+666
# print(new_age)


# age = 18
# new_age = age+1
# print(new_age)


# age = 3
# new_age = age*4
# print(new_age)


# age = 'name'
# new_age = age * 2
# print(new_age)


# age = 12
# Value = age > 15
# print(Value)


# age = 12
# Value = age <= 15
# print(Value)


# user_name = input('请输入名字:')
# new_name = user_name+'已输入'
# print(new_name)


# gender = input("请输入名别:")
# if gender == "男":
#     print('再见')
# elif gender == '女':
#     print('来呀来呀')
# elif gender == '人妖':
#     print('找ngh去,他也是')
# else:
#     print('滚')

# print('end')


# num = input('请输入数字:')
# number = int(num)
# if number >= 50:
#     print('大了')
# else:
#     print('小了')


# use = input('请输入用户名:')
# pws = input('请输入密码:')
# if use == '小王'and pws == '666':
#     print('登录成功')
# else:
#     print('用户名或密码错误')


# message = '''欢迎致电10086
# 1.话费查询:
# 2.流量查询:
# 3.人工服务:'''
# print(message)

# input('请输入你要选择的内容:')
# message_new = int(message)
# if message_new == '1':
#     print('话费查询:')


def variable():

    a = 1
    b = 3
    a = b

    print(b)

    a = [1, 2, 3, 4, 5, ]
    b = a
    a[0] = '1'  # 将列表中的1,替换为字符串'1'
    print(a)


# variable()


def genre():
    # 可变
    a = 'hello'
    a = a + 'python'  # str是不可变,此时的a+'python,得到了一个新的变量
    print(a)
    # 输出: hellopython


# genre()


# 判断变量类型: 使用id()函数
# b = 'hello'
# print(id(b))
# a = b + 'python'
# print(id(a))


def genre_2():
    # 不可变类型:
    print(id('python'[0]))  # 3205035870576
    print('python'[0])      # p

    # 'python'[0]='o'
    # print(id('python'[0]='o'))  # 报错,str不可改变类型
    # print('python'[0]='o')
# 运行时错误 - print
# 编译时错误 -

# genre_2()


def class_1():

    # 值类型int
    a = 1
    b = a
    a = 3
    print(a)
    print('b..', b)
    print('.............')

    # 引用类型 list可变的
    a = [1, 2, 3]
    b = a
    a[0] = '1'  # 数字是可变的
    print(a)
    print('b..', b)


# class_1()


def lass_2():
    a = 'hello'
    print(id(a))
    print(id(a))

    a = a + 'python'
    # print(a)
    print(id(a))

    # 反向验证:str不可变
    print('python'[0])  # 可以访问
    print('python'[0:3])
    print('python'[0] == 'n')  # 不能改变


# lass_2()


# 列表的可变 与元组的不可变

a = (1, 2, 3, [1, 2, ['a', 'b', 'c']])
print(a[3])
print(a[3][2])
print(a[3][2][1])


b = (1, 2, 3, [1, 2, 4])
b[3][1] = '2'
print(b)
