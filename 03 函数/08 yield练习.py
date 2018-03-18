# -*- coding: utf-8 -*-
"""
__title__ = '03 yield练习.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.16'
"""
'''
第一次见到yiled 是通过斐波那契数列中。
yield 也是生成器的一个标志。
yield：返回数据，并冻结当前函数的执行过程，直到next或者send 唤醒冻结的函数执行过程，继续执行，直到遇到下一个yield。

	1.通常的for...in...循环中，in后面是一个数组，这个数组就是一个可迭代对象，类似的还有链表，字符串，文件。它可以是mylist = [1, 2, 3]，也可以是mylist = [x*x for x in range(3)]。它的缺陷是所有数据都在内存中，如果有海量数据的话将会非常耗内存。
	2.生成器是可以迭代的，但只可以读取它一次。因为用的时候才生成。比如 mygenerator = (x*x for x in range(3))，注意这里用到了()，它就不是数组是一个生成器表达式，而上面的例子是[]。
	
	3.我理解的生成器(generator)能够迭代的关键是它有一个next()方法，工作原理就是通过重复调用next()方法，直到捕获一个异常。可以用上面的 mygenerator测试。  
	4.带有 yield 的函数不再是一个普通函数，而是一个生成器generator，可用于迭代，工作原理同上。
	5.yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行。
	6.简要理解：yield就是 return 返回一个值，并且记住这个返回的位置和状态，下次迭代就从这个位置后(下一行)开始。
	7.带有yield的函数不仅仅只用于for循环中，而且可用于某个函数的参数，只要这个函数的参数允许迭代参数。
	
****8.send(msg)与next()的区别在于send可以传递参数给yield表达式，这时传递的参数会作为yield表达式的值，而yield的参数是返回给调用者的值。换句话说，就是send可以强行修改上一个yield表达式值。比如函数中有一个yield赋值，a = yield 5，第一次迭代到这里会返回5，a还没有赋值。第二次迭代时，使用.send(10)，那么，就是强行修改yield 5表达式的值为10，本来是a = yield 5，那么现在相当于变成了 10 = yield 5

	9.send(msg)与next()都有返回值，它们的返回值是当前迭代遇到yield时，yield后面表达式的值，其实就是当前迭代中yield后面的参数
	
	10.第一次调用时必须先next()或send(None)，否则会报错，send后之所以为None是因为这时候没有上一个yield(根据第8条)。可以认为，next()等同于send(None)。
'''

def func():
    count = 0
    while count < 10:
        # print('count',count)
        count += 1
        sign = yield count
        if sign == 'stop':
            print("---sign", sign)
            break
        print('sign...',sign)
    return 3333

obj = func()
# print(next(obj)) # yield 里面的 count = 1
# print(next(obj)) # yield 里面的 count = 2
# print(next(obj)) # yield 里面的 count = 3

# print(obj.send(None))       # 返回 count 的值  1
print(obj.send(5))          # 返回 本次 send的值 5，以及下次的count = 2
print(obj.send(10))         # 返回本次send的值 10，以及下次的count = 3

# obj.send('stop')
print(next(obj))        # 返回 count = 4 的值，以及此时的生成器里面的变量 sign = None
obj.close()
print(next(obj))
# yield 的send 和next 完美解析（我都佩服我自己）：
# 当实例化生成器，并且 在生成器内部 yield 关键字的左边还有赋值变量时，如果没有send 数据时，左边的变量自动变成None。
# 第一次next 或者 send 的时候，都会在yield 停住，不往后执行。此时，被实例化后的生成器回保存当前的位置以及状态。
# 如果第二次执行next ，此时 yield 左边的值还是 None。然后，在继续循环执行到yield ，返回yield右边的值给外面的next。

# 当第一次next或者send的时候，生成器函数会在 sign = yield count 的地方卡主，并把count 的值像return一样返回给此次实例化的send，并且此时的sign 的值为None，而且，生成器会自动保存当前执行的状态，以及位置，直到下一次send 或者next
# 当第二次send('value') 的时候，生成器会从上次保存的位置 （sign = yield count）往下执行,并且此时的会把send 的value 赋值给 sign。然后，继续执行生成器的函数，一直到 sign = yield count 的地方，而且，此时的sign又变成了None

#重要提示：
# 当调用函数next(generator)时，获得生成器yiled 后面的表达式的值
# 当生成器内的值已经被执行完毕，再次调用next(generator)函数时，生成器会抛出异常“StopIteration”
# 当生成器内部执行到 return  语句时，自动抛出异常 “StopIteration” return的值将作为异常的解释
# 外部可以通过generator.close()函数手动关闭生成器，此后调用next 或者 send 方法将抛出异常。
# 当生成器第一次只使用 send 调用时，一定要先传 send(None).不然会报错，并且抛出异常 “TypeError”
