#coding =utf-8
from urllib import request


req = request.Request('http://www.jianshu.com')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36 Edg/80.0.361.62')
resp = request.urlopen(req)
html = resp.read()

writeTxt = html.decode('utf-8')
# print(writeTxt)

# 写文件

file = open("jianshu.html", "w", encoding='utf-8')  # a 以追加的方式打开 (默认以只读方式打开)

# 2. 写入文件
file.write(writeTxt)

# 3. 关闭
file.close()
