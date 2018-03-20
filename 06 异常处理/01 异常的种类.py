# -*- coding: utf-8 -*-

# __title__ = '01 异常的种类.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.20'

#为了保证程序的健壮性与容错性，即在遇到错误时程序不会崩溃，我们需要对异常进行处理。


#常见异常
'''
AttributeError 试图访问一个对象没有的属性，比如foo.x，但是foo没有属性x
IOError 输入/输出异常；基本上是无法打开文件
ImportError 无法引入模块或包；基本上是路径问题或名称错误
IndentationError 语法错误（的子类） ；代码没有正确对齐
IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError 试图访问字典里不存在的键
KeyboardInterrupt Ctrl+C被按下
NameError 使用一个还未被赋予对象的变量
SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError 传入对象类型与要求的不符合
UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，
导致你以为正在访问它
ValueError 传入一个调用者不期望的值，即使值的类型是正确的

'''

# 如果错误发生的条件是可预知的，我们需要用if进行处理：在错误发生之前进行预防

AGE = 10
while True:
    age = input(">>:").strip()
    if age.isdigit():    # 只有在age为字符串形式的整数时,下列代码才不会出错,该条件是可预知的
        age = int(age)
        if age == AGE:
            print('You guessed it')
            break



# 如果错误发生的条件是不可预知的，则需要用到try...except：在错误发生之后进行处理
#基本语法为
try:
    '被检测的代码块'
except '异常类型':
    'try中一旦检测到异常，就执行这个位置的逻辑'
#举例
try:
    f=open('a.txt')
    g=(line.strip() for line in f)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration:
    f.close()
