#!/usr/bin/env python
# -*- coding: utf8 -*-
import threading
import Queue
import traceback


class Worker(threading.Thread):
    def __init__(self, queue, worker_id, task, pool, timeout=0):
        threading.Thread.__init__(self)
        self.queue = queue
        self.id = worker_id
        self.task = task
        self.pool = pool
        self.timeout = timeout

    def run(self):
        while 1:
            try:
                data = self.queue.get(timeout=self.timeout)
                print ("worker %s is processing", self.id)
            except:
                print ("worker %s timeout", self.id)
                if self.pool.join_all:
                    break
            else:
                try:
                    self.task(data)
                    self.queue.task_done()
                except Exception, e:
                    print ("Worker %s failed", self.id)
                    print(traceback.format_exc())


class Pool(object):
    """ 创建一个有threads数目线程的线程池，通过从queue内获取数据来执行task
        如果timeout为0，则直接执行。
        join函数用来回收，如果不join则死循环继续
        work用来创建并开始
        put用来放置数据
    """
    def __init__(self, task, threads=10, timeout=0):
        self.queue = Queue.Queue()
        self.workers = []
        if threads <= 0:
            threads = 1
        self.threads = threads
        self.task = task
        self.timeout = timeout
        self.join_all = False

    def work(self):
        """ 开启threads数目的进程，把task赋予进程并运行
        """
        for i in range(self.threads):
            self.workers.append(Worker(self.queue, i, self.task, self,
                                       timeout=self.timeout))
        for worker in self.workers:
            worker.start()

    def join(self):
        """ 回收进程，进程通过判断join来实现跳出死循环
        """
        self.join_all = True
        for i in range(self.threads):
            print("worker %s joining"% i)
            self.workers[i].join()

    def put(self, data):
        """ 向queue内放置数据
        """
        self.queue.put(data)


if __name__ == '__main__':
    import time
    def task(t):
        print t

    p = Pool(task, threads=3, timeout=10)
    p.work()
    start_time = time.time()
    p.put(10)
    time.sleep(1)
    p.put(20)
    time.sleep(1)
    p.put(30)
    time.sleep(1)
    p.put(40)
    time.sleep(1)
    p.put(50)
    time.sleep(1)
    p.put(60)
    time.sleep(1)
    p.join()
    end_time = time.time()
    print end_time - start_time


