# -*- coding: utf-8 -*-
"""
__title__ = '02 LEGB 规则及 global and nolocal.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.16'
"""

'''
在Python中当引用1个变量时，对这个变量的搜索是按照 **LEGB** 规则顺序进行的：  
1. 本地作用域 (Local)  
2. 嵌套作用域 (Enclosing function locals)  
3. 全局作用域 (Global)  
4. 内置作用域 (builtins模块)  
- 当在函数内为一个变量赋值时，并非按上面所说LEGB规则来首先找到变量之后为其赋值。
- 在Python中，在函数中为一个变量赋值时，有下面这样一条规则：当在函数中为1个变量名赋值时( 而不是在一个表达式中对其进行引用 )，Python **总是创建或改变本地作用域的变量名，除非它已经在那个函数中被声明为全局变量!**

理解Python的LEGB原则是理解Python命名空间的关键，而理解Python的命名空间又是理解Python中许多语法规定的关键。所以Python的LEGB原则就成为Python中一个非常核心的内容
白话一点讲：命名空间是对变量名的分组划分!
不同组的相同名称的变量视为两个独立的变量，因此隶属于不同分组（即命名空间）的变量名可以重复。
命名空间可以存在多个，使用命名空间，表示在该命名空间中查找当前名称。

Python一切皆对象，所以在Python中变量名是字符串对象:
>>> a = 10
表示建立字符串对象a与Number对象10的对应。由于这是一种映射所以可以使用键值形式表示 {name : object}。

前面已经说过，命名空间是对变量名的分组划分，所以Python的命名空间就是对许多键值对的分组划分，即键值对的集合，因此：Python的命名空间是一个字典，字典内保存了变量名称与对象之间的映射关系
Python有多个命名空间，因此需要有规则来规定按照怎样的顺序来查找命名空间，“LEGB”就是用来规定命名空间查找顺序的规则。

#### LEGB含义： 
*  L Local(function)：  函数内的名字空间
*  E Enclosing function locals：    外部嵌套函数的名字空间(例如closure)
*  G Global(module)：   函数定义所在模块（文件）的名字空间
*  B Builtin(Python)：  Python内置模块的名字空间
#### 

'''
# global
# 例1：把全局变量在函数内进行修改,并把函数内的变量赋值给全局： global
x = 10

def func():
	global x,y
	y = 20
	x = 11
func()
print(x,y)


#Nolocal
# 关键子nonlocal作用与global类似，使用nonlocal关键字可 **在一个嵌套的函数中修改嵌套作用域中的变量**（非全局）
# 注意  nolocal 不能改变全局变量

def  func02():
	a = 1
	def func03():
		nonlocal a
		a = 2
	func03()
	print(a)

func02()


# 注：
# 使用global关键字修饰的变量之前可以不存在，但使用nonlocal关键字修饰的变量在嵌套作用域中必须已经存在

'''
参考：  
https://segmentfault.com/a/1190000000640834  
http://www.jianshu.com/p/3b72ba5a209c
'''

age = 19
def func01():
	global age   #==>等价于 把全局变量age=19 放到此处，然后此处的age还是全局变量
	def func02():
		print("inner",age)
	age = 73      #==>此处的age还是全局变量，并且 age = 73
	func02()
func01()
print("outer",age)

