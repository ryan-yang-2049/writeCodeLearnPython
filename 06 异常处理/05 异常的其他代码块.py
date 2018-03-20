# -*- coding: utf-8 -*-

# __title__ = '05 异常的其他代码块.py'
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

except Exception as e:
    print("Exception 异常结果为:", e)

else:
    print('try内代码块没有异常则执行!')
finally:
    print('无论异常与否,都会执行该模块,通常是进行清理工作!')





