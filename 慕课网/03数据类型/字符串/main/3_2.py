# 三引号换行 \n
def aa():
    a = '''
        hellow world
        hellow world
        hellow world'''
    a1 = '''hellow world\nhellow world\nhellow world'''

    print('a....', a)
    print('a1....', a1)


# aa()


# 单引号 换行


def bb():

    b = 'hellow world\hellow world\hellow world'

    print('b....', b)


bb()


# 双引号 换行 \n

def cc():

    c = "hellow world\nhellow world\nhellow world "

    print('c....', c)


# cc()


# 原始字符  r
print(r'hello \n world')
print('hello \\n world')
