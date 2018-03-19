# -*- coding: utf-8 -*-

# __title__ = '06 组合.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.19'

"""
组合指的是，在一个类中以另一个类的对象作为数据属性，称为类的组合。
*** 组合与继承都是有效的利用已有类的资源的重要方式。

组合应该是一种什么“有”什么的关系

"""

class People(object):
    school='luffycity'
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

class Teacher(People):
    def __init__(self,name,age,sex,level,salary):
        super().__init__(name,age,sex)
        self.level=level
        self.salary=salary

    def teach(self):
        print('%s is teaching' %self.name)

class Student(People):
    def __init__(self, name, age, sex, class_time):
        super().__init__(name,age,sex)
        self.class_time=class_time
    def learn(self):
        print('%s is learning' % self.name)

class Course(object):
    def __init__(self,course_name,course_price,course_period):
        self.course_name = course_name
        self.course_price = course_price
        self.course_period = course_period
    def tell_info(self):
        return  ('课程名<%s> 课程价钱<%s> 课程周期<%s>' %(self.course_name,self.course_price,self.course_period))

# 实例化对象
tc1 = Teacher('alex',18,'male',10,3000)
tc2 = Teacher('egon',28,'male',30,3000)
python = Course('python',3000,'3mons')
linux = Course('Linux',2000,'2mons')

tc1.course = python
tc2.course = linux

print("实例化的对象：",python)
print("实例化对象的属性：",python.course_name)
print("教师1的课程对象：",tc1.course)
print("教师2的课程对象：",tc2.course)
print("教师1的课程名称：",tc1.course.course_name)
print("教师2的课程名称：",tc2.course.course_name)
print("教师1的课程信息：",tc1.course.tell_info())
print("教师2的课程信息：",tc2.course.tell_info())

print(tc1.course.__dict__)

"""
自己了解的组合：在类A 与类B里面，类A没有x的属性，但是，类B里面有x属性对应的想要的内容。因此，就会 M=A（），先实例化对象M（类A的对象），N=B（），然后，M.x = N，这就是组合,这样就可以在M这个对象里面，有了x 的属性，去访问N 里面的属性或方法。（对象（A）.属性=对象（B））。顺便提一下，组合应该是一种什么有什么的现象。比如，飞机可以飞，如果人的这个对象去组合飞机的对象，那就得到了人可以飞，这个不是现实生活中的对象应该具有的类的特征。所以，不可以。

结论：可以看到，实例化的对象都是内存地址，只有调用该属性的时候，才可以得到它的值。
因此可以看出组合.   对象.属性 = 内存地址 。（赋值的是一个内存地址）
"""


# 学生学习多门课程的组合使用

st1 = Student('张三',28,'female','08:30:00')

st1.course = [python,linux]
print("学生学习的第 1 门课程：",st1.course[0].tell_info())
print("学生学习的第 2 门课程：",st1.course[1].tell_info())










