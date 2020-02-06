# 静态方法


class Student():
    sum1 = 2
    sum2 = 1

    def plus_sum1(self, num, sum1):
        self.sum1 += 1
        print(self.sum1)

    @classmethod
    def plus_sum2(cls):
        cls.sum2 += 1
        print(cls.sum2)

    @staticmethod
    def add(x):
        print('这是静态方法')
        print(Student.sum1)  # 静态方法也可以访问类变量


def xxx1():

    a1 = Student()
    a1.plus_sum1('当前人数为:', 1)
    a1.plus_sum2()
    a1.add(0)
    Student. add(0)


# xxx1()


# 静态方法和类方法,如何访问实例变量?

class Student():
    sum1 = 2
    sum2 = 1

    def plus_sum1(self, num, sum1):
        self.sum1 = sum1
        print(self.sum1)

    @classmethod
    def plus_sum2(cls):
        cls.sum2 += 1
        # print(cls.sum2)
        print(self.sum1)

    @staticmethod
    def add(x):
        # print('这是静态方法')
        print(self.sum1)


b1 = Student()
b1.plus_sum2()
b1.add(1)
Student.plus_sum2()
Student.add(1)

# 静态方法和类方法,无法访问实例变量
