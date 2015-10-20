import unittest
from functools import wraps
from memoize import *
from counter import *

class TestMemoize(unittest.TestCase):
    def setUp(self):
        @memoize
        @counter
        def fib(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fib(n-2) + fib(n-1)

        fib(20)
        fib(20)
        self.fib = fib

    def test_fib_receives_five_one_time(self):
        self.assertEqual(1, self.fib.total_calls(5))

    def test_fib_receives_thirty_zero_times(self):
        self.assertEqual(0, self.fib.total_calls(30))

if __name__ == '__main__':
    unittest.main()
