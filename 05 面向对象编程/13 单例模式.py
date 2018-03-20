# -*- coding: utf-8 -*-

# __title__ = '13 单例模式.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.19'


# 单例模式,对象内部特征一样用单列模式
# 单例模式就是让，参数一样，调用方式一样的不同对象，在创建时不要新申请内存空间

# class MySQL(object):
#
#
#     __instance = None
#     def __init__(self):
#         self.host = '127.0.0.1'
#         self.port = '3306'
#         print(self.__instance)
#
#     @classmethod
#     def singleton(cls):
#         if not cls.__instance:
#             obj = cls()
#             return cls.__instance
#
#         return cls.__instance
#
#     def conn(self):
#         print('conn')
#
#     def execute(self):
#         print('execute')
#
# obj1 = MySQL.singleton()
# obj2 = MySQL.singleton()
# obj3 = MySQL.singleton()
# print("obj1的内存地址",id(obj1))
# print("obj2的内存地址",id(obj2))
# print("obj3的内存地址",id(obj3))


# 基于元类实现MySQL 单例模式
#
class Mymeta(type):
	def __init__(self, class_name, class_bases, class_dic):
		if not class_name.istitle():
			raise TypeError('类名必须大写')
		if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
			raise TypeError('注释不能为空')
		super(Mymeta, self).__init__(class_name, class_bases, class_dic)
		self.__instance = None

	def __call__(self, *args, **kwargs):
		if not self.__instance:
			obj = object.__new__(self)
			self.__init__(obj)
			self.__instance = obj
		return self.__instance


class Mysql(object, metaclass=Mymeta):
	'''
	MySQL 连接
	'''

	def __init__(self):
		self.host = '127.0.0.1'
		self.port = '3306'

	def conn(self):
		print('conn')

	def execute(self):
		print('execute')


obj1 = Mysql()
obj2 = Mysql()
obj3 = Mysql()
print("obj1的内存地址",id(obj1))
print("obj2的内存地址",id(obj2))
print("obj3的内存地址",id(obj3))


# class Mymeta(type):
# 	def __init__(self, name, bases, dic):  # 定义类Mysql时就触发
# 		self.__instance = None
# 		super().__init__(name, bases, dic)
#
# 	def __call__(self, *args, **kwargs):  # Mysql(...)时触发
#
# 		if not self.__instance:
# 			self.__instance = object.__new__(self)  # 产生对象
# 			self.__init__(self.__instance, *args, **kwargs)  # 初始化对象
# 			# 上述两步可以合成下面一步
# 			# self.__instance=super().__call__(*args,**kwargs)
#
# 		return self.__instance
#
#
# class Mysql(metaclass=Mymeta):
# 	def __init__(self, host='127.0.0.1', port='3306'):
# 		self.host = host
# 		self.port = port
#
#
# obj1 = Mysql()
# obj2 = Mysql()
#
# print(obj1 is obj2)


# import time
# import threading
# class Singleton(object):
#     _instance_lock = threading.Lock()
#
#     def __init__(self):
#         time.sleep(1)
#
#     @classmethod
#     def instance(cls, *args, **kwargs):
#         if not hasattr(Singleton, "_instance"):
#             with Singleton._instance_lock:
#                 if not hasattr(Singleton, "_instance"):
#                     Singleton._instance = Singleton(*args, **kwargs)
#         return Singleton._instance
#
#
# def task(arg):
#     obj = Singleton.instance()
#     print(obj)
# for i in range(10):
#     t = threading.Thread(target=task,args=[i,])
#     t.start()
# # time.sleep(20)
# obj = Singleton.instance()
# print("11",obj)


# 使用装饰器实现单例模式。
# def Singleton(cls):
#     _instance = {}
#
#     def _singleton(*args, **kargs):
#         if cls not in _instance:
#             _instance[cls] = cls(*args,**kargs)
#         return _instance[cls]
#
#     return _singleton
#
#
# @Singleton
# class A(object):
#     a = 1
#
#     def __init__(self, x=0):
#         self.x = x
#
#
# a1 = A(2)
# a2 = A(3)
# print(id(a1))
# print(id(a2))
