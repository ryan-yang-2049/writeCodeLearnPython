# -*- coding: utf-8 -*-

# __title__ = '07 python抽象类.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.19'

import abc

class Animal(metaclass=abc.ABCMeta):
    all_type = 'animal'

    @abc.abstractclassmethod
    def run(self):
        pass

    @abc.abstractclassmethod
    def eat(self):
        pass


class People(Animal):

    def run(self):
        print("people is running")

    def eat(self):
        print("people is eating")

    def sleep(self):
        print("people is sleeping")



class Pig(Animal):
    def run(self):
        print("pig is running")

    def eat(self):
        print("pig is eatting")

class Dog(Animal):
    def run(self):
        print('dog is walking')

    def eat(self):
        print('dog is eating')


person = People()
pig = Pig()
dog = Dog()


person.run()
pig.run()
dog.run()

print(person.all_type)


"""
结论：
    1.根据结果和对象调用方法可以看出，实例化后的对象，调用的方法都是一样的，这样的好处在于，用户体验较好。
    2.在抽象类Animal，只能被继承，不能被实例化。并且，在抽象类中定义的方法，只定义名字，不实现代码的逻辑程序。并且，在抽象类中定义的方法名，要在继承它的子类中也存在。在子类中去实现该方法的逻辑程序。但是子类里面可以有别的方法。
    3.在抽象类中定义的数据属性，可以在子类中获取到。
抽象类的本质还是类，指的是一组类的相似性，包括数据属性（如all_type）和函数属性（如 run，eat），而接口只强调函数属性的相似性。
"""