
"""This Module impliments Geometry"""


class BaseGeometry:
    """This class impliments Geometry"""

    def area(self):
        """Not Implimented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function to validate parameters as an Int
        TypeError if Value is not an Int"""
        self.name = name
        self.value = value

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class rectangle inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Intialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
