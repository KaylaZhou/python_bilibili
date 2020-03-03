from urllib import request

url = 'https://www.shui5.cn/article/FaGuiJieDu/'
ff = request.urlopen(url)
htmldata = ff.read()
# html = htmldata.decode('UTF-8')

with open('./shui5.html', 'w', encoding='utf-8') as code:
    code.write(str(htmldata))

print(str(htmldata))
