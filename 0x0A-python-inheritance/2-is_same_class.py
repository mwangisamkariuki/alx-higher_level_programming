#!/usr/bin/python3
"""this Module checks if obj is an instance
of a given class"""


def is_same_class(obj, a_class):
    """ Check if obj is of type a_class
    """
    if type(obj) == a_class:
        return True
    return False
