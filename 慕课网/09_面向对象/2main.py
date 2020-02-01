class Student():
    name = ''
    age = 0

    def print_file(self):
        print('name:' + self.name)
        print('age:'+str(self.age))


# 通过实例化(类名加括号)调用类中的函数
student1 = Student()
student2 = Student()
student3 = Student()

print(id(student1))
print(id(student2))
print(id(student3))


# 如何调用类下面的方法?
# student.print_file()
