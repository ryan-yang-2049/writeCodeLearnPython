# -*- coding: utf-8 -*-

# __title__ = '05 __str__方法.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.20'


# 如要把一个类的实例变成 str ，就需要实现特殊方法 __str__()；

class People(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return  '<name:%s,age:%s>' %(self.name,self.age)


p1 = People('ryan',18)

print(p1)       #<name:ryan,age:18>







