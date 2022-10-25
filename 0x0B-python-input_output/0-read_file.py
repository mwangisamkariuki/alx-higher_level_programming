#!/usr/bin/python3
"""Impliments  file handling"""


def read_file(filename=""):
    """reads a text files and prints it to stdout"""
    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="\n")