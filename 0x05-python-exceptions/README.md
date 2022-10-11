#Task 0. Safe list printing
    Write a function that prints x elements of a list.
    Prototype: def safe_print_list(my_list=[], x=0):
    my_list can contain any type (integer, string, etc.)
    All elements must be printed on the same line followed by a new line.
    x represents the number of elements to print
    x can be bigger than the length of my_list
    Returns the real number of elements printed
    You have to use try: / except:
    You are not allowed to import any module
    You are not allowed to use len()
# Task 1: Safe printing of an integers list
    Write a function that prints an integer with "{:d}".format().
    Prototype: def safe_print_integer(value):
    value can be any type (integer, string, etc.)
    The integer should be printed followed by a new line
    Returns True if value has been correctly printed (it means the value is an integer)
    Otherwise, returns False
    You have to use try: / except:
    You have to use "{:d}".format() to print as integer
    You are not allowed to import any module
    You are not allowed to use type()
# Task 2:Print and count integerWrite a function that prints the first x elements of a list and only integers.
    Prototype: def safe_print_list_integers(my_list=[], x=0):
    my_list can contain any type (integer, string, etc.)
    All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
    x represents the number of elements to access in my_list
    x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur
    Returns the real number of integers printed
    You have to use try: / except:
    You have to use "{:d}".format() to print an integer
    You are not allowed to import any module
    You are not allowed to use len()
# Task 3:Integers division with debug
    Write a function that divides 2 integers and prints the result.
    Prototype: def safe_print_division(a, b):
    You can assume that a and b are integers
    The result of the division should print on the finally: section preceded by Inside result:
    Returns the value of the division, otherwise: None
    You have to use try: / except: / finally:
    You have to use "{}".format() to print the result
    You are not allowed to import any module
# Task 4:
# Task 5:Raise exception
    Write a function that raises a type exception.
    Prototype: def raise_exception():
    You are not allowed to import any module
# Task 6: Raise Message.
    Write a function that raises a name exception with a message.
    Prototype: def raise_exception_msg(message=""):
    You are not allowed to import any module

# Advanced tasks
# Task 7: Safe integer print with error message
    Write a function that prints an integer.
    Prototype: def safe_print_integer_err(value):
    value can be any type (integer, string, etc.)
    The integer should be printed followed by a new line
    Returns True if value has been correctly printed (it means the value is an integer)
    Otherwise, returns False and prints in stderr the error precede by Exception:
    You have to use try: / except:
    You have to use "{:d}".format() to print as integer
    You are not allowed to use type()
# Task 8:Safe function 
    Write a function that executes a function safely.
    Prototype: def safe_function(fct, *args):
    You can assume fct will be always a pointer to a function
    Returns the result of the function,
    Otherwise, returns None if something happens during the function and prints in stderr the error precede by Exception:
    You have to use try: / except: