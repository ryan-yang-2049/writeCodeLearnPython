# -*- coding: utf-8 -*-
"""
__title__ = '02 属性查找与绑定方法.py'
__author__ = 'ryan'
__mtime__ = '2018/3/18'
"""

country = 'china'

class UserInfo(object):

	address = 'SH'
	def __init__(self,name,sex,age):
		self.name = name
		self.sex = sex
		self.age = age

	def learn(self,country):
		print(" %s  studying in %s"%(self.name,country))


	def eat(self):
		print("%s is sleeping"%(self.name))

user1 = UserInfo('ryan','male',18)
user2 = UserInfo('cherry','female',16)
user3 = UserInfo('curry','male',20)

# 1.查看对象的私有特征
print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

# 2.查看类中的数据属性
# 结果得出，类中的数据属性的 memory ID 都是一样的。
print(UserInfo.address,id(UserInfo.address))
print(user1.address,id(user1.address))
print(user2.address,id(user2.address))
print(user3.address,id(user3.address))

# 3.查看类中的函数属性
# 类中的函数属性:是绑定给对象使用的，绑定到不同的对象是不同的绑定方法，对象调用绑定方式时，会把对象本身当作第一个传入，传给self
print(user1.learn)
user1.learn(country)

print(user2.learn)

# 结果： <bound method UserInfo.learn of <__main__.UserInfo object at 0x10b75bdd8>>
# 结论： bound method 绑定方法。相当于不同对象调用一种功能，但是各自执行不同的方法。类中定义的函数，是绑定给对象使用的。那个对象在调用，那就是那个对象在使用这个功能。

# 4.对象属性的查找顺序
# 查找顺序：先从自己的名称空间里面找自己的属性，然后在从类里面找属性(类还包括父类等)，类里面没有直接报错。

user1.country = 'USA'
UserInfo.country = 'china'

print(UserInfo.__dict__)
print(user1.__dict__)













