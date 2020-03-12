'''
用python中的字典映射来代替switch
1.首先定义一个空的字典,switcher
2.用字典的key,代替1_switch的case后面的0 ,1 ,2
3.定义day_name,用字典的映射代替switch,并将变量day传入

得到的结果:
当day=0时,通过字典的映射,把'Sunday'赋值给day_name,

解决day取值之外的情况?
1.换一种字典的访问方式,用内置的get方法,get(第一个参数是key 为变量day,第二个参数将指定当day所对应的key不存在的时候方法调用的结果)
get方法具有容错性

'''
day = 4
switcher = {
    # 字典可以是字符串,也可以是数字
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday'

}
# day_name = switcher[day]
day_name = switcher.get(day, 'Unknown')
print(day_name)
