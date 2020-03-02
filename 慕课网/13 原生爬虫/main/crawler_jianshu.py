from urllib import request


def getPage(url):
    request = request.Request(url)
    response = request.urlopen(request)
    return response.read().decode("utf-8")


url = 'http://www.jianshu.com'
result = getPage(url)
print(result)
