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

    @classmethod
    def save_to_file(cls, list_objs):
        """function that writes the json string to file"""

        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                file.write(Base.to_json_string(list_dicts))


    @staticmethod
    def from_json_string(json_string):
        """a function that returns the list of JSON string rep"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)      

    @classmethod
    def create(cls, **dictionary):
        """returns an instance already set attributes*"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new






                

