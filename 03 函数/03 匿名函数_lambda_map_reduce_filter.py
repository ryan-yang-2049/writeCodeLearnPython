# -*- coding: utf-8 -*-
"""
__title__ = '03 匿名函数_lambda_map_reduce_filter.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.16'
"""
'''
python匿名函数：lambda
匿名函数作用：1.节省代码量。2.看着更优雅。

python: map(function,iterable,...)
	Python函数编程中的map()函数是将func作用于seq中的每一个元素，并将所有的调用的结果作为一个list返回。    

reduce函数：
	在Python 3里,reduce()函数已经被从全局名字空间里移除了,它现在被放置在fucntools模块里 用的话要 先引 from functools import reduce 
reduce函数的定义：
	reduce(function, sequence[, initial]) -> value
	function参数是一个有两个参数的函数，reduce依次从sequence中取一个元素，和上一次调用function的结果做参数再次调用function。
	第一次调用function时，如果提供initial参数，会以sequence中的第一个元素和initial作为参数调用function，否则会以序列sequence中的前两个元素做参数调用function。
	
filter ：过滤一个可迭代对象
	
'''

# lambda
# square = lambda x,y:x**y
# print(square(2,3))
# compare = lambda  x,y:x*y if x<y else x - y
# print(compare(3,2))

#map
# square2 = map((lambda x:x**2),range(1,5))
# print(list(square2))

# reduce
#
# from  functools import reduce
#
# print(reduce(lambda x,y:x*y,range(1,5),2))


# filter

res = filter(lambda x:x*x%2==0,range(1,10))
print(list(res))



