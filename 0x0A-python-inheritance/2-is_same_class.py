#!/usr/bin/python3
"""this Module checks if obj is an instance
of an inherited classclass"""


def is_kind_of_class(obj, a_class):
    """ Check if obj is an instance of a given class
    Returns True if yes otherwise false
    """
    if type(obj) == a_class:
        return True
    return False
