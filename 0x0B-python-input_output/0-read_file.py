#!/usr/bin/python3
"""Module that impliments  file handling"""


def read_file(filename=""):
    """reads a text files and prints it to stdout"""
    with open(filename, encoding="utf-8") as MyFile:
        print(MyFile.read())
