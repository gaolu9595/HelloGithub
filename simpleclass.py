#用class关键字来创建类
#类变量和对象变量：前者是各个对象所共享的，一旦有改变，该变动在其他所有实例中都能体现
#后者是每个实例对象都拥有其自己的副本，不是共享的

#coding = UTF-8
class Person:
    '''表示一个带有名字和年龄的人的信息'''

    #pass  #表示一个空的代码块
    population = 0   #population是一个类变量，不论被哪个对象改变，其变动都会永久存在
    #__init__方法：对任何你想要进行操作的目标对象初始化,但是并不
    def __init__(self,name,age=16):
        self.name = name
        self.age = age
        print("(Initializing {}......)".format(self.name))
        Person.population += 1

    def sayhello(self):
        print("Greetings, you can call me {0}, and I am {1} years old!"\
              .format(self.name,self.age))

    def die(self):
        """我挂了"""
        print("{} died......".format(self.name))
        Person.population -= 1
        if Person.population == 0:
            print("Unfortunately! I was the last survived person...")
        else:
            print("Congratulation! There are still {} person alive!".format(Person.population))

    @classmethod
    def how_many(cls):
        '''打印当前人口数量'''
        print("We have {} person alive now!".format(Person.population))

#创建带有初始化字段的实例对象
p1 = Person("Jack",34)
p2 = Person("Rebecca",32)
p3 = Person("Kate")
p4 = Person("Kevin")
p5 = Person("Randall")
for person in [p1,p2,p3,p4,p5]:
    person.sayhello()
    person.die()


Person.how_many()
print(Person.__doc__)

#'r表示内部的字符串默认不转义
print(r"I'm \"OK\"!")
print("I'm \"OK\"!")
print('''
i
am
a
student
'''
)
print(r'''hello,\n
world''')
print("中文测试正常")

#字符串是不可变对象
a = "abc"
print(a.replace("a","A"))
print(a)
b = a.replace("a","A")
print(b)

