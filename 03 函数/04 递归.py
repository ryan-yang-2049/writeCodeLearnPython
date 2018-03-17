# -*- coding: utf-8 -*-
"""
__title__ = '04 递归.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.16'
"""

'''
递归的层数是有限的（1000层：sys.getrecursionlimit()）。
对某个变量或者程序需要重复执行时就可以用到递归。

递归的特性：
1.	必须要有一个明确的结束条件
2.	每次进入更深一层递归时，问题规模相比上一次递归都应有所减少。
3.	递归效率不高，递归层次过多会导致栈溢出（在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出）

'''

# def calc(n):
# 	n = int(n/2)
# 	print(n)
# 	if n>0:
# 		calc(n)
# 	print(n)
# calc(10)

# 递归的返回值

def calc(n,count):
    print(n,count)
    if count < 5:
        return calc(n/2,count+1)
    else:
        return n
res = calc(100,1)
print(res)





