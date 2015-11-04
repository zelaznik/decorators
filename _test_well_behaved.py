import unittest
from well_behaved import *
from memoize import *
from math import sqrt

well_behaved_memoize = well_behaved(memoize)
memo_square_root = well_behaved_memoize(sqrt)

class TestWellBehaved(unittest.TestCase):
    def test_decorator_name_equals_orig(self):
        self.assertEqual(well_behaved_memoize.__name__, memoize.__name__)

    def test_decorator_doc_equals_orig(self):
        self.assertEqual(well_behaved_memoize.__doc__, memoize.__doc__)

    def test_decorator_module_equals_orig(self):
        self.assertEqual(well_behaved_memoize.__module__, memoize.__module__)

    def test_function_name_equals_orig(self):
        self.assertEqual(memo_square_root.__name__, sqrt.__name__)

    def test_function_doc_equals_orig(self):
        self.assertEqual(memo_square_root.__doc__, sqrt.__doc__)

    def test_function_module_equals_orig(self):
        self.assertEqual(memo_square_root.__module__, sqrt.__module__)

if __name__ == '__main__':
    unittest.main()
