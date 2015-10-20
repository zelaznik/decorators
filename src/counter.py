from collections import defaultdict

def counter(func):
    ''' Records the nubmer of times a function was called. '''

    ct = defaultdict(int)

    def total_calls(key):
        return ct[key]

    @wraps(func)
    def counted(key):
        ct[key] += 1
        return func(key)

    counted.total_calls = total_calls
    return counted

__all__ = ['counter']
