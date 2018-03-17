# -*- coding: utf-8 -*-
"""
__title__ = '01 文件对象方法和属性.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.15'
"""
#open 打开文件模式
'''
w  :以写方式打开。（如果文件中有内容会被覆盖）
a  :以追加模式打开。
r+ :以读写方式打开。
w+ :以读写模式打开 (参见 w )
a+ :以读写模式打开 (参见 a )
rb :以二进制读模式打开
wb :以二进制写模式打开 (参见 w )
ab :以二进制追加模式打开 (参见 a )
rb+:以二进制读写模式打开 (参见 r+ )
wb+:以二进制读写模式打开 (参见 w+ )
ab+:以二进制读写模式打开 (参见 a+ )
'''



# 文件对象方法
#
# file.close()  # 关闭文件
# file.fileno()  # 返回文件的描述符
# file.flush()  # 刷新文件的内部缓冲区
# file.isatty()  # 判断file是否是一个类tty设备
# file.next()  # 返回文件的下一行,或在没有其他行时引发StopIteration异常
# file.read(size=-1)  # 从文件读取size个字节,当未给定size或给定负值的时候,读取剩余的所有字节,然后作为字符串返回
# file.readline(size=-1)  # 从文件中读取并返回一行(包括行结束符),或返回最大size个字符
# *file.readlines(sizhint=0)  # 读取文件的所有行作为一个列表返回
# file.seek(off, whence=0)  # 在文件中移动文件指针,从whence(0代表文件起始,1代表当前位置,2代表文件末尾)偏移off字节
# file.tell()  # 返回当前在文件中的位置
# file.truncate(size=file.tell())  # 截取文件到最大size字节,默认为当前文件位置
# *file.write(str)  # 向文件写入字符串
# file.writelines(seq)  # 向文件写入字符串序列seq;seq应该是一个返回字符串的可迭代对象

#
# 文件对象的属性
#
# file.closed  # 表示文件已被关闭,否则为False
# file.encoding  # 文件所使用的编码  当unicode字符串被写入数据时,它将自动使用file.encoding转换为字节字符串;若file.encoding为None时使用系统默认编码
# file.mode  # Access文件打开时使用的访问模式
# file.name  # 文件名
# file.newlines  # 未读取到行分隔符时为None,只有一种行分隔符时为一个字符串,当文件有多种类型的行结束符时,则为一个包含所有当前所遇到的行结束符的列表
# file.softspace  # 为0表示在输出一数据后,要加上一个空格符,1表示不加


