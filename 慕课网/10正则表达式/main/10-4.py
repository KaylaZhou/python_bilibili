# 概括字符集
import re
# a = 'python 11\11java&___\n78\rph\tp'
# r = re.findall('\d', a)
# r = re.findall('[^0-9]', a)
# r = re.findall('\w', a)  # 只能匹配单词字符(匹配不到 &)
# r = re.findall('[A-Za-z0-9_]', a)
# r = re.findall('\W', a)
# r = re.findall('\s', a)


# print(r)


# 边界匹配
# 例子:验证qq号是否符合4~8位?
qq = '100000001'
# 4~8
r1 = re.findall('\d{4,8}', qq)
r2 = re.findall('^\d{4,8}&', qq)  # 不符合匹配,(原字符串共9位,匹配条件是4~8)边界符是匹配完整的字符串意思.
r3 = re.findall('^0&', qq)  # 不符合匹配,^字符串的开始,&末尾
r4 = re.findall('000', qq)
r5 = re.findall('^000', qq)  # 不符合匹配,因为字符串的开始是1
r6 = re.findall('000&', qq)   # 不符合匹配,因为字符串的末尾是1

# print(r1)
# print(r2)
# print(r3)
# print(r4)
# print(r5)
# print(r6)


# 组
# 要求:判断字符串中,是否包含3个python?(假如100个啦)
a = 'pythonpythonpythonpythonpython'
b = re.findall('[python]{3}', a)

print(b)


e = 'abcabcabcabc'
z1 = re.findall('[abc]{3}', e)
z2 = re.findall('(abc){3}', e)

print(z1)
print(z2)
