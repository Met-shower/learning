# 设计一个 Person 类，属性包括姓名，年龄，性别，
# 再设计一个继承 Person类的Student类，
# 编写新的函数用来设置学生专业，然后生成该类对象并显示信息


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_info(self):
        print(f'学生姓名:{self.name}, 学生年龄:{self.age}, 学生性别:{self.gender}。', end='')


class Student(Person):
    def __init__(self, name, age, gender, profession=' '):
        super().__init__(name, age, gender)
        self.profession = profession
        print(f'学生姓名:{name}, 学生年龄:{age}, 学生性别:{gender}')

    def show_info(self):
        super().show_info()

        if self.profession == ' ':
            print('未输入专业')
        else:
            print(f'学生专业{self.profession}')


    def set_profession(self, profession):
        self.profession = profession
        print(f'已经将学生的专业设置为{self.profession}')


stu1 = Student('李行宇', 18, '男')
stu1.show_info()

stu1.set_profession('engineer')
