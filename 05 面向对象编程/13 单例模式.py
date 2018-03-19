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