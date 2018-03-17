# -*- coding: utf-8 -*-
"""
__title__ = '07 生成器_迭代器.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.16'
"""
'''

一个生成器表达式或者函数就是一个生成器，生成器大部分都是一个迭代器，迭代器总是一个可迭代对象。
列表，集合，字典 可以生成一个容器，他们通常是一个可迭代对象，一个可迭代对象经过 iter()以后，就可以变成一个迭代器。
一个迭代器 通过next()，一个一个的获取迭代器里面的value

可迭代对象和容器一样是一种通俗的叫法，并不是指某种具体的数据类型，list是可迭代对象，dict是可迭代对象，set也是可迭代对象。
容器：容器是一种把多个元素组织在一起的数据结构，容器中的元素可以逐个地迭代获取，可以用 in、not in 关键字判断元素是否包含在容器中。尽管绝大多数容器都提供了某种方式来获取其中的每一个元素，但这并不是容器本身提供的能力，而是可迭代器对象赋予了容器这种能力，当然并不是所有的容器都是可迭代的。

可迭代对象：但凡是可以返回一个迭代器的对象都可称之为可迭代对象。

迭代器：是一个带状态的对象，他能在你调用 next() 方法的时候返回容器中的下一个值，任何实现了  __iter__ 和 __next__（） 方法的对象都是迭代器，__iter__ 返回迭代器自身， __next__ 返回容器中的下一个值，如果容器中没有更多元素了，则抛出 StopIteration 异常

迭代器内部持有一个状态，该状态用于记录当前迭代所在的位置，以方便下次迭代的时候获取正确的元素。

生成器：生成器算得上是Python语言中最吸引人的特性之一，生成器其实是一种特殊的迭代器，不过这种迭代器更加优雅。它不需要再像上面的类一样写__iter__()和__next__()方法了，只需要一个 yiled 关键字。 生成器一定是迭代器（反之不成立），因此任何生成器也是以一种懒加载的模式生成值。
优点：相比其它容器对象它更能节省内存和CPU
yield实现。

'''
#可迭代对象：
# x = list(range(10))  # 列表，是一个可迭代对象，通过iter 可以变成迭代器
# y = iter(x)          # 迭代器
#
# print(next(y))       # 迭代器通过 next 获取值
# print(next(y))
# print(next(y))
# print(next(y))


# 迭代器：

# 生成无限序列
# from itertools import count
# counter = count(start=3)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# 从有限序列中生成无限序列
# from itertools import  cycle
#
# colors = cycle(['red','white','blue'])
# print(next(colors))
# print(next(colors))
# print(next(colors))
# print(next(colors))

#迭代器就像一个懒加载的工厂，等到有人需要的时候才给它生成值返回，没调用的时候就处于休眠状态等待下一次调用。


# 生成器:相比其它容器对象它更能节省内存和CPU
#实现斐波那契数列
#
# def fib(max):
# 	n,a,b = 0,0,1
# 	while n<max:
# 		yield b
# 		a,b = b,a+b
# 		n +=1
#
# for i in fib(10):
# 	print(i)
#
# # 或者
# print(next(fib(10)))

'''
fib就是一个普通的python函数，它特殊的地方在于函数体中没有return关键字，函数的返回值是一个生成器对象。当执行f=fib()返回的是一个生成器对象，此时函数体中的代码并不会执行，只有显示或隐示地调用next的时候才会真正执行里面的代码。

生成器在Python中是一个非常强大的编程结构，可以用更少地中间变量写流式代码，此外，相比其它容器对象它更能节省内存和CPU，当然它可以用更少的代码来实现相似的功能。
'''

# 生成器表达式

gen = (x*x for x in range(10))
print(type(gen))        # <class 'generator'>

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))













