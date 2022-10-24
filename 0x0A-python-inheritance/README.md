# 0x0A-python-inheritance - ALX Higher Learning

# Task 0: Look up
a function that returns the list of available attributes and methods of an object:
Prototype: def lookup(obj):
Returns a list object

# Task 1# Implimenting MyList() that inherits from list
Public instance method: def print_sorted(self): that prints the list,
but sorted (ascending sort)

# Task 2# Exact same object
Write a function that returns True if the object is exactly an instance of the specified class ;
otherwise False.
Prototype: def is_same_class(obj, a_class):

# Task 3: Same class or inherit from
rite a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
Prototype: def is_kind_of_class(obj, a_class):

# Task 4:Only a subclass
Prototype: def is_kind_of_class(obj, a_class):
Write a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
Prototype: def is_kind_of_class(obj, a_class):
You are not allowed to import any module

# Task 5:Geometry Module
Write an empty class of BaseGeometry
class BaseGeometry():

# Task 6:Improve Geometry
Write a class BaseGeometry (based on 5-base_geometry.py).
Public instance method: def area(self):
that raises an Exception with the message area() is not implemented
You are not allowed to import any module

# Task 7: Int Validator

# Task 8: Rectangle
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

# Task 9:
Write a class Rectangle that inherits from BaseGeometry(7-base_geometry.py).
(task based on 8-rectangle.py)
print() should print, and str() should return, the following rectangle description:
[Rectangle] <width>/<height>

# Task 10:Square #1
Write a class Square that inherits from Rectangle (9-rectangle.py):
Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented

# Task 11: Square #2
Write a class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).
Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
print() should print, and str() should return,
the square description: [Square] <width>/<height>


# Task 12:MyInt
Write a class MyInt that inherits from int:
MyInt is a rebel. MyInt has == and != operators inverted
You are not allowed to import any module

# Task 13:  Can I? hasattr()
Write a function that adds a new attribute to an object if it’s possible:
Raise a TypeError exception, with the message
can't add new attribute if the object can’t have new attribute
You are not allowed to use try/except
You are not allowed to import any module