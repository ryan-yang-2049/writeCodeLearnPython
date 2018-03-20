# -*- coding: utf-8 -*-

# __title__ = '09 __get__,__set__,__delete__方法.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.20'

'''
 描述符是什么:描述符本质就是一个新式类,在这个新式类中,至少实现了__get__(),__set__(),__delete__()中的一个,这也被称为描述符协议
__get__():调用一个属性时,触发
__set__():为一个属性赋值时,触发
__delete__():采用del删除属性时,触发

描述符是干什么的:描述符的作用是用来代理另外一个类的属性的(必须把描述符定义成这个类的类属性，不能定义到构造函数中)

'''

#描述符Str
class Str:
    def __get__(self, instance, owner):
        print('Str调用')
    def __set__(self, instance, value):
        print('Str设置...')
    def __delete__(self, instance):
        print('Str删除...')

#描述符Int
class Int:
    def __get__(self, instance, owner):
        print('Int调用')
    def __set__(self, instance, value):
        print('Int设置...')
    def __delete__(self, instance):
        print('Int删除...')

class People:
    name=Str()
    age=Int()
    def __init__(self,name,age): #name被Str类代理,age被Int类代理,
        self.name=name
        self.age=age

#何地？：定义成另外一个类的类属性
#何时？：且看下列演示
p1=People('ryan',18)    # 调用描述符的 __set__

#描述符Str的使用
# p1.name               # 调用描述符的 __get__
# p1.name='cherry'        # 调用描述符的 __set__
# del p1.name             # 调用Str 描述符的 __delete__

# #描述符Int的使用
# p1.age
# p1.age=18
# del p1.age
#
# #我们来瞅瞅到底发生了什么
print(p1.__dict__)
print(People.__dict__)
#
# #补充
print(type(p1) == People) #type(obj)其实是查看obj是由哪个类实例化来的
print(type(p1).__dict__ == People.__dict__)



