import re
lanuage = 'PythonC#\nJavaPHP'
# 4~8
r1 = re.findall('c#', lanuage, re.I)
r2 = re.findall('c#.{3}', lanuage, re.I | re.S)  # re.S 匹配所有字符,包括换行符; |表示且
# re.S里的 . ,意思是改变c#.中.的行为,使表达式匹配换行符
print(r1)
print(r2)
