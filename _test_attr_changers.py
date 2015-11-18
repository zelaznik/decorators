import unittest

from attr_changers import *

from math import atan

@attr_reader('x', 'y')
class Reader(object):
    def __init__(self, x, y):
        self.__x, self.__y = x,y
    def __abs__(self):
        return (self.__x**2+self.__y**2)**0.5
    @property
    def theta(self):
        return atan(self.y / self.x)

@attr_writer('x', 'y')
class Writer(object):
    def __abs__(self):
        return (self.__x**2+self.__y**2)**0.5
    @property
    def theta(self):
        return atan(self.y / self.x)

@attr_accessor('x', 'y')
class Accessor(object):
    def __abs__(self):
        return (self.__x**2+self.__y**2)**0.5
    @property
    def theta(self):
        return atan(self.y / self.x)

class test_attr_reader(unittest.TestCase):
    def setUp(self):
        self.r = Reader(3,4)

    def test_reader_private_attributes_readable_by_class(self):
        self.assertEqual(abs(self.r), 5)

    def test_reader_attributes_readable_from_outside(self):
        self.assertEqual(self.r.x, 3)
        self.assertEqual(self.r.y, 4)

    def test_reader_attributes_not_writeable_from_outside(self):
        self.assertRaises(AttributeError, setattr, self.r, 'x', 3)
        self.assertRaises(AttributeError, setattr, self.r, 'y', 4)

class test_attr_writer(unittest.TestCase):
    def setUp(self):
        w = Writer()
        w.x = 3
        w.y = 4
        self.w = w

    def test_writer_private_attributes_readable_by_class(self):
        self.assertEqual(abs(self.w), 5)

    def test_writer_attributes_not_readable_from_outside(self):
        self.assertRaises(AttributeError, getattr, self.w, 'x')
        self.assertRaises(AttributeError, getattr, self.w, 'y')

    def test_writer_attributes_writeable_from_outside(self):
        self.w.x = 0
        self.assertEqual(abs(self.w), 4)
        self.w.y = 0
        self.assertEqual(abs(self.w), 0)

class test_attr_accessor(unittest.TestCase):
    def setUp(self):
        a = Accessor()
        a.x = 3
        a.y = 4
        self.a = a

    def test_accessor_private_attributes_readable_by_class(self):
        self.assertEqual(abs(self.a), 5)

    def test_accessor_attributes_readable_from_outside(self):
        self.assertEqual(self.a.x, 3)
        self.assertEqual(self.a.y, 4)

    def test_accessor_attributes_writeable_from_outside(self):
        self.a.x = 0
        self.assertEqual(abs(self.a), 4)
        self.a.y = 0
        self.assertEqual(abs(self.a), 0)

if __name__ == '__main__':
    unittest.main()