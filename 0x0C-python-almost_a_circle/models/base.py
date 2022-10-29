#!/usr/bin/python3
"""defines a model of class Base"""


class Base:
    """represents the Model-Base
    attributes:
        __nb_objects(int)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initilialize a new base instance"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
