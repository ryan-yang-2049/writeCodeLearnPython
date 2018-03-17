# -*- coding: utf-8 -*-
"""
__title__ = '03 替换文件内容.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.15'
"""
# 修改文件两种方式：
#
# 1）  直接把要修改的文件内容写到一个新文件，然后再把新文件rename成为一个老文件。
# 2）  把修改的内容修改以后放到一个列表里面，然后，在把列表里面的内容写到源文件。注意：当要修改的文件，或者说是要替换的字符串的长度大于新字符串的长度时，文件原始的字节长度是不变的，因此 就会出现一部分字符串在修改文件的末尾，因此，此时就要用 文件操作的方法（truncate）来进行截断。因为，当文件修改以后，游标会到修改的那个位置，因此，在游标的位置进行truncate就会把原始文件未被占用的字节长度给截断掉。


# 把info.txt 中的python替换成java

class ReplaceFileString(object):
	info_list = []
	def __init__(self,filePath,oldString,newString):
		self.oldString = oldString
		self.newString = newString
		self.filePath = filePath

	def readfile(self):
		with open(self.filePath,mode='r',encoding='utf-8') as fr:
			data = fr.read()
			print(data)

	def replace(self):
		fr = open(self.filePath,mode='r+',encoding='utf-8')
		for line in fr:
			if self.oldString in line:
				line = line.replace(self.oldString,self.newString)
			self.info_list.append(line)
		print("列表信息",self.info_list)
		values = ''.join(self.info_list)
		fr.seek(0)
		fr.write(values)
		fr.truncate()
		fr.close()

if __name__ == '__main__':
	oldString = "python"
	newString = "java"
	obj = ReplaceFileString('./info.txt',oldString,newString)
	obj.replace()
# 如果以r+ 的模式修改的文件内容，一定要注意seek 和 truncate 的用法
# seek 是指把写指针放到某个位置
#  truncate的意思就是，列表内容写完以后，假如源文件的字节长度大于现在的字节长度，那么就把现在的字节长度写完以后，进行截断。因为，不管是读还是写都是在源文件的基础上去进行的，源文件的原始字节长度不会改变。如果不进行截断，那么就会多出源文件的一部分字节出来。演示方法去掉truncate即可，并且替换的字节长度小于要替换的字节长度。


