class Student():
   # 类变量
    name = ''
    age = 0

    def __init__(self, name, age):
      # 实例变量(通过sele.变量名形成)
        self.name = name
        self.age = age
        print(self.name)
        print(self.age)


student1 = Student('kayla', 18)
# print(self.name)
