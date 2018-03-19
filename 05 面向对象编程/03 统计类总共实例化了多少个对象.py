# -*- coding: utf-8 -*-
"""
__title__ = '03 统计类总共实例化了多少个对象.py'
__author__ = 'ryan'
__mtime__ = '2018/3/18'
"""
country = 'china'

class UserInfo(object):

	address = 'SH'
	count = 0
	def __init__(self,name,sex,age):
		self.name = name
		self.sex = sex
		self.age = age
		UserInfo.count += 1

	def learn(self,country):
		print(" %s  studying in %s"%(self.name,country))


	def eat(self):
		print("%s is sleeping"%(self.name))


print("未绑定实例之前：",UserInfo.count)
user1 = UserInfo('ryan','male',18)
user2 = UserInfo('cherry','female',16)
user3 = UserInfo('curry','male',20)

print("绑定实例之后：",UserInfo.count)

"""
这题的意义在于了解 __init__ 方法。
每触发一次 __init__ 方法，就相当于实例化出了一个对象。就相当于一个类创建了一个对象，如果，count 是自己的属性，那么别的对象就感受不到，那就会形成 count =1 ，因此，就要把count 设置为类的属性，那样，在创建一个对象的时候，对象本身的count 就会自增一次。最后，在调用 UserInfo.count 的时候，就可以查看到创建了多少次对象
"""


