class Animals:
    def __init__(self,name):
        self.name=name
    def show_info(self):
        return "动物的名字:{0}".format(self.name)
    def move(self):
        print("动一动……")
    def run(self):
        print("什么在跑？原来是{0}".format(self.name))

class Dog(Animals):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def run(self):
        print("汪汪……我{0}在跑".format(self.name))
class Cat(Animals):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def run(self):
        print("喵……我{0}在跑".format(self.name))
cat=Cat("TOM",2)
cat.move()
print(cat.show_info())
print(cat.age)
class Doat(Dog,Cat):
    def __init__(self,name,age,weight):
        self.name=name
        self.weight=weight
        self.age=age
    def show(self):
        print("I'm a doat,age:{0},name:{1},weight:{2}".format(self.age,self.name,self.weight))
da=Doat("Jason",114514,123)
da.show()
da.run()
an1=Dog("Jason",114514)
an2=Cat("Jasons",1919)
an1.run()
an2.run()