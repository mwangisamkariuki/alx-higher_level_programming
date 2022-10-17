#!/usr/bin/python3
"""Module to find the area of an rectangle
"""


class Rectangle:
    """that defines a rectangle by: (based on 0-rectangle.py)"""
    def __init__(self, height=0, width=0):
        """a function that defines the arguments of a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
