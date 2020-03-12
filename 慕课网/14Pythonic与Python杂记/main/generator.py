# 生成器
# print 0~10000

n = [i for i in range(0, 10001)]
# n = (i for i in range(0, 10001))
# print(n)
# for i in n:
#     print(i)  #消耗内存


def gen(max):
    n = 0
    while n <= max:
        # print(n)
        n += 1
        yield n  # 接着上次返回的结果继续返回结果


g = gen(10000)
for i in g:
    # print(i)
    # print(next(g))
    # print(next(g))
    # print(next(g))
