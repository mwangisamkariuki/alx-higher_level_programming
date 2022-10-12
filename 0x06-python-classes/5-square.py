#!/usr/bin/python3

"""Defining a class Square."""


class Square:
    """This is the starting point of a class"""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the a new square instance.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size to the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current square area"""
        result = self.__size * self.__size
        return (result)

    def my_print(self):
        """This method prints to the stdout the
        square with character
        """
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
