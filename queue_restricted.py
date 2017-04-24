import gevent
from gevent.queue import Empty, Queue

tasks = Queue(maxsize=3)


def worker(name):
    try:
        while True:
            task = tasks.get(timeout=1)
            print("Worker {} got task {}".format(name, task))
            gevent.sleep(0)
    except Empty:
        print("Quitting time!")


def boss():
    """
    Boss will wait until an individual worker is free
    since the maxsize of the task queue is 3.
    """
    for i in range(1, 10):
        tasks.put(i)
    print("Assigned all work in iteration 1")

    for i in range(10, 20):
        tasks.put(i)
    print("Assigned all work in iteration 2")


gevent.joinall([
    gevent.spawn(boss),
    gevent.spawn(worker, 'steve'),
    gevent.spawn(worker, 'john'),
    gevent.spawn(worker, 'bob')
])
