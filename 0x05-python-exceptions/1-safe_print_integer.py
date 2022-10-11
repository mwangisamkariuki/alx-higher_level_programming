#!/usr/bin/python3
def safe_print_integer(value):

    """print an Integer with "{:d}".format().
    Returns:
        TypeError when Int found is- False
        Prints the Int if int found is -True
    """

    try:
        print("{:d}".format(value))
        return (True)
    except ValueError:
        return (False)
