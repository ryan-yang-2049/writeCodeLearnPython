# -*- coding: utf-8 -*-

# __title__ = '06 主动触发异常.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.20'


try:
    raise TypeError('类型错误')
except Exception as e:
    print("Exception 异常结果为:", e)    # Exception 异常结果为: 类型错误










