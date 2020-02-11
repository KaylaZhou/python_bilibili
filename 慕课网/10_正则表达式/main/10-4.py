# 概括字符集
import re
a = 'python 11\11java&___\n78\rph\tp'
# r = re.findall('\d', a)
# r = re.findall('[^0-9]', a)
# r = re.findall('\w', a)  # 只能匹配单词字符(匹配不到 &)
# r = re.findall('[A-Za-z0-9_]', a)
# r = re.findall('\W', a)
r = re.findall('\s', a)


print(r)
