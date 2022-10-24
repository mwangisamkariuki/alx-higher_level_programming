#!/usr/bin/python3
"""this Module checks if obj is an instance
of a given class"""


def is_kind_of_class(obj, a_class):
    """ Check if obj is of type a_class
    """
    if isinstance(obj, a_class):
        return True
    return False
