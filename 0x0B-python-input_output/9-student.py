#!/usr/bin/python3
#!/usr/bin/python3
"""impliments student to json"""


class Student:
    """Represent a student."""


    def __init__(self, first_name, last_name, age):
        """initialize an new student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self):
        """retrienves a dictionary repr of a student instance"""
        return self.__dict__
