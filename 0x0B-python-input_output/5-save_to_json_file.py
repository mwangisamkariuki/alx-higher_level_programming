#!/usr/bin/python3
"""Defines a JSON to file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON rep"""
    with open(filename, mode ="w") as MyFile:
        json.dump(my_obj, MyFile)
