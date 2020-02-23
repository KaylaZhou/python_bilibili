import re

a = 'c0c++7java8c#9python10javascript'

r1 = re.findall('\d', a)
print(r1)  # ['0', '7', '8', '9', '6']

r2 = re.findall('\D', a)
print(r2)
