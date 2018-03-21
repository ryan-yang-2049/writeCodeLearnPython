# -*- coding: utf-8 -*-

# __title__ = '06 生产者消费者模型.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.21'


'''
1.yield 实现生产者消费者模型
2.多进程/多线程实现生产者消费者模型
3.协程实现生产者消费者模型

'''

# yield 实现生产者消费者模型

def init(func):
    def wrapper(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)     # 或者  g.send(None)
        return g
    return wrapper

@init
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            print("not n...")
            return
        print('3==>[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    n = 0
    while n < 2:
        n += 1
        print('1==>[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('2==>[PRODUCER] Consumer return: %s' % r)
    c.close()

# produce(consumer())

# 进程实现生产者消费者模型
# 有几个消费者，就要发送几个None的信号
# from multiprocessing import Process,Queue
# import os,time,random
# def consumer(q):
#     while True:
#         res = q.get()
#         if res is None:break        #  取数据，如果消费者收到None的值（信号），就结束该线程
#         time.sleep(random.randint(1,3))
#         print("\033[45m %s 消费了 %s \033[0m" % (os.getpid(), res))
#
# def producer(product,q):
#     for i in range(5):
#         time.sleep(2)
#         res = '%s%s'%(product,i)
#         q.put(res)
#         print("\033[44m %s 生产了  %s \033[0m"%(os.getpid(),res))
# # q.put(None) # 发送信号到队列里面，表示该线程（生产者）已经结束。
#
# if __name__ == '__main__':
#     q = Queue() #存保证的容器
#     # 生产者
#     p1 = Process(target=producer,args=('包子',q))
#     p2 = Process(target=producer,args=('馒头',q))
#     p3 = Process(target=producer,args=('烧卖',q))
#     # 消费者
#     c1 = Process(target=consumer,args=(q,))
#     c2 = Process(target=consumer,args=(q,))
#     p_l = [p1,p2,p3]
#     c_l = [c1,c2]
#     p1.start()
#     p2.start()
#     p3.start()
#
#     c1.start()
#     c2.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#     q.put(None)
#     q.put(None)
#     c1.join()
#     c2.join()
#     print("主")


# 协程实现生产者消费者模型
import asyncio
import random
async def producer(queue, n):
    for x in range(n):
        # produce an item
        print('producing {}/{}'.format(x, n))
        # simulate i/o operation using sleep
        await asyncio.sleep(random.random())
        item = str(x)
        # put the item in the queue
        await queue.put(item)
async def consume(queue):
    while True:
        # wait for an item from the producer
        item = await queue.get()
        # process the item
        print('consuming {}...'.format(item))
        # simulate i/o operation using sleep
        await asyncio.sleep(random.random())
        # Notify the queue that the item has been processed
        queue.task_done()
async def run(n):
    queue = asyncio.Queue()
    # schedule the consumer
    consumer = asyncio.ensure_future(consume(queue))
    # run the producer and wait for completion
    await producer(queue, n)
    # wait until the consumer has processed all items
    await queue.join()
    # the consumer is still awaiting for an item, cancel it
    consumer.cancel()



loop = asyncio.get_event_loop()
loop.run_until_complete(run(10))
loop.close()