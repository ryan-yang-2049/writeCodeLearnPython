# -*- coding: utf-8 -*-

# __title__ = '07 __setattr__,__delattr__,__getattr__方法.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.20'

'''
　　__getattr__ 定义当用户试图访问一个不存在属性的时候的行为

　　__setattr__ 定义当一个属性被设置的时候的行为

    __delattr__ 定义当一个属性被删除的时候的行为


'''


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._registry = {
            'name': name,
            'age': age
        }

    def __getattr__(self, item):
        print("don't have the attribute ", item)
        return False

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattribute__(self, item):
        # 注意此处不要用 self.__dict__[item]
        # 因为self.__dict__依然会被__getattribute__拦截 这样就会陷入循环
        return object.__getattribute__(self, item)


a = Person('p1', 20)
print(a.__dict__)
print(a.hh)  # 这里会打印 don't have the attribute hh 以及 False
a.hh = 'fdf'  # 这里设置该属性值为'fdf'
print(a.hh)  # 这里将打印出 fdf