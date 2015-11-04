def well_behaved(dec):
    ''' Makes sure that the wrapped functions still look like
       the original, with the same name, docs, and modules.
    '''
    def you_will_never_see_this_name(orig_func):
        new_func = dec(orig_func)
        new_func.__doc__ = orig_func.__doc__
        new_func.__name__ = orig_func.__name__
        new_func.__module__ = orig_func.__module__
        return new_func

    you_will_never_see_this_name.__module__ = dec.__module__
    you_will_never_see_this_name.__name__ = dec.__name__
    you_will_never_see_this_name.__doc__ = dec.__doc__
    return you_will_never_see_this_name
