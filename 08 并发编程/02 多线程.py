# -*- coding: utf-8 -*-

# __title__ = '02 多线程.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.21'


'''
进程只是用来把资源集中到一起（进程只是一个资源单位，或者说资源集合），而线程才是cpu上的执行单位。

多线程（即多个控制线程）的概念是，在一个进程中存在多个线程，多个线程共享该进程的地址空间

进程和线程最大的区别在于:
    同一个进程内的多个线程共享该进程内的地址资源
    创建线程的开销要远小于创建进程的开销


多线程与多进程的区别
1.开启线程的开销比开启进程的开销要小。
2.线程的PID与开启线程的进程的PID相同，就不需要重新去申请内存地址空间。进程在开启子进程就需要去申请，因此，速度慢。
3.进程之间的数据是相互隔离的。同一进程内开启的多个线程是共享该进程地址空间的

'''

# 如果并发的多个任务是计算密集型：多进程效率高
from multiprocessing import Process
from threading import Thread
import os,time
def work():
    res=0
    for i in range(100000000):
        res*=i


if __name__ == '__main__':
    l=[]
    print(os.cpu_count()) #本机为4核
    start=time.time()
    for i in range(4):
        # p=Process(target=work) #耗时21s多
        p=Thread(target=work) #耗时62多
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop=time.time()
    print('run time is %s' %(stop-start))


#如果并发的多个任务是I/O密集型：多线程效率高
from multiprocessing import Process
from threading import Thread
import threading
import os,time
def work():
    time.sleep(2)
    print('===>')

if __name__ == '__main__':
    l=[]
    print(os.cpu_count()) #本机为4核
    start=time.time()
    for i in range(400):
        p=Process(target=work) #耗时52s多,大部分时间耗费在创建进程上
        # p=Thread(target=work) #耗时2s多
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop=time.time()
    print('run time is %s' %(stop-start))































