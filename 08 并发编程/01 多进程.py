# -*- coding: utf-8 -*-

# __title__ = '01 多进程.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.21'


'''
进程：正在进行的一个过程或是一个任务。而负责执行任务的是CPU。
进程与程序的区别：程序仅仅是一堆代码而已，而进程指的是程序的运行过程。

并发: 单CPU，多进程并发
并行：多CPU（同时运行，只有具有多个CPU才能实现并行）

同步和异步：
	同步执行：一个进程在执行某个任务时，另外一个进程必须等待其执行完毕，才能继续执行。
	异步执行：一个进程在执行某个任务时，另外一个进程无需等待其执行完毕，就可以继续执行，当有消息返回时，系统会通知或者进行处理，这样可以提高效率。
'''


# 多进程实现socket并发

# import socket
# from multiprocessing import  Process
#
# def talk(conn):
#     while True:
#         try:
#             res = conn.recv(1024)
#             if not res:continue
#             print("recv:",res)
#             conn.send(res)
#         except ConnectionResetError:
#             break
#     conn.close()
#
# def server(ip_port):
#     server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#     server.bind(ip_port)
#     server.listen(5)
#
#     while True:
#         conn,client_addr = server.accept()
#         p = Process(target=talk,args=(conn,))
#         p.start()
#     server.close()
#
#
# if __name__ == '__main__':
#     ip_port = ('127.0.0.1',8090)
#     server(ip_port)

from  multiprocessing import  Process,Lock
import time,json

def search(name):
	'''
	查看剩余票的余额
	'''
	time.sleep(1)
	dic = json.load(open('db.txt','r',encoding='utf-8'))
	print('<%s> 查看到的剩余票数位: 【%s】'%(name,dic['count']))

def get(name):
	'''
	开始进行抢票操作
	'''
	time.sleep(1)
	dic = json.load(open('db.txt','r',encoding='utf-8'))

	if dic['count'] >0:
		dic['count'] -= 1
		time.sleep(1)
		json.dump(dic,open('db.txt','w',encoding='utf-8'))
		print('<%s> 购票成功' %name)
	else:
		print('<%s> 购票失败' % name)

def task(name,mutex):
	search(name)
	mutex.acquire()
	get(name)
	mutex.release()

if __name__ == '__main__':
	mutex = Lock()
	for i  in range(5):
		p=Process(target=task,args=('路人 %s'%i,mutex))
		p.start()




