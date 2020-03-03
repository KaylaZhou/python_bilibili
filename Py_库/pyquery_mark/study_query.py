from pyquery import PyQuery
import os
#  1. 爬取网闸内容并解析成utf-8
#  2. 将utf-8的字符串保存为utf-8格式的文件
#  3 .读取文件并解析

# 读文件


def readTxt(url):
    FILE_OBJECT = open(url, 'r', encoding='UTF-8')
    return FILE_OBJECT.read()


txtContent = readTxt("./jianshu.html")
# 读文件 -- end


# 解析


html = '''
<div>
    <p>test 1</p>
    <p>test 2</p>
    <div>test 5</div>
    <a>test 8</a>
</div>
'''
# p = PyQuery(html)
p = PyQuery(txtContent)


titles = p('#list-container').find(".title")

titleArr = "[]"
for a in titles:
    pyquery_a = PyQuery(a)
    print(pyquery_a.html())

# 解析 - end
