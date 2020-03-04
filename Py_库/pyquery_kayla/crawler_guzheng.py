from pyquery import PyQuery as pq
from urllib import request

hts = request.Request('https://www.guzheng.cn/zhengren/')
hts.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36 Edg/80.0.361.62')
hts_h = request.urlopen(hts)
html = hts_h.read()
writeTxt = html.decode('utf-8')

file = open('./guzheng.html', 'w', encoding='utf-8')
file.write(writeTxt)

# print(writeTxt)

# 解析
