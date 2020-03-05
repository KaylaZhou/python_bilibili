from urllib import request

# 通过向Request对象发送请求,获取网址
req = request.Request('http://www.shui5.cn/')

# 使用add_header()方法添加信息 查看网址代码中network下的name下的headers中最后部分User-Agent:
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36 Edg/80.0.361.62')

# 通过urlopen函数,获取网址数据
resp = request.urlopen(req)

# 读取文件
html = resp.read()

# decode中的内容查看爬取网页代码中network下的name下的charset="xxx"
writeTxt = html.decode('gb2312')


file = open('./shui5.html', "w", encoding='gb2312')
file.write(writeTxt)

print(writeTxt)
