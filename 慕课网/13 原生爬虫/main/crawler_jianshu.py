from urllib import request


class Crawler():
    url = 'https://www.jianshu.com/'

    def __fetch_content(self):
        r = request.urlopen(Crawler.url)
        html = r.read()  # 用read方法读取url结果

    def go(self):
        self.__fetch_content()


crawler = Crawler()
crawler.go()
