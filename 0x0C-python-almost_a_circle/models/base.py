#!/usr/bin/python3
"""defines a model of class Base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

