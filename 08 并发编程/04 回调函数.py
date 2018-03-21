# -*- coding: utf-8 -*-

# __title__ = '04 回调函数.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.21'


# 可以为进程池或线程池内的每个进程或线程绑定一个函数，该函数在进程或线程的任务执行完毕后自动触发，并接收任务的返回值当作参数，该函数称为回调函数
# import requests
# import time,os,random
# from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
#
# # 获取网页，
# def get_page(url):
#     print('<%s> is getting [%s]' %(os.getpid(),url))
#     response=requests.get(url)
#     time.sleep(random.randint(1,7))
#     return {'url':url,'text':response.text}
# # 解析网页
# def parse_page(res):
#     res = res.result()
#     print("res",res)
#     print("<%s> parse [%s]"%(os.getpid(),res['url']))
#     with open('content.txt','a') as f:
#         parse_res = "[url]: %s [size]: %s\n"%(res['url'],len(res['text']))
#         f.write(parse_res)
#
# if __name__ == '__main__':
#     urls = [
#         'https://www.baidu.com',
#         'https://www.python.org',
#         'https://www.openstack.org',
#         'https://help.github.com/',
#         'http://www.sina.com.cn/'
#     ]
#     start = time.time()
#     # pool = ThreadPoolExecutor()
#     pool = ThreadPoolExecutor()
#     for url in urls:
#         pool.submit(get_page,url).add_done_callback(parse_page)
#     pool.shutdown()
#     print("主进程PID：%s,运行时间:%s"%(os.getpid(),time.time()-start))


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