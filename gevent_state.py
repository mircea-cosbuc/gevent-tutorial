import gevent


def win():
    return 'You win!'


def fail():
    raise Exception('You win at failing.')


winner = gevent.spawn(win)
loser = gevent.spawn(fail)

# Has the greenlet started?
print(winner.started)
print(loser.started)

# Exceptions raised in the Greenlet, stay inside the Greenlet.
try:
    gevent.joinall([winner, loser])
except Exception as e:
    print('This will never be reached')

# What value does the greenlet return?
print(winner.value)
print(loser.value)

# Has the greenlet finish executing instructions?
print(winner.ready())
print(loser.ready())

# Has the greenlet finished execution successfully?
print(winner.successful())
print(loser.successful())

# Access exceptions raised inside the greenlet
print(winner.exception)
print(loser.exception)

raise loser.exception
