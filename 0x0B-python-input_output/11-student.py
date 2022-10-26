#!/usr/bin/python3
"""impliments student to json"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """initialize an new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrienves a dictionary repr of a student instance
        if attrs is a list of strings, represents only those attributes
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.
        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
