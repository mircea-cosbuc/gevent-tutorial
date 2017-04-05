from urllib.request import urlopen

import gevent
import gevent.monkey
import simplejson as json

gevent.monkey.patch_socket()


def fetch(pid):
    response = urlopen('https://hangyman.herokuapp.com/')
    result = response.read()
    json_result = json.loads(result)
    puzzle = json_result['puzzle']

    print('Process %s: %s' % (pid, puzzle))
    return json_result['tries']


def synchronous():
    for i in range(1, 10):
        fetch(i)


def asynchronous():
    threads = []
    for i in range(1, 10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)


print('Synchronous:')
synchronous()

print('Asynchronous')
asynchronous()
