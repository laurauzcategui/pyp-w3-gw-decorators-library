# implement your decorators here.
import functools
import signal
import time
from .exceptions import FunctionTimeoutException
from .exceptions import MyCoolException

def inspect(fn):
    #@functools.wraps(fn)
    def wrapper(*args,**kwargs):
        list_args = [str(arg) for arg in args]
        func_name = fn.__name__
        result = fn(*args,**kwargs)
        print("{} invoked with {}. Result: {}").format(func_name, ','.join(list_args), result)
        return fn(*args,**kwargs)
    return wrapper


class timeout(object):
    def __init__(self, alarm, exception=FunctionTimeoutException):
        self.alarm = alarm
        self.exception = exception

    def __call__(self, fn, *args, **kwargs):

        def receive_alarm(signum, stack):
            time.ctime()
            raise self.exception("Function call timed out")

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, receive_alarm)
            signal.alarm(self.alarm)

            return fn(*args, **kwargs)
        return wrapper


def memoized(fn):
    pass

class counters(object):
    counter = 0


def count_calls(fn):
    @functools.wraps(fn)
    def wrapper():
        counters.counter += 1
        fn()
    return wrapper
