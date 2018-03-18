# -*- coding: utf-8 -*-
"""
__title__ = '03 开源模块以及pip的使用.py'
__author__ = 'ryan'
__mtime__ = '2018/3/17'
"""
'''
https://pypi.python.org/pypi/PyTyrion/1.0.1（开源软件的一个例子<吴佩琪>）
可以用下载源码包安装：
然后执行：python3 setup.py build (编译)
  python3 setup.py install  （安装）

pip使用
    pip freeze					# 查看包版本
    pip install Package				# 安装包 pip install requests
    pip show --files Package			# 查看安装包时安装了哪些文件
    pip show --files Package			# 查看哪些包有更新
    pip install --upgrade Package		# 更新一个软件包
    pip uninstall Package           # 卸载软件包
    pip list               		# 查看pip安装的包及版本
    pip install django==1.5         	# 指定版本安装

pip命令默认会连接在国外的python官方服务器下载，速度比较慢，你还可以使用国内的豆瓣源，数据会定期同步国外官网，速度快好多
pip install -i http://pypi.douban.com/simple/ alex_sayhi（模块名） --trusted-host pypi.douban.com

'''









