from time import time

def timer(func, *args, **kwargs):
    """Decorator to time the call of a function"""
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print(f'{func.__name__}({args=}, {kwargs=}) executed in {after - before} s')
        return rv
    return f

def counter(func, *args, **kwargs):
    """Decorator that counts the number of calls to a function"""
    func._count = 0
    def f(*args, **kwargs):
        rv = func(*args, **kwargs)
        func._count += 1
        print(f'{func.__name__}({args=}, {kwargs=}) has been called {func._count} times')
        return rv
    return f
