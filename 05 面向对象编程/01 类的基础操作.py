# -*- coding: utf-8 -*-
"""
__title__ = '01 类的基础操作.py'
__author__ = 'ryan'
__mtime__ = '2018/3/18'
"""


class UserInfo(object):

	address = 'SH'

	def __init__(self,name,sex,age):
		self.name = name
		self.sex = sex
		self.age = age


	def learn(self):
		print("is learning")


	def eat(self):
		print("is sleeping")




# 操作1：查看未被实例化时-查看类的名称空间

print(UserInfo.__dict__)

# 操作2:  产生对象，__init__ 实例化的步骤

user1 = UserInfo('ryan','male',18)
print(user1.__dict__)


# 操作3： 查看对象单独的属性
print(user1.name)


# 操作4: 改变对象属性的值

print("未改变对象属性之前:",user1.name)

user1.name = 'cherry'

print("改变对象属性之后:",user1.name)


# 操作5: 删除对象属性

del user1.sex
print(user1.__dict__)

# 操作6：增加对象属性

user1.job = 'IT'
print(user1.__dict__)
















