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
    print(id('python'[0]='o'))  # 报错,str不可改变类型
    print('python'[0]='o')


genre_2()
