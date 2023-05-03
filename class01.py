class Dog():
    #构造方法
    mass=12
    __mas=3#私有变量
    def __init__(self,name,age,sex):
        self.name=name#创建和初始化实例变量name
        self.age=age
        self.sex=sex
    #实例方法
    def run(self):
        print("{}在跑".format(self.name))
    def speak(self,sound):
        print("{0}在叫{1}".format(self.name,sound))
    #装饰器&类方法
    """@classmethod
    def rmas(cls,be):
        return be-cls.mass"""
    def rmas(self,be):
        return be-Dog.mass
    def __fs(self):#访问私有化变量方法
        print(Dog.__mas)
d=Dog("球球",sex="雌性",age=2)
print("我们家的狗狗名字叫{0},{1}岁,{2}".format(d.name,d.age,d.sex))
d.run()
d.speak("aaa")
print("普通狗的质量为{}kg".format(Dog.mass))
print("减肥{}kg".format(d.rmas(13)))
#d.__fs()私有方法不可以访问
d.__mas=999
print("aaaaaaaaa{}".format(d.__mas))# 不可通过外部直接访问私有变量