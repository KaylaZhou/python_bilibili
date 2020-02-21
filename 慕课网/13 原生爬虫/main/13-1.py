from urllib import request
# 断点调试


class Spider():
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()

    def go(self):
        self.__fetch_content()


spider = Spider()
spider.go()
