# 字符集

import re


# 或,[]表示或,a[或]c
b = 'abc,acc,adc,aec,afc,ahc'

s1 = re.findall('a[cf]c', b)
print(s1)  # ['acc', 'afc']

s2 = re.findall('a[^cfd]c', b)
print(s2)  # ['abc', 'aec', 'ahc']

s3 = re.findall('a[c-f]c', b)
print(s3)  # ['acc', 'adc', 'aec', 'afc']
