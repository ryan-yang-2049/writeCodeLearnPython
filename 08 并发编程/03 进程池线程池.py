# -*- coding: utf-8 -*-

# __title__ = '03 进程池线程池.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.21'
'''
 线程池/进程池：池对数目加以限制，保证机器以一个可承受的范围，以一个健康的状态保证程序的进行。

from multiprocessing import Pool 实现进程池
以及
from  concurrent.futures import ProcessPoolExecutor，ThreadPoolExecutor 实现进程池和线程池

'''


# 进程池
# apply 串行
# from multiprocessing import Pool
# import os,time
# def  task(n):
#     print('<%s> is running'%os.getpid())
#     time.sleep(2)
#     print('<%s> is done'%os.getpid())
#     return  n**2
#
# if __name__ == '__main__':
#     now = lambda:time.time()
#     start = now()
#     p = Pool(4)              # 如果不指定大小，默认是使用cpu的个数
#     # res1 = p.apply(task,args=(2,))              #同步提交任务    串行的执行。没有实现并发
#     # print("res",res1)
#     for i in range(1,9):
#         res= p.apply(task,args=(i,))
#         print("第%s次结果 ：%s"%(i,res))
#
#     print("主进程",os.getpid())
#     print("主进程运行时间：",now() - start)   # 主进程运行时间： 16.37465262413025

#并行 apply_async
# from multiprocessing import Pool
# import os,time
# def task(n):
#     print('<%s> is running'%os.getpid())
#     time.sleep(2)
#     print('<%s> is done'%os.getpid())
#     return  n**2
#
# if __name__ == '__main__':
#     now = lambda: time.time()
#     start = time.time()
#     p = Pool(4)              # 如果不指定大小，默认是使用cpu的个数
#     obj_l = []
#     for i in range(1,9):
#         res= p.apply_async(task,args=(i,))     # 异步提交任务。得到的是一个对象：<multiprocessing.pool.ApplyResult object at 0x000001C88A61F4A8>
#         obj_l.append(res)
#     # print(res.get())   # 在这里获取结果就会变成串行，apply 就是在返回时调用了 apply_async 的get方法造成的串行。
#     p.close()       # 禁止往进程池内再添加任务
#     p.join()
#     print("主进程",os.getpid())
#     print(obj_l)
#     for obj in obj_l:
#         print(obj.get())        # 获取结果。
#     print("主进程运行时间：", now() - start)    # 主进程运行时间： 4.441152811050415



# concurren.futures 实现进程池和线程池


# 进程池
# from  concurrent.futures import ProcessPoolExecutor
# import os,random,time
#
# def task(arg,n):
#     print('name: %s,PID: %s run'%(arg,os.getpid()))
#     time.sleep(random.randint(1,3))
#     return n**2
#
# if __name__ == '__main__':
#     # 进程池
#     now = lambda:time.time()
#     start = now()
#     pool = ProcessPoolExecutor(4)   # 如果不指认进程池的个数，默认使用CPU的个数。
#     p_list = []
#     for i in range(10):
#         p=pool.submit(task,'ryan%s'%i,i)  # 提交任务的方式叫异步调用。提交完任务，不用再等着任务提交执行结果的返回。
#         print("submit的对象：",p)          # <Future at 0x1d138564cc0 state=running>
#         p_list.append(p)
#     pool.shutdown()                 # 等待所有进程池里面的进程结束以后再去执行主进程
#     print("主")
#     print([obj.result() for obj in p_list])
#     print("run time: %s"%(now()-start))   # 运行时间： 7.62



# from  concurrent.futures import ProcessPoolExecutor
# import os,random,time
#
# def task(arg,n):
#     print('name: %s,PID: %s run'%(arg,os.getpid()))
#     time.sleep(random.randint(1,3))
#     return n**2
#
# if __name__ == '__main__':
#     # 进程池
#     now = lambda:time.time()
#     start = now()
#     pool = ProcessPoolExecutor(4)   # 如果不指认进程池的个数，默认使用CPU的个数。
#     p_list = []
#     for i in range(10):
#         p=pool.submit(task,'ryan%s'%i,i).result() # 此时 p 直接result，那么这个进程池就变成了串行。
#         p_list.append(p)
#     pool.shutdown()                 # 等待所有进程池里面的进程结束以后再去执行主进程
#     print("主")
#     print(p_list)
#     # print([obj.result() for obj in p_list])
#     print("run time: %s"%(time.time()-start)) # 18.74



# 线程池
from  concurrent.futures import ThreadPoolExecutor
import os,random,time

def task(arg,n):
    print('name: %s,PID: %s run'%(arg,os.getpid()))
    time.sleep(random.randint(1,3))
    return n**2

if __name__ == '__main__':
    # 进程池
    now = lambda:time.time()
    start = now()
    pool = ThreadPoolExecutor()             # 最大线程池，默认为： cpu个数 * 5
    p_list = []
    for i in range(22):
        p=pool.submit(task,'ryan%s'%i,i)# 提交任务的方式叫异步调用。提交完任务，不用再等着任务提交执行结果的返回。
        # print("submit的对象：",p)       # <Future at 0x1d138564cc0 state=running>
        p_list.append(p)
    pool.shutdown()                 # 等待所有进程池里面的进程结束以后再去执行主进程
    print([obj.result() for obj in p_list])
    print("run time: %s"%(now()-start))   # 运行时间：3.005432605743408










