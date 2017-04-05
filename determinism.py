import time
from multiprocessing.pool import Pool as MPool

from gevent.pool import Pool as GPool


def echo(i):
    time.sleep(0.001)
    return i

p = MPool(10)
run1 = [a for a in p.imap_unordered(echo, range(10))]
run2 = [a for a in p.imap_unordered(echo, range(10))]
run3 = [a for a in p.imap_unordered(echo, range(10))]
run4 = [a for a in p.imap_unordered(echo, range(10))]

print(run1 == run2 == run3 == run4)

p = GPool(10)
run1 = [a for a in p.imap_unordered(echo, range(10))]
run2 = [a for a in p.imap_unordered(echo, range(10))]
run3 = [a for a in p.imap_unordered(echo, range(10))]
run4 = [a for a in p.imap_unordered(echo, range(10))]

print(run1 == run2 == run3 == run4)
