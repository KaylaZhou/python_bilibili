from urllib import request


class Cpa():
    url = 'http://www.cicpa.org.cn/'

    def __fetch_content(self):
        r = request.urlopen(Cpa.url)  # 通过request.urlopen方法,接受url,url就是要抓取网页的地址
        html = r.read()  # 通过read方法读取html
        print(html)


# cpa = Cpa()
# print(cpa.html)
