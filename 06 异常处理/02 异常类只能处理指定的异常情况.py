# -*- coding: utf-8 -*-

# __title__ = '02 异常类只能处理指定的异常情况.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.20'


s1 = 'hello'

# try:
#     int(s1)             # 如果不捕获异常将会报错： ValueError: invalid literal for int() with base 10: 'hello'
# except IndexError as e:
#     print(e)


#正确用法：
try:
    int(s1)             # 如果不捕获异常将会报错： ValueError: invalid literal for int() with base 10: 'hello'
except ValueError as e:
    print("异常结果为:",e)       # 异常结果为: invalid literal for int() with base 10: 'hello'




