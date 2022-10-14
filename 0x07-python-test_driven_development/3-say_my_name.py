#!/bin/bash/python3


def say_my_name(first_name, last_name=""):
    """
    a function that prints my name
    Args: first_name and Last_name
    TypeError: Both Names must be string
    """
    if(not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if(not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
