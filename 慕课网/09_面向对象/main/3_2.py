# self


class Student():
    sum = 0
    name = '王云'
    age = 0

    # 实例方法
    def __init__(self, name, age):
          # this
        self.name = name+"xx"
        self.age = age + 1
        # print(name)
        # print(self.name)
        # print(self.age)

      # 实例方法(是和对象实例相关联的.第一个参数需要传入self)
    def do_homework(self):  # self代表一个实例
        print('homework')


student1 = Student('kayla', 18)
student2 = Student('李显华', 18)
# student1.__init__('kk', 88)

student1.do_homework()
student2.do_homework()

print(student1.name)
# print(Student.name)
