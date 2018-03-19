# -*- coding: utf-8 -*-

# __title__ = '10 property用法.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.19'

'''
property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值
property 可以封装一些通过计算后，在访问的数据类型等封装在函数里面，通过 “对象.属性” 访问。

property是一个装饰器，它是让一个方法相当于一个属性来使用。并且他是一组算法（程序）的返回，并不会传入一些参数进去。但是这个被property装饰后的方法不可以像数据属性一样去赋值。

为什么要用property：将一个类的函数定义成特性以后，对象再去使用的时候obj.name,根本无法察觉自己的name是执行了一个函数然后计算出来的，这种特性的使用方式遵循了统一访问的原则

'''
# 计算BMI指数 ：体质指数（BMI）=体重（kg）÷身高^2（m）

class Person(object):

    def __init__(self,name,weight,height):
        self.name = name
        self.weight = weight
        self.height = height


    @property
    def bmi(self):
        return  self.weight/(self.height**2)


# p1=Person('cherry',52,1.56)
# print(p1.bmi)


# property 的扩展


class People(object):

    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return  self.__name

    @name.setter
    def name(self,val):
        if not isinstance(val,str):
            print("名字必须是字符串类型")
            return
        self.__name =val

    @name.deleter
    def name(self):
        print("不允许删除")



p1 = People('ryan')

print("1)打印name：",p1.name)      # property 可以让对象.方法  来进行调用，相当于数据属性
p1.name = 'cherry'
print("2)打印name：",p1.name)      # 1)打印name： cherry

p1.name = 123           # 名字必须是字符串类型


del p1.name             # 不允许删除

"""
结论：后面的name.setter 或者 name.deleter 都是现有 name被property装饰了以后才会有。如果name改名为 A，那setter 就要改写成为 A.setter。该例子其实和上面例子的解释对应，property是给一个把一个方法（函数）作为属性去调用，但是在属性调用的过程中，又不可以传入参数，因此，才会有后面的 setter and delete 。
"""






























