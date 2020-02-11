class Human():  # 父类
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)

    def do_homework(self):
        print('这是一个父类方法')
