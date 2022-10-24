#!/usr/bin/python3
"""A Module that returns  a list of available
attributes and methods of a class
"""


def lookup(obj):
    """
    this sunction returns  a list of available objects
    attributes
    """

    return(dir(obj))
