#!/usr/bin/python3
"""Defines a Rectangle and its (square)."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """print method"""
        return "[{}] {}/{}" \
            .format(__class__.__name__, self.__size, self.__size)
