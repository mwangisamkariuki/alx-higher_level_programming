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

# advanced Tasks
# Task 7:
    ```python
    Write a function that multiplies 2 matrices:

    Read: Matrix multiplication - only Matrix product (two matrices)

    Prototype: def matrix_mul(m_a, m_b):

    m_a and m_b must be validated with these requirements in this order

    m_a and m_b must be an list of lists of integers or floats:

    if m_a or m_b is not a list: raise a TypeError exception with the message m_a must be a list or m_b must be a list
    if m_a or m_b is not a list of lists: raise a TypeError exception with the message m_a must be a list of lists or m_b must be a list of lists
    if m_a or m_b is empty (it means: = [] or = [[]]): raise a ValueError exception with the message m_a can't be empty or m_b can't be empty
    if one element of those list of lists is not an integer or a float: raise a TypeError exception with the message m_a should contain only integers or floats or m_b should contain only integers or floats
    if m_a or m_b is not a rectangle (all ‘rows’ should be of the same size): raise a TypeError exception with the message each row of m_a must be of the same size or each row of m_b must be of the same size
    If m_a and m_b can’t be multiplied: raise a ValueError exception with the message m_a and m_b can't be multiplied

    You are not allowed to import any module
```
# Task 8: Lazy matrix multiplication
write a functionthat multiplies 2 matrices using the Numpy
to isntall it: pip3 install numpy == 1.15.0