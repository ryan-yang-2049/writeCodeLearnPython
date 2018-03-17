# -*- coding: utf-8 -*-
"""
__title__ = '07 集合的内建方法.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.15'
"""
# 集合方法
#
# s.update(t)  # 用t中的元素修改s,s现在包含s或t的成员   s |= t
# s.intersection_update(t)  # s中的成员是共用属于s和t的元素          s &= t
# s.difference_update(t)  # s中的成员是属于s但不包含在t中的元素    s -= t
# s.symmetric_difference_update(t)  # s中的成员更新为那些包含在s或t中,但不是s和t共有的元素  s ^= t

# s.remove(obj)  # 从集合s中删除对象obj;如果obj不是集合s中的元素(obj not in s),将引发KeyError错误
# s.discard(obj)  # 如果obj是集合s中的元素,从集合s中删除对象obj
# s.pop()  # 删除集合s中的任意一个对象,并返回它
# s.clear()  # 删除集合s中的所有元素
# s.issubset(t)  # 如果s是t的子集,则返回True   s <= t
# s.issuperset(t)  # 如果t是s的超集,则返回True   s >= t
# s.union(t)  # 合并操作;返回一个新集合,该集合是s和t的并集   s | t

# s.difference(t)  # 返回一个新集合,改集合是s的成员,但不是t的成员  s - t
# s.symmetric_difference(t)  # 返回一个新集合,该集合是s或t的成员,但不是s和t共有的成员   s ^ t
# s.copy()  # 返回一个新集合,它是集合s的浅复制
# obj in s  # 成员测试;obj是s中的元素 返回True
# obj not in s  # 非成员测试:obj不是s中元素 返回True
# s == t  # 等价测试 是否具有相同元素
# s != t  # 不等价测试
# s < t  # 子集测试;s!=t且s中所有元素都是t的成员
# s > t  # 超集测试;s!=t且t中所有元素都是s的成员

# s.add(obj)  # 在集合s中添加对象obj

# s.intersection(t)  # 交集操作;返回一个新集合,该集合是s和t的交集   s & t
s = {1,2,3,4,5,6}
t = {2,4,6,7,8,9}

print(s.intersection(t)) #交集

s.add('a') #怎加元素
print(s)

print(s.difference(t))



