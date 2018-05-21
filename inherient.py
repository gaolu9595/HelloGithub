#coding = UTF-8

class SchoolMember:
    '''表示学校里各种角色的成员'''
    def __init__(self,name,age):
        #所有成员都共有name和age两个字段
        self.name = name
        self.age = age
        print("My name is {0}, and I'm {1} years old...".format(self.name,self.age))

class Student(SchoolMember):  #student类继承于schoolMember类
    '''表示学生'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print("Student {0} got {1}...".format(self.name,self.marks))


class Teacher(SchoolMember):
    '''表示教师'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print("Teacher {0} got {1} dollars per month...".format(self.name,self.salary))


t = Teacher("Mrs.Shrividya",40,3000)
print()
s = Student("Swaroop",20,88)

