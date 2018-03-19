# -*- coding: utf-8 -*-

# __title__ = '02 __init__方法.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.19'


'''
__init__(self[, ...])

__init__ 构造器，当一个实例被创建的时候初始化的方法.但是它并不是实例化调用的第一个方法，__new__才是实例化对象调用的第一个方法，它只取下 cls参数，并把其他参数传给 __init__
'''


# class Foo(object):
#
#     def __init__(self):
#         print(" auto execute")
#
#
# print(Foo())




class Person(object):
    """Silly Person"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '<Person: %s(%s)>' % (self.name, self.age)

if __name__ == '__main__':
    p1 = Person('ryan', 24)
    print(p1)








