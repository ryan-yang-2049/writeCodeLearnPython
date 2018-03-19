# -*- coding: utf-8 -*-

# __title__ = '11 绑定方法与非绑定方法.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.19'

'''
在类内部定义的函数，分为两大类：
    一：绑定方法:绑定给谁，就应该由谁来调用，谁来调用就会把调用者当作第一个参数自动传入
        - 绑定到对象的方法：在类内定义的没有被任何装饰器修饰的
        - 绑定到类的方法：在类内定义的被装饰器classmethod修饰的方法
    二：非绑定方法:没有自动传值这么一说了，就类中定义的一个普通工具，对象和类都可以使用
        非绑定方法：不与类或者对象绑定

'''

# class Foo(object):
#
#     def __init__(self,name):
#         self.name = name
#
#
#     def tell(self):             # 绑定给对象的方法
#         print("名字：%s"%self.name)
#
#     @classmethod                # 绑定给类的方法
#     def bound_class(cls):
#         print(cls)
#
#     @staticmethod               # 非绑定方法，类和对象都可以使用（普通函数）
#     def common_method(x,y):
#         print("x+y=",x+y)

# f = Foo('ryan')
#
# print("类的普通函数:",Foo.tell)
#
# print("绑定给对象的方法:",f.tell)
#
# print("绑定给类的方法:",Foo.bound_class)
#
# print("非绑定方法,给类使用:",Foo.common_method)
#
# print("非绑定方法,给使用:",f.common_method)
#
# Foo.common_method(1,2)      # 非绑定方法，该怎么传参就怎么传参
#
# f.common_method(1,3)        # 非绑定方法，该怎么传参就怎么传参



# 绑定方法与非绑定方法的应用

import settings
import hashlib
import time

class People(object):
    def __init__(self,name,age,sex):
        self.id = self.create_id()
        self.name = name
        self.age = age
        self.sex = sex


    def tell_info(self):
        print('Name:%s Age:%s Sex:%s' %(self.name,self.age,self.sex))

    @classmethod
    def from_conf(cls):
        obj = cls(
            settings.name,
            settings.age,
            settings.sex
        )
        return obj

    @staticmethod
    def create_id():
        m = hashlib.md5(str(time.time()).encode('utf-8'))
        return m.hexdigest()


p1 = People('cherry',18,'female')

# tell_Info 是绑定给对象的方法，就应该有对象来调用，自动将对象本身当做第一个参数传入
p1.tell_info()


# 绑定给类，就应该由类来调用，自动将类本身当作第一个参数传入
# 在用户使用时自动去文件里面去调用一些参数，调用参数本身是通过类去调用文件里面的信息，因此，就要使用类的绑定方法。

p2 = People.from_conf()
p2.tell_info()


# 非绑定方法不与类或者对象绑定，谁都可以调用，没有自动传值一说
print(p1.id)
print(p2.id)






