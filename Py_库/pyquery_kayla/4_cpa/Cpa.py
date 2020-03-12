import re
from urllib import request
# 断点调试


class Cpa():
    url = 'https://shcpa.org.cn/'
    root_patter = '<ul class="hlist notice">([\s\S]*?)</ul>'  # ()可以去掉定界的内容
    name_patter = '<li>[\s\S]*?</li>'

    def __fetch_content(self):
        r = request.urlopen(Cpa.url)  # 通过request.urlopen方法,接受url,url就是要抓取网页的地址
        html = r.read()  # 通过read方法读取html
        html = str(html, encoding='utf-8')  # 将html字节码转换为字符串

        return html
        # print(html)

# 分析文本
    def __analysis(self, html):
        root_html = re.findall(cpa.root_patter, html)

        anchors = []
        for html in root_html:  # 用for便利html
            name = re.findall(Cpa.name_patter, html)
            # number = re.findall(Cpa.number_pattern, heml)
            anchor = {'name': name}
            # anchor = {'name': number}
            anchors.append(anchor)
        # print(anchors)
        return anchors

# /分析文本

# 精炼
    def __refine(self, anchors):  # 通过refine将数据精炼(去掉空格,换行符等,将列表转换为单一的值)
        def l(anchors): return {
            'name': anchor['name'][0].strip(),
            # 'number': anchor['number'][0]
        }
        return map(1, anchors)

# /精炼

# 排序
    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    def __sort_seed(self, anchor):
        r = re.findall('[1-9]\d*.?\d*', anchor['number'])
        number = float(r[0])
        # print(number)
        if '万' in an['number']:
            number *= 10000
        return number
# /排序

# 展现数据
    def __show(self, anchors):
        for rank in range(0, len(anchors):
            print('rank' + str(rank + 1)
            + ':' + anchors[rank]['name']
            + '   '+anchors[rank]['number'])

            # print(anchor['name']+'----'+anchor['number'])

        # /展现数据

    def go(self):  # 入口方法(也是总控方法,所有的函数调用最后都会汇集到go方法)
        html=self.__fetch_content()    # 取内容
        anchors=self.__analysis(html)  # 分析内容
        anchors=list(self.__refine(anchors))  # 精炼内容
        anchors=self.__sort(anchors)    # 业务处理(sort函数 排序)
        self.__show(anchors)      # 展示方法


cpa=Cpa()
cpa.go()
