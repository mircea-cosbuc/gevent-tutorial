import signal

import gevent


def run_forever():
    gevent.sleep(1000)


if __name__ == '__main__':
    # react to SIGQUIT, otherwise long running greenlets can
    # only be stopped from the outside
    gevent.signal(signal.SIGQUIT, gevent.kill)
    thread = gevent.spawn(run_forever)
    thread.join()
