#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """ Add or update a value a dictionary entry
    """
    if a_dictionary is not None:
        a_dictionary[key] = value
    return a_dictionary
