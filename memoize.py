from functools import wraps

def memoize(func):
    ''' Stores the results of function calls in a dictionary. '''
    cache = {}
    @wraps(func)
    def _memoize(*args, **kw):
        key = (args, frozenset(kw.items()))
        if key in cache:
            return cache[key]
        val = func(*args, **kw)
        cache[key] = val
        return val
    return _memoize

__all__ = ['memoize']
