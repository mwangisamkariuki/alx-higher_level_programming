#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from Dynamcaaly creating a new instance attributes
    except if the new instance attributes.
    """

    __slots__ = ["first_name"]
