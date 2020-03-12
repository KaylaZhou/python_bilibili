'''
用python中的字典映射来代替switch
也可以用函数,作为字典中的value值

'''
day = 8


def get_studay():
    return 'Sunday'


def get_Monday():
    return 'Monday'


def get_Tuesday():
    return 'Tuesday'


def get_default():
    return 'Unknown'


switcher = {
    0: get_studay,
    1: get_Monday,
    2: get_Tuesday
}


day_name = switcher.get(day, get_default)()  # get返回的是方法,直接加()可以执行方法
print(day_name)
