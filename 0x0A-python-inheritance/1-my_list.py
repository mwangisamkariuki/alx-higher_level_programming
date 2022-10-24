#!/usr/bin/python3
"""A module that contains a list"""


class MyList(list):
    """pints a sorted list"""

    def print_sorted(self):
        """prints a list sorted in ascending order"""
        print(sorted(self))
