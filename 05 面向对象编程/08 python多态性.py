# -*- coding: utf-8 -*-

# __title__ = '08 python多态性.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.19'


import abc
class Animal(metaclass=abc.ABCMeta): #同一类事物:动物
    @abc.abstractmethod
    def talk(self):
        pass

class People(Animal): #动物的形态之一:人
    def talk(self):
        print('say hello')

class Dog(Animal): #动物的形态之二:狗
    def talk(self):
        print('say wangwang')

class Pig(Animal): #动物的形态之三:猪
    def talk(self):
        print('say aoao')


peo1=People()
dog1=Dog()
pig1=Pig()

# 动态多态性
peo1.talk()
dog1.talk()
pig1.talk()

#结论：不考虑对象的类型，只要是继承了某个类的方法，就可以按照类的标准进行使用，这个就是动态多态性。


# 静态多态性

def func(animal):
    animal.talk()

func(peo1)
func(dog1)
func(pig1)

# 结论：不用考虑对象具体的类型，直接调用一个方法就行。


