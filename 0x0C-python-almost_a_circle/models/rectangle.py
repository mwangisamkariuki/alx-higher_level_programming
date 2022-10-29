#!/usr/bin/python3
"""Defines a Model-of a rectangle"""
from models.base import Base


class Rectangle(Base):
    """represents a rectangle prototye"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes a new rectangle

        Args:
            width (int): represents the width of the rectangle
            height (int): the height of the rectangle
            x (int): left attribute
            y (int): right attribute
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """sets/gets the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """sets/gets the width of the rectangle"""
        return self.__height

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of a rectangle"""
        return self.height * self.width

    def display(self):
        """prints the reactangle on the stdout using #"""
        if self.width == 0 or self.width == 0:
            print("")
            return
        
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
            """Return the print() and str() representation of the Rectangle."""
            return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.x, self.y,
                                                        self.width, self.height)