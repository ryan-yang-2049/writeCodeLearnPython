# -*- coding: utf-8 -*-

# __title__ = '07 自定义异常.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.20'

class DefineException(BaseException):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    raise DefineException("自定义的错误结果")

except DefineException as e:
    print("DefineException 自定义异常的报错结果为：",e)


'''
总结try..except

1：把错误处理和真正的工作分开来

2：代码更易组织，更清晰，复杂的工作任务更容易实现；

3：毫无疑问，更安全了，不至于由于一些小的疏忽而使程序意外崩溃了；

'''




