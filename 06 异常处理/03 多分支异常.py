# -*- coding: utf-8 -*-

# __title__ = '03 多分支异常.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.20'




s1 = 'hello'
try:
    int(s1)
except IndexError as e:
    print("IndexError 异常结果为:", e)
except KeyError as e:
    print("KeyError 异常结果为:", e)
except ValueError as e:
    print("ValueError 异常结果为:", e)






