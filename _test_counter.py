import unittest
from counter import *

class TestCounter(unittest.TestCase):
    def setUp(self):
        @counter
        def func(key):
            return key

        self.func = func

        for x in range(5):
            for y in range(x):
                func(x)

    def tearDown(self):
        del self.func

    def test_func_zero_never_called(self):
        self.assertEqual(0, self.func.total_calls(0))

    def test_func_one_called_1x(self):
        self.assertEqual(1, self.func.total_calls(1))

    def test_func_two_called_2x(self):
        self.assertEqual(2, self.func.total_calls(2))

    def test_func_two_called_3x(self):
        self.assertEqual(3, self.func.total_calls(3))

    def test_func_two_called_4x(self):
        self.assertEqual(4, self.func.total_calls(4))

if __name__ == '__main__':
    unittest.main()
