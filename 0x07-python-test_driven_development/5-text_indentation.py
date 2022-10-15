#!/usr/bin/python3


"""
Text identation function that prints
text with 2 new lines after each of defined characters
"""


def text_indentation(text):
    """
    defining text_Identation
    Args:
        text(str): this is the text to print
    Raises:
        TypeError("text must be a string")
    """
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    panctuation = ".?:"
    new_line = ("\n")
    c = 0

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in panctuation:
            if text[c] in panctuation:
                print("\n")
            c += 1
        c += 1
