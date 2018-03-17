# -*- coding: utf-8 -*-
"""
__title__ = '02 读写文件.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.15'
"""
import os

#读取文件内容
def readDataFromTxt(path):
	contents=""
	if os.path.exists(path):
		try:
			fr = open(path,'r',encoding='utf-8')
			contents = fr.read()
			fr.close()
		except IOError:
			print("提示：文件不存在，或者读取异常")
	else:
		print("提示：文件"+path+"不存在，请输入正确路径！")

	return contents

# 把内容写入文件
def  writeDataFile(path,mytxt):
	if os.path.exists(path):
		try:
			fw = open(path,'a+')
			fw.write(mytxt+'\n')
			fw.close()
		except IOError:
			print("提示：文件不存在，或者读取异常")
	else:
		print("提示：文件"+path+"不存在，创建该文件！")
		fw = open(path,'a+')
		fw.write(mytxt+'\n')
		fw.close()

# 将A文件写入B文件

def writeAFile2BFile(aPath,bPath):
	mytxt = readDataFromTxt(aPath)
	if mytxt:
		print("写入的内容："+mytxt)
		writeDataFile(bPath,mytxt)
		mytxtB = readDataFromTxt(bPath)
		print("写入的文件内容："+mytxtB)

	else:
		print("提示：输入的文件不存在")



# if __name__ == '__main__':
# 	currentPath = os.getcwd()
# 	aPath = currentPath+"\\passwd.txt"
# 	bPath = currentPath+"\\passwd.bak"
# 	writeAFile2BFile(aPath,bPath)


open('passwd.bak','a+').write(open('passwd.txt','r').read()+'\n')


