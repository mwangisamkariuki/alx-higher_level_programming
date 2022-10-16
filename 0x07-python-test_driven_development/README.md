# TEST DRIVEN DEVELOPMENT
# Task 0: Integers addition
    Write a function that adds 2 integers.
    Prototype: def add_integer(a, b=98):
    a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
    You are not allowed to import any module

# Task 1 skipped (Not available on ALX)
# Task  2.Divide a matrix
    Write a function that divides all elements of a matrix.
    Prototype: def matrix_divided(matrix, div):
    matrix must be a list of lists of integers or floats,
    otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
    Each row of the matrix must be of the same size,
    otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
    div must be a number (integer or float),
    otherwise raise a TypeError exception with the message div must be a number
    div can’t be equal to 0,
    otherwise raise a ZeroDivisionError exception with the message division by zero
    All elements of the matrix should be divided by div, rounded to 2 decimal places
    Returns a new matrix
    You are not allowed to import any module

# Task 3. Write a function that prints My name
    Write a function that prints My name is <first name> <last name>
    Prototype: def say_my_name(first_name, last_name=""):
    first_name and last_name must be strings otherwise, 
	raise a TypeError exception with the message,
	 first_name must be a string or last_name must be a string
    You are not allowed to import any module
# Task 4.Text Identation
	Write a function that prints a text with 2 new lines after
	each of these characters .,? and :
	prototype: def text_identation(text)
	text must be a string
	There should be no space at teh start or at the end of each printed line
# Task 5. Max Int- unittest NOT Interractive test
    Since the beginning you have been creating “Interactive tests”.
    For this exercise, you will add Unittests.
    In this task, you will write unittests for the function def max_integer(list=[]):.
    Your test file should be inside a folder tests
    You have to use the unittest module
    Your test file should be python files (extension: .py)
    Your test file should be executed by using this command: 
    python3 -m unittest tests.6-max_integer_test
    All tests you make must be passable by the function below
    We strongly encourage you to work together on test cases,
    so that you don’t miss any edge case
    
# Task 6: unittest()
Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function def max_integer(list=[]):.

Your test file should be inside a folder tests
You have to use the unittest module
Your test file should be python files (extension: .py)
Your test file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
All tests you make must be passable by the function below
We strongly encourage you to work together on test cases, so that you don’t miss any edge case