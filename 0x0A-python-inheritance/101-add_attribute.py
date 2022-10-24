#!/usr/bin/python3
"""Defines a modult which adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
