# -*- coding: utf-8 -*-

# __title__ = '04 继承.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.19'

"""
继承就是解决类与类之间的代码冗余问题，也就是代码重复的问题。
继承指的是类与类之间的关系，是表达一种 “什么是什么的关系”。
继承是一种创建新类的方式，在python中，新建的类可以继承一个或多个父类，父类又可以称为基类或超类，新建的类称为派生类或子类

派生：当实例调用某个方法时，如果子类有就调用子类里面的，如果没有，就调用父类里面。
"""


class Hero(object):

    def __init__(self,nickname,atk,life_value):
        self.nickname = nickname
        self.atk = atk
        self.life_value = life_value


    def move_forward(self):
        print("%s move forward"%self.nickname)


    def move_backward(self):
        print("%s move backward"%self.nickname)

    def attack(self,enemy):
        enemy.life_value -= self.atk

    def info(self):
        print("from Hero.info")
        self.move_forward()

class Garen(Hero):
    def move_forward(self):
        print("from Garen.move_forward")
        print("g1 move forward")


class Riven(Hero):
    pass


g1= Garen('草丛伦',100,500)
r1 = Riven("亚瑟",70,700)

# print(r1.life_value)
# g1.attack(r1)
# print(r1.life_value)
print(g1.__dict__)
g1.info()
print(Garen.__bases__)
print(Garen.mro())  # 继承的实现原理