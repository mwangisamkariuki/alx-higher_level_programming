#!/usr/bin/python3
"""Defines Module impliments Geometry
"""


class BaseGeometry:
    """represents a base Geometry"""

    def area(self):
        """Area Not Implimented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function to validate parameters as an int
        """
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
