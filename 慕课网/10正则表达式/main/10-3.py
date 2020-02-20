# 字符集

import re


# 或,[]表示或,a[或]c
b = 'abc,acc,adc,aec,afc,ahc'

s1 = re.findall('a[cf]c', b)
# print(s1)  # ['acc', 'afc']

s2 = re.findall('a[^cfd]c', b)
# print(s2)  # ['abc', 'aec', 'ahc']

s3 = re.findall('a[c-f]c', b)
# print(s3)  # ['acc', 'adc', 'aec', 'afc']


# 数量词
a = 'python 1111java678php'
r1 = re.findall('[a-z]{3}', a)
r2 = re.findall('[a-z]{3,6}', a)   # 贪婪匹配(尽可能多的取最大的一个区间的值)
r3 = re.findall('[a-z]{3,6}?', a)  # 非贪婪匹配
# print(r1)
# print(r2)
# print(r3)


# 匹配 0 次或者无限多次
c = 'pythov0python1pythonn2'

x1 = re.findall('python*', c)
x2 = re.findall('python+', c)
x3 = re.findall('python?', c)  # 正则中,允许n出现0次或者1次,多出来的n会去掉.(去重)


print(x1)
print(x2)
print(x3)
