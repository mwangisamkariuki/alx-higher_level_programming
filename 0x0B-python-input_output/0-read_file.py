#!/usr/bin/python3
"""Defines a function hat reads a file"""


def read_file(filename=""):
    """prints text file content in utf-8 to the stdout"""
    with open(filename, encoding="utf-8") as MyFile:
        print(MyFile.read(), end="")
