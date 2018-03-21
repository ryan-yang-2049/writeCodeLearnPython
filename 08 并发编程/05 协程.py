# -*- coding: utf-8 -*-

# __title__ = '05 协程.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.21'

'''
并发的本质：切换+保存状态

无论多线程和多进程，IO的调度更多取决于系统，而协程的方式，调度来自用户，用户可以在函数中yield一个状态。使用协程可以实现高效的并发任务。

协程的本质就是在单线程下，由用户自己控制一个任务遇到io阻塞了就切换另外一个任务去执行，以此来提升效率。为了实现它，我们需要找寻一种可以同时满足以下条件的解决方案：

    1. 可以控制多个任务之间的切换，切换之前将任务的状态保存下来，以便重新运行时，可以基于暂停的位置继续执行。
    2. 作为1的补充：可以检测io操作，在遇到io操作的情况下才发生切换

协程：是单线程下的并发，又称微线程，纤程。英文名Coroutine。一句话说明什么是线程：协程是一种用户态的轻量级线程，即协程是由用户程序自己控制调度的。


需要强调的是：
    1. python的线程属于内核级别的，即由操作系统控制调度（如单线程遇到io或执行时间过长就会被迫交出cpu执行权限，切换其他线程运行）
    2. 单线程内开启协程，一旦遇到io，就会从应用程序级别（而非操作系统）控制切换，以此来提升效率（！！！非io操作的切换与效率无关）

对比操作系统控制线程的切换，用户在单线程内控制协程的切换

    优点如下：

        1. 协程的切换开销更小，属于程序级别的切换，操作系统完全感知不到，因而更加轻量级
        2. 单线程内就可以实现并发的效果，最大限度地利用cpu
    缺点如下：

        1. 协程的本质是单线程下，无法利用多核，可以是一个程序开启多个进程，每个进程内开启多个线程，每个线程内开启协程
        2. 协程指的是单个线程，因而一旦协程出现阻塞，将会阻塞整个线程

    总结协程特点：

        必须在只有一个单线程里实现并发
        修改共享数据不需加锁
        用户程序里自己保存多个控制流的上下文栈
        附加：一个协程遇到IO操作自动切换到其它协程（如何实现检测IO，yield、greenlet都无法实现，就用到了gevent模块（select机制））

'''

# 协程的两个模块  gevent 和 asyncio
# python3.5 引进了 asyncio 模块。因此主要理解asyncio模块
'''
event_loop 事件循环：程序开启一个无限的循环，程序员会把一些函数注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。

coroutine 协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。

task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。

future： 代表将来执行或没有执行的任务的结果。它和task上没有本质的区别

async/await 关键字：python3.5 用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。

'''

# 1.定义一个协程函数
import asyncio

async def do_some_work01(x):pass

def do_not_coroutine(x):pass
#判断某个方法或者函数是不是协程
#
# print(asyncio.iscoroutinefunction(do_some_work01))    # True
# print(asyncio.iscoroutinefunction(do_not_coroutine)) # False


# 2.运行一个简单的协程
'''
协程什么都没做，我们让它睡眠几秒，以模拟实际的工作量
在解释 await 之前，有必要说明一下协程可以做哪些事。协程可以：

    * 等待一个 future 结束
    * 等待另一个协程（产生一个结果，或引发一个异常）
    * 产生一个结果给正在等它的协程
    * 引发一个异常给正在等它的协程
asyncio.sleep 也是一个协程，所以 await asyncio.sleep(x) 就是等待另一个协程。
'''
# import asyncio
# import time
# count = 0
# async def  do_some_work02(x):
#     global count
#     count += 1
#     print("waitting:",x)
#     await asyncio.sleep(x)
#     print("over")
#
# now = lambda:time.time()
# start = now()
# loop = asyncio.get_event_loop()
# # print("future:",asyncio.ensure_future(do_some_work02(3)))
# # loop.run_until_complete(do_some_work02(5))
# # # loop.run_until_complete()
#
# for i in range(10):
#     asyncio.ensure_future(do_some_work02(i))
#
# loop.run_until_complete(do_some_work02(10))
# print("count:",count)
# print("total run time:",now()-start)
'''
run_until_complete 是一个阻塞（blocking）调用，直到协程运行结束，它才返回。这一点从函数名不难看出。
run_until_complete 的参数是一个 future，但是我们这里传给它的却是协程对象，之所以能这样，是因为它在内部做了检查，通过 ensure_future 函数把协程对象包装（wrap）成了 future。所以，我们可以写得更明显一些：
loop.run_until_complete(asyncio.ensure_future(do_some_work(3)))

'''

