# -*- coding: utf-8 -*-

# __title__ = '04 __call__方法.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.19'


# __call__(self,  *args, **kwargs) 如果类实现了这个方法，相当于把这个类型的对象当作函数来使用，相当于 重载了括号运算符

# 让对象变成一个可调用对象
# class Person(object):
#
# 	def __init__(self):
# 		print("init")
#
#
# 	def __call__(self, *args, **kwargs):
# 		print("i am chinese")
# 		print(self)         #<__main__.Person object at 0x10fa55390>
# 		print(args)         # (1, 2, 3) 位置参数
# 		print(kwargs)       # {'a': 1, 'b': 2, 'c': 3} 关键字参数
#
#
# 	def tell_info(self):
# 		print("aaa")
#
# ryan = Person()
#
# ryan(1,2,3,a=1,b=2,c=3)


# 元类内部也应有一个 __call__ 方法，会在调用Foo时触发执行。

#
class Mymeta(type):
    def __init__(self,class_name,class_bases,class_dic):
        if not class_name.istitle():
            raise TypeError('类名的首字母必须大写')

        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError('必须有注释，且注释不能为空')

        super(Mymeta,self).__init__(class_name,class_bases,class_dic)

    def __call__(self, *args, **kwargs): #obj=Chinese('ryan',age=18)
        # print(self) #self=Chinese
        # print(args) #args=('ryan',)
        # print(kwargs) #kwargs={'age': 18}

        #第一件事：先造一个空对象obj
        obj=object.__new__(self)
        #第二件事：初始化obj
        self.__init__(obj,*args,**kwargs)
        # 这里可以做一些控制实例化对象的方法
        #第三件事：返回obj
        return obj

class Chinese(object,metaclass=Mymeta):
    '''
    中国人的类
    '''
    country='China'

    def __init__(self,namem,age):
        self.name=namem
        self.age=age

    def talk(self):
        print('%s is talking' %self.name)

obj=Chinese('ryan',age=18) #Chinese.__call__(Chinese,'ryan',18)
# obj()
print(obj.__dict__)

obj.talk()
