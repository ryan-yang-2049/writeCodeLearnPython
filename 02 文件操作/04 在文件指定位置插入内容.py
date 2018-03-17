# -*- coding: utf-8 -*-
"""
__title__ = '04 在文件指定位置插入内容.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.16'
"""

#把内容插入 directory.html中
# 原始文件如下：
# <ol>
# <li><a style="text-decoration:none;color: #000000; line-height: 20px; font-family: 楷体; font-size: 20px;" href="http://www.cnblogs.com/keep-going2099/articles/8134851.html" target="_blank">python 编码格式 </a></li>
# </ol>
# 要求：当有新的url链接需要生成时，在最后一个<li></li>标签后面添加一行数据，或者说是，在</ol>前面添加一个<li></li>标签里面的内容；

import os,sys
def add_info(url,info):
	add_content = '<li><a  style="text-decoration:none;color: #000000; line-height: 20px; font-family: 楷体; font-size: 20px;" href="%s" target="_blank">%s</a></li>'%(url,info)

	with open('directory.html','r+',encoding='utf-8') as fr:
		content = fr.read()
		post = content.find('</ol>')
		if post != -1:
			content = content[:post] + add_content + '\n' + content[post:]
		fr.seek(0)
		fr.write(content)
		fr.close()

if __name__ == '__main__':
	while True:
		url = input("输入网址,退出（Q）：").strip()
		if url == 'Q':break
		if len(url) == 0:continue
		if  url.startswith("http://") or url.startswith("https://"):
			info = input("输入网站信息：").strip()
			add_info(url,info)
		else:
			print("必须是http:// 或者https:// 开头才能访问,")
			continue


'''
content = content[:post] + add_content+'\n' + content[post:]
        这里就相当于字符串的切片操作，find的意思是，如果找不到就返回-1，找到返回查找的字符串的位置。
        content = content[:post] + add_content + content[post:]
        content[:post] ：读取的是查找内容之前内容
        add_content ： 表示要添加的内容
        content[post:] ：表示查找内容之后的
'''













