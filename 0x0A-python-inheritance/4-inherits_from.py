#!/usr/bin/python3
"""this Module checks if obj is an instance
of a given class"""


def inherits_from(obj, a_class):
    """ Check if obj is of type a_class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
