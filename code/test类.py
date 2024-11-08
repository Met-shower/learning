class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"姓名: {self.name}, 年龄: {self.age}, 性别: {self.gender}")


class Student(Person):
    def __init__(self, name, age, gender, major=None):
        super().__init__(name, age, gender)  # 调用父类的构造函数
        self.major = major  # 初始化学生专业

    def set_major(self, major):
        self.major = major  # 设置学生专业

    def display_info(self):
        super().display_info()  # 调用父类的display_info方法显示基本信息
        if self.major:
            print(f"专业: {self.major}")
        else:
            print("专业: 未设置")

        # 创建Student类的实例并设置信息


student1 = Student("张三", 20, "男", "计算机科学与技术")
student1.display_info()  # 显示学生信息

# 创建一个未设置专业的学生实例
student2 = Student("李四", 21, "女")
student2.set_major("软件工程")  # 设置学生专业
student2.display_info()  # 显示学生信息