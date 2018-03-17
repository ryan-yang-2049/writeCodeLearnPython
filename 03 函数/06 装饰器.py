# -*- coding: utf-8 -*-
"""
__title__ = '06 装饰器.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.16'
"""
'''
装饰器用来装饰函数或类，使用装饰器可以在函数执行前和执行后添加相应操作。
装饰器原理：
python允许将方法当做参数传递。
	开放封闭原则；
		•	封闭：已实现的功能代码块
		•	开放：对扩展开发
装饰器好处：装饰器的好处就是，不改变源代码而去实现一个新功能。

它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
'''

# 1,简单装饰器，插入日志
# import logging
# def loginfo(func):
# 	def warnLog(*args,**kwargs):
# 		logging.warning("%s is running"%func.__name__)
# 		return func(*args,**kwargs)
# 	return warnLog
#
# @loginfo          # 等价于 bar = loginfo(bar)
# def bar():
# 	print("i am bar")
#
# bar()


# 2，带参数装饰器
# import logging
#
# def logLevel(level):
# 	def log_func(func):
# 		def log_info(*args,**kwargs):
# 			if level == 'warn':
# 				logging.warning("%s is running"%func.__name__)
# 			return func(*args,**kwargs)
# 		return log_info
# 	return log_func
#
# @logLevel('warn')
# def bar():
# 	print("i am bar")
#
# bar()


# 3,登陆认证使用装饰器
#  使用functools.wraps装饰器,它能把原函数的元信息拷贝到装饰器函数中，这使得装饰器函数也有和原函数一样的元信息了。
# from  functools import wraps
#
# def login_auth(func):
# 	@wraps(func)
# 	def auth_info(*args,**kwargs):
# 		if password == '1111' and username == 'ryan':
# 			print(func.__name__, func.__doc__, 'call decorator') # 如果不加wraps 装饰器，就获取不了被装饰函数的元信息
# 			func(*args,**kwargs)
# 	return auth_info
#
# @login_auth
# def run(username):
# 	""" running"""
# 	print("%s,welcome to this system"%username)
#
# if __name__ == '__main__':
# 	username = input("name:").strip()
# 	password = input("passwd:").strip()
# 	run(username)
#
# 	print(run.__name__)  # wrapper
# 	print(run.__doc__)



# 4，利用装饰器记录程序运行时间
import time
from functools import reduce
def timer(func):
	def inner(*args,**kwargs):
		now = lambda:time.time()
		start = now()
		func(*args,**kwargs)
		print("程序运行时间：%s"%(now()-start))
	return inner

@timer
def run(n):
	square = reduce(lambda x,y:(x*y)*3.1415,map(lambda x:x**2,range(2,n)))
	print("square:",square)

run(2222225)
















