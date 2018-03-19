# -*- coding: utf-8 -*-

# __title__ = '05 在子类中重用父类的方法(super()).py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.19'

#方式一：直接引用

class Hero1:
    def __init__(self,nickname,life_value,aggresivity):
        self.nickname=nickname
        self.life_value=life_value
        self.aggresivity=aggresivity
    def attack(self,enemy):
        enemy.life_value-=self.aggresivity

class Garen1(Hero1):
    camp='Demacia'

    def __init__(self,nickname,life_value,aggresivity,weapon):
        Hero1.__init__(self,nickname,life_value,aggresivity)         #初始化的时候，在调用父类的 __init__ 方法。
        self.weapon=weapon


    def attack(self,enemy):
        Hero1.attack(self,enemy) #指名道姓，不依赖继承，相当于用了另外一个类的方法。
        print('from Garen Class')

class Riven1(Hero1):
    camp='Noxus'

# g=Garen('草丛伦',100,30)
# r=Riven('锐雯雯',80,50)
#
# print(r.life_value)
# g.attack(r)
# print(r.life_value)
# g=Garen('草丛伦',100,30,'金箍棒')
# print(g.__dict__)

# 结论：上面两种重用父类的方法，都不依赖于继承的原理。是一种类似于导入的方法，相当于直接指定某个类的某方法Hero.__init__(self,nickname,life_value,aggresivity) 这里就相当于上面子类里面注释掉的self.属性的内容。因此，应该有更好的方法去重用父类的方法。



class Hero:
    def __init__(self,nickname,life_value,aggresivity):
        self.nickname=nickname
        self.life_value=life_value
        self.aggresivity=aggresivity
    def attack(self,enemy):
        enemy.life_value-=self.aggresivity

class Garen(Hero):
    camp='Demacia'

    def __init__(self,nickname,life_value,aggresivity,weapon):
        # super(Garen,self).__init__(nickname,life_value,aggresivity)
        super().__init__(nickname,life_value,aggresivity)   #super qu mro中找
        self.weapon=weapon

    def attack(self,enemy):
        super().attack(enemy)  #实际上是这样用的 super(Garen,self).attack(enemy)
        print('from Garen Class')
class Riven(Hero):
    camp='Noxus'


g=Garen('草丛伦',200,50,'金箍棒')
print(Garen.__mro__)
print(g.__dict__)

r=Riven('锐雯雯',80,50)
g.attack(r)
print(r.life_value)


# super() 的查找顺序

class A(object):
    def f1(self):
        print('from A')
        super().f1()

class B(object):
    def f1(self):
        print('from B')

class C(A,B):
    pass

print(C.mro())  # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

c=C()
c.f1()


# 结论：super 的查找顺序是按照 __mro__ 列表往后找，就像上例一样，在A中super().f1() 此时，虽然 A没有继承B，但是，在super 这个方式，是由c对象触发的，因此，super的查找方法，会按照，c对象的 __mro__ 列表往后找。因此，就会打印 from B;
# A 和 B 无关乎于继承，只是在C中继承了A,B 导致了后面super的查找顺序。该例子一般是特例。
