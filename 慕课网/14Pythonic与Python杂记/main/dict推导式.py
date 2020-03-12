# 字典推导式

students = {
    '喜小乐': 18,
    '石敢当': 20,
    '王小五': 15
}

# 调用字典的.items()方法,字典student才能被遍历
# b = [key for key, value in students.items()]  # 对字典来说,形参是key和value,中间用逗号隔开

# 颠倒 key:value
# b = {value: key for key, value in students.items()}

b = (key for key, value in students.items())
# 元组无法打印,需要对generator做遍历.因为元组是不可变的
for x in b:
    print(x)