# 3.回调
'''
假如协程是一个 IO 的读操作，等它读完数据后，我们希望得到通知，以便下一步数据的处理。这一需求可以通过往 future 添加回调来实现。

注意回调函数必须和 future 搭配使用。
'''
# import  asyncio
#
# async def do_some_work03(x):
#     print("waiting:",x)
#     await asyncio.sleep(x)
#     print("over")
#
# def done_callback(futu):
#     print("done")
#     print("inner futu:",futu)   #inner futu: <Task finished coro=<do_some_work03() done, defined at ./05 协程.py:120> result=None>
#
# loop = asyncio.get_event_loop()
# futu = asyncio.ensure_future(do_some_work03(3))
# print("outter futu:",futu)          # outter futu: <Task pending coro=<do_some_work03() running at ./05 协程.py:120>>
# futu.add_done_callback(done_callback)
# loop.run_until_complete(futu)


# 4.运行多个协程的三种方法
'''实际项目中，往往有多个协程，同时在一个 loop 里运行。为了把多个协程交给 loop，需要借助 asyncio.gather 函数
# gather 起聚合的作用，把多个 futures 包装成单个 future，因为 loop.run_until_complete 只接受单个 future。
'''
import asyncio,time

async  def do_some_work04(x):
    print("waiting:",x)
    await asyncio.sleep(x)
    print("over")


def done_callback(futu):
    print("done")


now = lambda:time.time()
start = now()
loop = asyncio.get_event_loop()
#第一种方法：把全部协程写到 asyncio.gather里面
# futu = asyncio.ensure_future(asyncio.gather(do_some_work04(3),do_some_work04(2)))
# futu.add_done_callback(done_callback)
# loop.run_until_complete(futu)


# 第二种方法：可以把多个协程写到一个列表里面在使用 asyncio.gather 进行调用
# coros = [do_some_work04(1),do_some_work04(2),do_some_work04(3)]
# futu = asyncio.ensure_future(asyncio.gather(*coros))
# futu.add_done_callback(done_callback)
# loop.run_until_complete(futu)

# 第三种方法：把future对象写到 run_until_complete 中
# futus = [asyncio.ensure_future(do_some_work04(1)),asyncio.ensure_future(do_some_work04(2)),asyncio.ensure_future(do_some_work04(3))]
# for futu in futus:
#     futu.add_done_callback(done_callback)
# loop.run_until_complete(asyncio.gather(*futus))

print("run time：",now()-start)

loop.close()


# 协程实现
import requests
import time,os,random

import asyncio
# 获取网页，
async def get_page(url):
    print('<%s> is getting [%s]' %(os.getpid(),url))
    response=requests.get(url)
    # await asyncio.sleep(random.randint(1,4))
    return {'url':url,'text':response.text}
# 解析网页
def parse_page(res):
    res = res.result()
    print("res",res)
    print("<%s> parse [%s]"%(os.getpid(),res['url']))
    with open('content.txt','a') as f:
        parse_res = "[url]: %s [size]: %s\n"%(res['url'],len(res['text']))
        f.write(parse_res)

if __name__ == '__main__':
    urls = [
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://help.github.com/',
        'http://www.sina.com.cn/'
    ]
    now = lambda: time.time()
    start = now()
    loop = asyncio.get_event_loop()
    # 开启多个协程
    futus = []
    for i in urls:
        futu = asyncio.ensure_future(get_page(i))
        futus.append(futu)
    for futu in futus:
        futu.add_done_callback(parse_page)
    loop.run_until_complete(asyncio.gather(*futus))


    print("run time:",now()-start)

    loop.close()

















