# -*- coding: utf-8 -*-

# __title__ = '01 isinstance和issubclass.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.19'


'''
1. isinstance(obj,cls) 和 issubclass(sub,super)
'''


class Foo(object):
    pass
class Bar(Foo):
    pass

obj = Foo()
# isinstance(obj,cls)检查是否obj是否是类 cls 的对象
print(isinstance(obj,Foo))      # True

#issubclass(sub, super)检查sub类是否是 super 类的派生类
print(issubclass(Bar,Foo))  #True








