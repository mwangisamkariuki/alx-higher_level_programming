#!/usr/bin/python3
""" A function that impliments write to file"""


def write_file(filename="", text=""):
    """writes a given string to a UTF* text File"""
    with open(filename, mode="w", encoding="utf-8") as MyFile:
        return MyFile.write(text)
