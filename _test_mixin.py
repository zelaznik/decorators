import unittest
from collections import MutableMapping, OrderedDict
from mixin import *
from abc import ABCMeta, abstractmethod

try:
    from abc import ABC
except ImportError:
    ABC = ABCMeta('ABC', (), {})

class Blah(object):
    def display(self):
        return 'NotImplemented'

class Foo(object):
    def __eq__(self, other):
        return 'NotImplemented'

    def bar(self):
        return 'bar'

    def display(self):
        return "Hi"

class ArbitraryAbstract(ABC):
    @abstractmethod
    def does_not_matter(self):
        raise NotImplementedError

@Mixin(ArbitraryAbstract, MutableMapping, Foo, Blah)
class LRUCache(ABC):
    def __init__(self, limit = 4):
        self.__limit = limit
        self.__d = OrderedDict()

    def __len__(self):
        return len(self.__d)

    def __iter__(self):
        return iter(self.__d)

    def __getitem__(self, key):
        return self.__d[key]

    def __delitem__(self, key):
        del self.__d[key]

    def __setitem__(self, key, val):
        try:
            del self[key]
        except KeyError:
            pass
        self.__d[key] = val
        self.__trim()

    def __trim(self):
        while len(self) > self.limit:
            for key in self:
                del self[key]
                break

    def __eq__(self, other):
        return self is other

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, val):
        self.__limit = val
        self.__trim()

    def __repr__(self):
        cls = self.__class__.__name__
        args = (cls, self.limit, list(self.items()))
        return '%s(limit=%d, items=%r)' % args

class TestMixin(unittest.TestCase):
    def setUp(self):
        self.lru = LRUCache()
        self.foo = Foo()

    def tearDown(self):
        del self.lru

    def test_LRUCache_is_ABCMeta(self):
        self.assertEqual(type(LRUCache), ABCMeta)

    def test_LRUCache_items_is_MutabelMapping_items(self):
        self.assertEqual(LRUCache.items, MutableMapping.items)

    def test_LRUCache_display_returns_Foo_display(self):
        self.assertEqual(self.lru.display(), self.foo.display())

if __name__ == '__main__':
    unittest.main()
