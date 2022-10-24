#!/usr/bin/python3
"""defines a module MyList that inheritslist"""


class MyList(list):
    """prints a sorted list"""

    def print_sorted(self):
        """prints a list sorted in ascending order"""
        print(sorted(self))
