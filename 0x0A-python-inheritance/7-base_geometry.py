#!/usr/bin/python3
"""the Module impliments Geometry"""


class BaseGeometry:
    """This class defines  base Geometry"""

    def area(self):
        """Area Not Implimented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function to validate parameters as an Int
        TypeError if Value is not an Int
        """
        self.name = name
        self.value = value

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
