class Student():
    # 在类的内部可以定义变量
    name = ''
    age = 0

    # 也可以定义函数
    def print_file(self):
        # print(name)  # 打印会报错,不接受参数
        # print(str(age))
        print('name:' + self.name)
        print('age:'+str(self.age))


# 如何调用类中的函数 ?   通过实例化(类名加括号)
student = Student()

# # 如何调用类下面的方法?
student.print_file()
