from gevent import sleep
from gevent.lock import BoundedSemaphore
from gevent.pool import Pool

sem = BoundedSemaphore(2)


def worker1(n):
    sem.acquire()
    print("Worker {} acquired semaphore".format(n))
    sleep(0)
    sem.release()
    print("Worker {} released semaphore".format(n))


def worker2(n):
    with sem:
        print("Worker {} acquired semaphore".format(n))
        sleep(0)
    print("Worker {} released semaphore".format(n))


pool = Pool()
pool.map(worker1, range(0, 2))
pool.map(worker2, range(3, 6))
