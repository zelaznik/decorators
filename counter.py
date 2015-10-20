from collections import defaultdict
from functools import wraps

def counter(func):
    ''' Records the nubmer of times a function was called. '''

    ct = defaultdict(int)

    def key(*args, **kw):
        return (args, frozenset(kw.items()))

    def total_calls(*args, **kw):
        return ct[key(*args, **kw)]

    @wraps(func)
    def counted(*args, **kw):
        ct[key(*args, **kw)] += 1
        return func(*args, **kw)

    counted.total_calls = total_calls
    return counted

__all__ = ['counter']
