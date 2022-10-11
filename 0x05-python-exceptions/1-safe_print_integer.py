#!/usr/bin/python3
def safe_print_integer(value):

    """print an Integer with "{:d}".format().
    Returns:
        TypeError when Int found is- False
        Prints the Int if int found is -True
    """

    try:
        print("{:d}".format(value), end="\n")
        return (True)
    except (TypeError, ValueError):
        return (False)
