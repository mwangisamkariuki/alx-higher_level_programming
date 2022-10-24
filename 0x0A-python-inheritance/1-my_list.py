#!/usr/bin/python3
"""A module that contains a list"""


class MyList(list):
    """pints a sorted list"""

    def print_sorted(self):
        """prints a list sorted in ascending order"""

        self.list = list
        if len(self) <= 1:
            return None
        else:
            print(sorted(self))
