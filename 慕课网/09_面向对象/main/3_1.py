class Student():
    # 类变量
    sum = 0
    name = '王云'
    age = 0

    def __init__(self, name, age):
          # 实例变量(通过self.变量名形成)
        self.name = name+"xx"
        self.age = age + 1
        # print(name)
        # print(self.name)
        # print(self.age)


student1 = Student('kayla', 18)
print(student1.name)
print(Student.name)
# print(student1.age)


# __dict__可以查看当前所有变量
# print(student1.__dict__)
# print(Student.__dict__)
