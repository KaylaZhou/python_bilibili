from urllib import request

reqUrl = "http://www.jianshu.com"

req = request.Request(reqUrl)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36 Edg/80.0.361.62')

resp = request.urlopen(req)

html = resp.read()

writeTxt = html.decode('utf-8')

# 写文件
