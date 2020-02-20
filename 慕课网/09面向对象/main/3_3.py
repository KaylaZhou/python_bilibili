# 在实例中访问实例变量与类变量


class Student():
    sum = 0
    name = '王云'
    age = 0
    action = "xxx"

    # 实例方法
    def __init__(self, name1, age):
        print('homework')
        # 构造函数,是一个特殊的实例方法
        # print(self)
        self.name = name1+"xx"
        self.age = age + 1
        # print(name1)
        # print(self.name)  # 在实例方法中访问实例变量
        # print(self.age)

      # 实例方法(是和对象实例相关联的.第一个参数需要传入self)
    # def do_homework(self):  # self代表一个实例
        # self.action = "到家了"
        # print('homework')


def class_1():

    xxxxx = Student("", 0)
    # student2 = Student('李显华', 18)
    print(xxxxx.name)
    print(xxxxx.age)


# class_1()

# 在实例中访问类变量
class Student():
    sum1 = 88

    def __init__(self, sum1):
        self.sum1 = sum1+2
        print(self.__class__.sum1)  # self内置的class,这个class代表类
        print(Student.sum1)


a1 = Student(22)
print(a1.sum1)
