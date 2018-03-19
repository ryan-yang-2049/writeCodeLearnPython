# -*- coding: utf-8 -*-

# __title__ = '03 __new__方法.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.19'

'''
__new__(cls[, ...])

__init__ 构造器，当一个实例被创建的时候初始化的方法。但是它并不是实例化调用的第一个方法，__new__才是实例化对象调用的第一个方法，它只取下 cls参数，并把其他参数传给 __init__。 __new__很少使用，但是也有它适合的场景，尤其是当类继承自一个像元组或者字符串这样不经常改变的类型的时候。

__new__ 使用时注意以下四点：
    1. __new__ 是在一个对象实例化的时候所调用的第一个方法

    2. 它的第一个参数是这个类，其他的参数是用来直接传递给 __init__ 方法
    3. __new__ 决定是否要使用该 __init__ 方法，因为 __new__ 可以调用其他类的构造方法或者直接返回别的实例对象来作为本类的实例，如果 __new__ 没有返回实例对象，则 __init__ 不会被调用
    4. __new__ 主要是用于继承一个不可变的类型比如一个 tuple 或者 string
    5. __new__ return的是一个构建的实例

'''

# __new__ 实现单例模式

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'instance'):
            cls.instance = super(Person,cls).__new__(cls)
        return cls.instance

# a = Person('p1',20)
# b = Person('p2',21)
# print(a is b)

# 这里的打印结果是True，可见a,和b都是同一个实例
# 单例作用：
# 第一、控制资源的使用，通过线程同步来控制资源的并发访问；
# 第二、控制实例产生的数量，达到节约资源的目的。
# 第三、作为通信媒介使用，也就是数据共享，它可以在不建立直接关联的条件下，让多个不相关的两个线程或者进程之间实现通信。
# 比如，数据库连接池的设计一般采用单例模式，数据库连接是一种数据库资源。


class Bar(object):

    def __init__(self):
        print(" this is bar class")

    def __new__(cls, *args, **kwargs):
        print("Bar class __new__")
        return object.__new__(cls,*args,**kwargs)

class Foo(object):

    def __init__(self):
        print("this is Foo class")

    def __new__(cls, *args, **kwargs):
        print("Foo class __new__")
        print("cls type:",type(cls))
        return Bar.__new__(cls,*args,**kwargs)

obj = Foo()
print(obj)
'''
所有我们发现__new__和__init__就像这么一个关系，__init__提供生产的原料self(但并不保证这个原料来源正宗，像上面那样它用的是另一个不相关的类的__new__方法类得到这个实例)，而__init__就用__new__给的原料来完善这个对象（尽管它不知道这些原料是不是正宗的）
'''


















