#!/usr/bin/python3
"""
This is a simple module That takes 2 parameters, 
adds and returns the results of the params of int type

"""

def add_integer(a, b=98):
    """
    Return the sum of two int and Raise:TypeError if either of a or b is not int or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError ("a must be an integer")
    if((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError ("b must be an integer")
    return (int(a) + int(b))
