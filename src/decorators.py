class Mixin(object):
    ''' A class decorator which allows you
        to mix in the properties of other
        classes without inheriting directly.

        **ONLY WORKS ON NEW STYLE CLASSES***

        Method resolution order is just like
        multiple inheritence.  Left takes
        precedence over right.

        Mixins are added to the class directly,
        so they take precedence over any regularly
        inherited superclasses.

        This requires copying of attributes,
        so any changes to the precedent classes
        will not be reflected in the child class.
    '''

    def __init__(self, *mixins):
        self.mixins = mixins

    def __call__(self, cls):
        dct = {}
        mcls = type(cls)
        name = cls.__name__
        bases = cls.__mro__
        for mix in reversed(self.mixins):
            for parent in reversed(mix.__mro__):
                dct.update(parent.__dict__)
            dct.update(mix.__dict__)
        dct.update(cls.__dict__)
        return type.__new__(mcls, name, bases, dct)
