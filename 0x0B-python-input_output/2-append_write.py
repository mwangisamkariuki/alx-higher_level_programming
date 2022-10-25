#!/usr/bin/python3
""" A function that impliments append to file"""


def append_write(filename="", text=""):
    """appends a given string to a UTF* text File"""
    with open(filename, mode="a", encoding="utf-8") as MyFile:
        return MyFile.write(text)
