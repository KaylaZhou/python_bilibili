from s_2 import Human


class Student(Human):   # 子类 (也有自己一些变量)
    # sum = 0

    def __init__(self, school):
        self.school = school
        # self.__score = 0
        # self.__class__.sum += 1

    def do_homework(self):
        print('I like python')


a1 = Student('石敢当', 18)
print(a1.sum)
print(Student.sum)
print(a1.name)
print(a1.age)
a1.get_name()


# 问题:s_1模块中的类,如何继承s_2模块中people这个类?
# 首先将s_2中的类导入到s_1的模块中
# 构造函数的继承性?(    a1 = Student() TypeError: __init__() missing 2 required positional arguments: 'name' and 'age')
