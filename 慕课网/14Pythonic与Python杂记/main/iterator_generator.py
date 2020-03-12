#
class Book:
    pass


class BookCollection:  # 表示一组书,类有可能是需要被遍历的
    def __init__(self):
        self.data = ['<<往事>>', '<<简书>>', '<<回味>>']
        self.cur = 0  # 没调用一次next,cur变量就加一
        pass

    def __iter__(self):
        pass

    def __next__(self):
     # 如果超出整个列表的长度,就抛出异常StopAsyncIteration
        if self.cur >= len(self.data):
            raise StopAsyncIteration()   # for in循环在调用next时,接到异常,就知道列表的遍历已经完成了,停止调用

     # 当for in循环第一次调用next时,只需要直接取出self.data下面对应的索引序号的数据.并且把r得到的书名返回就可以了
        r = self.data[self.cur]
        self.cur += 1   # 序号加一,才会取到第二本书名
        return r


books = BookCollection()
for book in books:
    print(book)
