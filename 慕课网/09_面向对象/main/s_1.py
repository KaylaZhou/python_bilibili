from s_2 import Human


class Student(Human):   # 子类 (也有自己一些变量)
    # sum = 0   #子类可以继承父类的类变量

    def __init__(self, school, name, age):
        self.school = school
        Human.__init__(self, name, age)
        # 在子类里把name和age传给父类(用类调用实例方法,python中允许)
        super(Student, self).__init__(name, age)
        # self.__score = 0
        # self.__class__.sum += 1

    def do_homework(self):
        super(Student, self).do_homework()  # 不仅可以调用构造函数,也可以调用普通的实例方法
        print('I like python')


a1 = Student('人名路小学', '石敢当', 18)
a1.do_homework()  # 子类方法和父类方法同名时,python优先调用子类方法
# print(a1.sum)
# print(Student.sum)
# print(a1.name)
# print(a1.age)
# a1.get_name()  # 访问父类实例方法
# a1.do_homework()
# Student.do_homework('')
'''
问题:s_1模块中的类,如何继承s_2模块中people这个类?
首先将s_2中的类导入到s_1的模块中

 '''
#  构造函数的继承性?(    a1 = Student() TypeError: __init__() missing 2 required positional arguments: 'name' and 'age')
