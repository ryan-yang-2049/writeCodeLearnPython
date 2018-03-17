# -*- coding: utf-8 -*-
"""
__title__ = '08 python内建函数.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.15'
"""

# 内建函数
#
# dir(sys)  # 显示对象的属性
# help(sys)  # 交互式帮助
# int(obj)  # 转型为整形
# str(obj)  # 转为字符串
# len(obj)  # 返回对象或序列长度
# open(file, mode)  # 打开文件 #mode (r 读,w 写, a追加)
# range(0, 3)  # 返回一个整形列表
# input("str:")  # 等待用户输入
# type(obj)  # 返回对象类型
# abs(-22)  # 绝对值
# random  # 随机数
# choice()  # 随机返回给定序列的一个元素
# divmod(x, y)  # 函数完成除法运算，返回商和余数。
# round(x[, n])  # 函数返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数
# strip()  # 是去掉字符串两端多于空格,该句是去除序列中的所有字串两端多余的空格
# del  # 删除列表里面的数据
# cmp(x, y)  # 比较两个对象    #根据比较结果返回一个整数，如果x<y，则返回-1；如果x>y，则返回1,如果x==y则返回0
# max()  # 字符串中最大的字符
# min()  # 字符串中最小的字符
# *sorted()  # 对序列排序
# *reversed()  # 对序列倒序
# *enumerate()  # 返回索引位置和对应的值
# sum()  # 总和
# list()  # 变成列表可用于迭代
# eval('3+4')  # 将字符串当表达式求值 得到7
# exec('a=100')  # 将字符串按python语句执行
# tuple()  # 变成元组可用于迭代   #一旦初始化便不能更改的数据结构,速度比list快
# *zip(s, t)  # 返回一个合并后的列表  s = ['11','22']  t = ['aa','bb']  [('11', 'aa'), ('22', 'bb')]
# *isinstance(object, int)  # 测试对象类型 int
# range([lower, ]
# stop[, step])  # 函数与range()类似，但xrnage()并不创建列表，而是返回一个xrange对象

li = ['a','b','c']

for k,v in enumerate(li,1):
	print(k,v)
