# 将普通对象,变为迭代器
import copy


class Book:
    pass


class BookCollection:  # 表示一组书,类有可能是需要被遍历的
    def __init__(self):
        self.data = ['<<往事>>', '<<简书>>', '<<回味>>']
        self.cur = 0  # 每调用一次next,cur变量就加一
        pass

    def __iter__(self):
        # 只需返回自身就可以了
        return self

    def __next__(self):
     # 如果超出整个列表的长度,就抛出异常StopAsyncIteration
        if self.cur >= len(self.data):
            # for in循环在调用next时,接到异常,就知道列表的遍历已经完成了,停止调用
            raise StopAsyncIteration()
     # 当for in循环第一次调用next时,只需要直接取出self.data下面对应的索引序号的数据.并且把r得到的书名返回就可以了
        r = self.data[self.cur]
    # 序号加一,才会取到第二本书名
        self.cur += 1
        return r


books = BookCollection()
for book in books:  # 用for in 类遍历
    print(book)

# 错误:不可以多次遍历for in循环
# for book in books:
#     print(book)

# 两次遍历的方法:copy
books_copy = copy.copy(books)

# 也可以调用next方法,逐个从迭代器里取出相应的书籍名称
# print(next(books))
# print(next(books))
# print(next(books))
