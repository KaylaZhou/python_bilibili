class Student():
    name = ''
    age = 0

    def print_file(self):
        print('name:' + self.name)
        print('age:'+str(self.age))


# 通过实例化(类名加括号)调用类中的函数
student1 = Student()   # 用student这个新的模板来创建一个对象(就是实例化)
student2 = Student()    # 这三个对象所表示的意义是一样的,但是再计算机中所表示的意义是不同的.通过打印id可以知道内存地址不同.
student3 = Student()

# 如何在实例化中,让三个对象打印的结果不同?
# print(id(student1))
# print(id(student2))
# print(id(student3))

# 如何调用类下面的方法?
# student.print_file()


# 如何在实例化中,让对象打印的结果不同?
class Student():
    name = ''
    age = 0
# 通过这个固定的特殊函数(构造函数)

    def __init__(self, name, age):
      # 构造函数
      # 初始化对象的特征/属性
        name = name  # 将右边的name这个形参传给左边新的变量name
        age = age
        # print('student')
        # return None
        # return 'student'  # 报错

    def print_file(self):
        print('name:' + self.name)
        print('age:'+str(self.age))


student1 = Student('kayla', 18)  # 用student这个新的模板来创建一个对象(就是实例化)
print(student1.age)  # 打印的结果是类的变量

# a = student1.__init__()
# print(a)
# print(type(a))
