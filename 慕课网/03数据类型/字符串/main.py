# v = 'abfk'
# new_v = v.upper() # 转换位大写
# print(new_v)
# ABFK


# v = 'ABCD'
# new_v = v.lower() # 转换位小写
# print(new_v)


# 判断字符串是否为数字:  .isdigit
def judge():

    print("""欢迎致电10086
1.话费查询
2.业务办理
3.流量查询""")

    num = input('请选择服务:')
    flag = num.isdigit()
    print(flag)     # 判断用户输入的字符串, 是否可以转换成数字.
    if flag:
        num = int(num)
        print(num)
    else:
        print('请输入数字:')


# judge()


# 去除空白strip/lstrip/rstrip
def num():

    user = input('请输入用户名:')
    new_user1 = user.strip()  # 去除左右两边的空白
    new_user2 = user.lstrip()  # 去除左边的空白
    new_user3 = user.rstrip()  # 去除左边的空白
    print('--->', new_user1, '<---')  # ---> kayla <---
    print('--->', new_user2, '<---')   # 输出结果为:---> kayla       <---
    print('-->', new_user3, '<--')  # 输出结果为: -->    mei <--


# num()


# 字符串替换 .replace()
def use():
    hint = input('请说话:')
    # print(hint)
    new_hint = hint.replace('喜欢', '**', 2)  # 将喜欢替换为**,数字代表,要替换这句话中几个喜欢
    print(new_hint)


# use()


# 切割 split
def num():

    content = '罗小黑战记,是一部很好看的动漫,大家都喜欢看'
    new_content = content.split(',', 1)  # 从左到右,切有逗号的每句话.1表示第个逗号
    print(new_content)  # 输出:['罗小黑战记', '是一部很好看的动漫', '大家都喜欢看']


# num()

def num_2():

    content = '罗小黑战记,是一部很好看的动漫,大家都喜欢看'
    new1_content = content.rsplit(',', 1)  # 从右到左,切割第一个有逗号的话子
    print(new1_content)  # 输出:['罗小黑战记', '是一部很好看的动漫', '大家都喜欢看']


# num_2()


# 切片 ,练习: 取最后两个字符
def chop():
 # 方法一
    use = input("请输入:")
    v = use[-2:]
    print(v)
 # 方法二
    total_len = len(use)
    v = use[total_len-2:total_len]
    print(v)


# chop()


# startwith,判断是否以...开头
def nn():
    name = "kayla"
    v = name.startswith('a')
    print(v)


# nn()


# encode,转换编码

def mm():

    name = '王明'
    v1 = name.encode('gbk')
    print()


# mm()


# join 循环每个元素,并在元素和元素之间加入连接符
def vv():

    name = 'kayla'
    result = '_'.join(name)
    print(result)  # k_a_y_l_a


# vv()


# use = '9990'
# nn = use.isdigit()
# print(nn)


# name = "kayla"
# v = name[::-1]    # alyak
# v = name[1::2]    # al
# v = name[-2::-3]  # lk
# print(v)


def splitStr(p):
    s = p

    s1 = ""
    for v in s:
        if v != " ":
            s1 += v

    return s1


def inputSplt():
    content = input('请输入:')
    new_content = content.strip()
    bbb = splitStr(new_content)
    return bbb


vvv = inputSplt()
# print(vvv)
