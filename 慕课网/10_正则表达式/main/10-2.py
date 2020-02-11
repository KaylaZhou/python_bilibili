import re

a = 'c0c++7java8c#9python6javascript'

r = re.findall('python', a)
print(r)
# 规则
if len(r) > 0:
    print('字符串中包含python')
