# -*- coding: utf-8 -*-
"""
__title__ = '01 查看模块的使用方法.py'
__author__ = 'ryan'
__mtime__ = '2018/3/17'
"""

'''
查看模块的使用方法：
	1.去查看对应版本的 documentation 然后搜索，查看文档
	2.去Console 去import，然后 print(timeit.__doc__)去查看文档
	2.1 查看该模块的BIF(内置函数) 是  dir(模块名称)
	2.2 如果BIF里面有 '__all__' 的BIF，则可以通过  模块.__all__ 去查看方法（未显示的则不能被直接使用）
	注意：
	第一，不是所有的模块都有'__all__' 属性；
	第二，如果一个模块设置了 '__all__'属性，那么使用"from 模块 import *" 这样的形式导入命名空间，就只有'__all__'属性这个列表里边的名字才会被导入，
	其他的BIF不受影响。但如果没有设置 '__all__'属性的话，用"from 模块 import *" 就会把所有不以下划线开头的名字都导入到当前的命名空间。所以，
	建议在编写模块的时候，将对外提供的接口函数和类都设置在'__all__'属性这个列表里
	'__file__'属性指明了该模块的源代码位置；
'''

import timeit

print(timeit.__file__)


#res:/usr/local/Cellar/python3/3.6.1/Frameworks/Python.framework/Versions/3.6/lib/python3.6/timeit.py







