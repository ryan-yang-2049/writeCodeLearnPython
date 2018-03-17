# -*- coding: utf-8 -*-
"""
__title__ = '04 字符串类型内建方法.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.15'
"""
#内建方法：
# string.endswith(obj, beg=0, end=len(string))  # 检测字符串是否已obj结束,如果是返回True #如果beg或end指定检测范围是否已obj结束
# string.count(str, beg=0, end=len(string))  # 检测str在string里出现次数  f.count('\n',0,len(f)) 判断文件行数
# string.find(str, beg=0, end=len(string))  # 检测str是否包含在string中
# string.index(str, beg=0, end=len(string))  # 检测str不在string中,会报异常
# string.isalnum()  # 如果string至少有一个字符并且所有字符都是字母或数字则返回True
# string.isalpha()  # 如果string至少有一个字符并且所有字符都是字母则返回True
# string.isnumeric()  # 如果string只包含数字字符,则返回True
# string.isspace()  # 如果string包含空格则返回True
# string.isupper()  # 字符串都是大写返回True
# string.islower()  # 字符串都是小写返回True
# string.lower()  # 转换字符串中所有大写为小写
# string.upper()  # 转换字符串中所有小写为大写
# string.lstrip()  # 去掉string左边的空格
# string.rstrip()  # 去掉string字符末尾的空格
# string.replace(str1, str2, num=string.count(str1))  # 把string中的str1替换成str2,如果num指定,则替换不超过num次
# string.startswith(obj, beg=0, end=len(string))  # 检测字符串是否以obj开头
# string.zfill(width)  # 返回字符长度为width的字符,原字符串右对齐,前面填充0
# string.isdigit()  # 只包含数字返回True
# string.split("分隔符")  # 把string切片成一个列表
# ":".join(string.split())  # 以:作为分隔符,将所有元素合并为一个新的字符串

# 切片操作





#举例说明：只举例比较重要的方法；

text = "hello word,word,i love china"
text2 = "this is text"

if text.endswith("ina"):print(text)
print("统计o 的个数:",text.count('o'))


if text.find("love"):print(text.find("love"))  #find 是找到 sub string 在 字符串中的起始位置

try:
	a = text.index('loa')
except ValueError:
	print("loa don't exist")

print(text.replace('word','everybody',1))  # 1 是只替换1次，如果不写则替换所有匹配的字符串。

if text.startswith('hello'):print(text)

if not text.isdigit():print('not integer number')

print(text.split())    #['hello', 'word,word,i', 'love', 'china']
print(text.split(',')) #['hello word', 'word', 'i love china']
print(":".join(text.split()))  # hello:word,word,i:love:china  以:作为分隔符,将所有元素合并为一个新的字符串

# 切片举例
print(text[::-1])   #倒着打印字符串
print(text[:-1])    #排除最后一个字符串的字符
print(text[::2])    # 每隔两个字符开始打印