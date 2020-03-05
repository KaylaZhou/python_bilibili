import re
from urllib import request
# 断点调试


class Cpa():
    url = 'https://shcpa.org.cn/'
    root_patter = '<ul class="hlist notice">([\s\S]*?)</ul>'  # ()可以去掉定界的内容

    def __fetch_content(self):
        r = request.urlopen(Cpa.url)  # 通过request.urlopen方法,接受url,url就是要抓取网页的地址
        html = r.read()  # 通过read方法读取html
        html = str(html, encoding='utf-8')  # 将html字节码转换为字符串
        # return html
        print(html)

# 分析文本
    def __analysis(self, html):
        root_html = re.findall(cpa.root_patter, html)
        print(root_html)

# /分析文本

    def go(self):  # 入口方法(也是总控方法,所有的函数调用最后都会汇集到go方法)
        html = self.__fetch_content()
        self.__analysis(html)


cpa = Cpa()
cpa.go()
