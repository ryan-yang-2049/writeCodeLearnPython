# -*- coding: utf-8 -*-

# __title__ = '04 万能异常Exception.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.20'

s1 = 'hello'

try:
    int(s1)
except Exception as e:
    print("Exception 异常结果为:", e)        # Exception 异常结果为: invalid literal for int() with base 10: 'hello'


# 万能异常主要用于不可预知的异常捕获

s1 = 'hello'
try:
    int(s1)
except IndexError as e:
    print("IndexError 异常结果为:", e)
except KeyError as e:
    print("KeyError 异常结果为:", e)

except Exception as e:
    print("Exception 异常结果为:", e)








