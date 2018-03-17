# -*- coding: utf-8 -*-
"""
__title__ = '02 字符串格式化.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.15'
"""

'''
首先字符串格式化先了解占位符：
%s ：表示字符串占位符
%d ：表示数字占位符
%f ：浮点型占位符；
%r ：原样打印 
'''
#例子1：
'''
现有一练习需求，问用户的姓名、年龄、工作、爱好 ，然后打印成以下格式

------------ user info -----------
Name  : ryan
Age   : 25
Job   : IT
Hobbie: basketball
------------- end -----------------
'''
# while True:
# 	name = input("Name:").strip()
# 	if not name:continue
# 	age = input("Age:").strip()
# 	if not age.isdigit():continue
# 	job = input("Job:").strip()
# 	if not job:
# 		job = 'searching job status'
#
# 	hobbie = input("Hobbie:").strip()
# 	if not hobbie:
# 		hobbie = '无'
#
# 	info = '''
# ------------ user info -----------
# Name  : %s
# Age   : %s
# job   : %s
# Hobbie: %s
# ------------- end -----------------
# 	''' %(name,age,job,hobbie)
# 	if info:
# 		print(info)
# 		break

# 例子二：基于字典的字符串格式化

user_info = {}
while True:
	user_info['name'] = input("Name:").strip()
	if not user_info['name']:continue
	user_info['age'] = input("Age:").strip()
	if not user_info['age'].isdigit():continue
	user_info['job'] = input("Job:").strip()
	if not user_info['job']:
		user_info['job'] = 'searching job status'

	user_info['hobbie'] = input("Hobbie:").strip()
	if not user_info['hobbie']:
		user_info['hobbie'] = '无'

	info = '''
------------ info of -----------
Name  : %(name)s
Age   : %(age)s
job   : %(job)s
Hobbie: %(hobbie)s
------------- end -----------------
			''' %(user_info)
	if info:
		print(info)
		break

# 第三种方法
print('{name} {age}'.format(age=12,name='lhf'))






















