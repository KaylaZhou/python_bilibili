# 在以下字符串中是否包含python?
# 方法一: 用index内置函数(不能满足各种各样的需求)


import re


def aa1():
    a = 'c|c++|java|c#|python|javascript'
    print(a.index('python') > -1)
    print('python' in a)  # 也可以用in操作符


# aa1()


# 方法二:

# import re使用正则表达式模块  (搜索字符串a, 在a中找到所有python)

a = 'c|c++|java|c#|python|javascript'

b = re.findall('pattern', a)  # 打印出:[]
r = re.findall('python', a)  # 打印出:['python']
print(b)
print(r)

if len(r) > 0:
    print('字符串中包含python')
