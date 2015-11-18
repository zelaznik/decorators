def _attr_or_property(cls, name):
    try:
        return getattr(cls, name)
    except AttributeError:
        return property()

def attr_reader(*attribute_names):
    ''' Class decorator:
        Adds a read-only way to access the equivalent
        private methods of the underlying class. '''
    from operator import attrgetter
    def maker(cls, name):
        private = '_%s__%s' % (cls.__name__, name)
        return attrgetter(private)

    def _attr_reader(cls):
        for name in attribute_names:
            obj = _attr_or_property(cls, name)
            fget = maker(cls, name)
            setattr(cls, name, obj.getter(fget))
        return cls
    return _attr_reader

def attr_writer(*attribute_names):
    ''' Class decorator:
        Adds a write-only way to access the equivalent
        private methods of the underlying class.
    '''
    def maker(cls, name):
        private = '_%s__%s' % (cls.__name__, name)
        def fset(self, value):
            setattr(self, private, value)
        return fset
    
    def _attr_reader(cls):
        for name in attribute_names:           
            obj = _attr_or_property(cls, name)
            fset = maker(cls, name)
            setattr(cls, name, obj.setter(fset))
        return cls
    return _attr_reader

def attr_accessor(*attribute_names):
    ''' Class decorator:
        Combines attr_reader and attr_writer
    '''
    def _attr_accessor(cls):
        cls = attr_reader(*attribute_names)(cls)
        cls = attr_writer(*attribute_names)(cls)
        return cls
    return _attr_accessor

@attr_reader('x', 'y')
class Reader(object):
    def __init__(self, x, y):
        self.__x, self.__y = x,y
    def __abs__(self):
        return (self.x**2+self.y**2)**0.5

@attr_writer('x', 'y')
class Writer(object):
    def __abs__(self):
        return (self.__x**2+self.__y**2)**0.5

from math import atan
@attr_accessor('x', 'y')
class Accessor(object):
    def __abs__(self):
        return (self.__x**2+self.__y**2)**0.5        
    r = property(__abs__)
    @property
    def theta(self):
        return atan(self.y / self.x)