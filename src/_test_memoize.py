import unittest
from collections import defaultdict
from functools import wraps
from memoize import *

def count_calls(func):
    ct = defaultdict(int)

    @wraps(func)
    def counted(key):
        ct[key] += 1
        return func(key)
    


class TestMemoize(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
