from urllib import request


def getPage(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    return response.read().decode("utf-8")


url = 'https://www.jianshu.com/'
result = getPage(url)
print(result)
