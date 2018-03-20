# -*- coding: utf-8 -*-

# __title__ = '06 __repr__方法.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.20'


#__str__与__repr__ 是在类(对象)中对类(对象)本身进行字符串处理。

# __str__ 与 __repr__ 在我看来，__repr__ 是隐形显示的给开发人员看的，__str__ 是给用户看的

class A(object):

    def __str__(self):
        return  "__str__"

    def __repr__(self):
        return "__repr__"

a = A()
b = A

a           # __repr__ ,在console 中显示，在py文件中不显示。
print(a)    #__str__
print(b)    # <class 'A'>


