# -*- coding: utf-8 -*-

# __title__ = '12 反射.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.19'


# 反射：通过字符串映射到对象的属性


class People(object):
    COUNTRY = 'China'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' % self.name)

obj = People('ryan',18)

# 判断对象有没有这个属性  hasattr(obj,属性)
print(obj.__dict__)
print("hasattr:",hasattr(obj,'name')) #判断是否有 obj.name 这个属性，本质上是去判断对象的__dict__ 下面是否有这个属性 obj.__dict__['name']

print("hasattr:",hasattr(obj,'talk'))

# 获取对象的属性  getattr(obj，'属性','默认值')
print("getattr 对象属性:",getattr(obj,'namexxx',None))
print("getattr 对象绑定方法:",getattr(obj,'talk',None))   # <bound method People.talk of <__main__.People object at 0x000002718A7A9F28>>


# 设置对象属性  setattr(obj,'属性','value')
setattr(obj,'sex','male') #obj.sex='male'
print("setattr 设置对象属性 sex =",obj.sex)

# 删除对象属性
delattr(obj,'age') #本质上是 del obj.age
print("delattr 删除U对象属性",obj.__dict__)


print(getattr(People,'COUNTRY')) #判断People类中是否有country的属性：People.country



################# 反射的应用

class Service:
    def run(self):
        while True:
            inp=input('>>: ').strip() #cmd='get a.txt'
            cmds=inp.split() #cmds=['get','a.txt']
            # print(cmds)
            if hasattr(self,cmds[0]):
                func=getattr(self,cmds[0])
                func(cmds)

    def get(self,cmds):
        print('get.......',cmds[1])

    def put(self,cmds):
        print('put.......',cmds[1])

obj=Service()
obj.run()

















