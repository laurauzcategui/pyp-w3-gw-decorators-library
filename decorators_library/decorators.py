# implement your decorators here.
import functools

def inspect(fn):
    @functools.wraps(fn)
    def wrapper(a,b):
        print("{} invoked with {} {}".format(fn.__name__, a, b))
        fn(a,b)
    return wrapper

@inspect
def my_add(a, b):
    return a + b

my_add(3, 5)

def timeout(fn):
    pass

def memoized(fn):
    pass
