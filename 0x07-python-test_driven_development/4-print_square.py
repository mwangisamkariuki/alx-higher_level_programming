#!/usr/bin/python3
"""defines square printing of size (size) using #"""


def print_square(size):
    """
    print a square of length (size)
    usng #
    Args:
        Size (int):width and height
    Raise:
        TypeError: size must be integer
        ValueError: if size is less than 0
    """
    if(not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if(size < 0):
        raise ValueError("size must be >=0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
