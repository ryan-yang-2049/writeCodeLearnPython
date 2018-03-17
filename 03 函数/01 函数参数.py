# -*- coding: utf-8 -*-
"""
__title__ = '01 函数参数.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.16'
"""

def func01(*args,**kwargs):
	for i in args:
		print(i)

arg = list(range(3))
func01(arg)
func01(*arg)
'''
传递的列表参数，如果不带 * 号表示，把整个列表看成一个变量。
如果传递的列表带了* 号，那么表示，把所有的列表里面的元素，单独看成一个参数
[0, 1, 2]
0
1
2
'''
# 非固定参数：用字典传入 也称为关键字参数。
def func02(*args,**kwargs):
	print("name:",kwargs['name'])
	print("age:",kwargs['age'])


dic = {'name':'ryan','age':20}
func02(**dic)



