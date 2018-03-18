# -*- coding: utf-8 -*-
"""
__title__ = '02 自定义模块和包的导入方法.py'
__author__ = 'ryan'
__mtime__ = '2018/3/17'
"""

# 自定义模块：就是自己写的任何一个python脚本都是自定义模块。
# 导入方法就是 直接import 文件名(不带.py)

# 到如包的方法：

#环境：做一个比较大的项目，该项目需要很多py文件来进行完成。那就要区分代码文件的含义与用途。那就会把这些文件，区分开放在某个目录下。
#而这些文件之间需要互相的去调用，那么这些目录就要设置为python包。
#那包与包之间的导入主要是从顶层开始导入，就是说，从该功能或者项目的顶层目录去导入
# 那导入包里面的模块就需要去获取他们的路径


import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

#"__file__"表示的是当前py文件文件名，然后用os.path.abspath获取绝对路径，然后，用os.path.dirname获取相对路径








