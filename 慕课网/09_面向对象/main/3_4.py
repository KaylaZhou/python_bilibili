# 类方法


class Student():
    sum = 0

  # 实例方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.sum += 1
        # self.sum += 1

        print('当前人数为:' + str(self.sum))

  # 实例方法(是和对象实例相关联的.第一个参数需要传入self)
    def do_homework(self):  # self代表一个实例
        print('homework')

  # 类方法:用来操作和类相关的变量
    @classmethod
    def plus_sum(cls):  # cls也可以用self
        cls.sum += 1
        print(cls.sum)


def xx_1():

    b1 = Student('你好', 2)
    Student.plus_sum()  # 调用类方法
    # b1.plus_sum()  # 也可以用对象调用类方法(一般不推荐,其他语言没有)
    b2 = Student('我', 2)
    Student.plus_sum()
    b3 = Student('他', 2)
    Student.plus_sum()


# print(b1.sum)
# xx_1()


class Student():
    sum = 1

    @classmethod
    def plus_sum(cls):  # cls也可以用self
        cls.sum += 1
        print(cls.sum)


a1 = Student()
a1.plus_sum()
Student.plus_sum()
