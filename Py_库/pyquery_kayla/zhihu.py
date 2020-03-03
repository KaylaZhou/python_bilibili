from urllib import request

url = 'http://www.shui5.cn/article/FaGuiJieDu'
f = request.urlopen(url)
htmldata = f.read()
# html = htmldata.decode('UTF-8')

with open(url, 'w', encoding='UTF-8') as code:
    code.write(htmldata)

print(htmldata)


# url = 'http://www.shui5.cn/'
# request.urlretrieve(url, "html")
# print(request.urlretrieve)
