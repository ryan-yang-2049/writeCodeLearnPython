# -*- coding: utf-8 -*-
"""
__title__ = '01 时间的表示方式.py'
__author__ = 'ryan'
__mtime__ = '2018/3/18'
"""

'''
在Python中，通常有这几种方式来表示时间：
1.	时间戳
2.	格式化的时间字符串
3.	元组（struct_time）共九个元素。由于Python的time模块实现主要调用C库，所以各个平台可能有所不同。

时间戳（timestamp）的方式：通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。我们运行“type(time.time())”，返回的是float类型。

元组（struct_time）方式：struct_time元组共有9个元素，返回struct_time的函数主要有gmtime()，localtime()，strptime()。下面列出这种方式元组中的几个元素：
索引（Index）    属性（Attribute）    值（Values）
0     tm_year（年）                  比如2011 
1     tm_mon（月）             	    1 - 12
2     tm_mday（日）                  1 - 31
3     tm_hour（时）                  0 - 23
4     tm_min（分）             	    0 - 59
5     tm_sec（秒）             	    0 - 61
6     tm_wday（weekday）          	0 - 6（0表示周日）
7     tm_yday（一年中的第几天）    	1 - 366
8     tm_isdst（是否是夏令时）  	    默认为-1

'''













