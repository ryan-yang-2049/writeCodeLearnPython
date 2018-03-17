# -*- coding: utf-8 -*-
"""
__title__ = '06 字典内建方法.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.15'
"""

# 字典内建方法
#
# dict.clear()  # 删除字典中所有元素
# *dict
# copy()  # 返回字典(浅复制)的一个副本
# *dict.fromkeys(seq, val=None)  # 创建并返回一个新字典,以seq中的元素做该字典的键,val做该字典中所有键对的初始值
# *dict.get(key, default=None)  # 对字典dict中的键key,返回它对应的值value,如果字典中不存在此键,则返回default值
# *dict.items()  # 返回一个包含字典中键、值对元组的列表
# *dict.keys()  # 返回一个包含字典中键的列表
# dict.pop(key[, default])  # 和方法get()相似.如果字典中key键存在,删除并返回dict[key]
# dict.setdefault(key, default=None)  # 和set()相似,但如果字典中不存在key键,由dict[key]=default为它赋值
# *dict.update(dict2)  # 将字典dict2的键值对添加到字典dict
# *dict.values()  # 返回一个包含字典中所有值得列表
#
# dict([container])  # 创建字典的工厂函数。提供容器类(container),就用其中的条目填充字典
# len(mapping)  # 返回映射的长度(键-值对的个数)
# hash(obj)  # 返回obj哈希值,判断某个对象是否可做一个字典的键值







