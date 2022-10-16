#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """defining test case for the module  Max_integerlist[]"""

    def test_with_empty_list(self):
        """Test case with an empty list"""
        list0 = []
        self.assertEqual(max_integer(list0), None)

    def test_with_one_item(self):
        """Test case with a list of 1 item"""
        list1 = [9]
        self.assertEqual(max_integer(list1), 9)

    def test_with_ordered_list(self):
        """test with list which is ordered"""
        list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(max_integer(list2), 9)

    def test_with_unordered_list(self):
        """Test case with unordered list of int"""
        list3 = [7, 2, 6, 3, 8, 6, 4, 8, 10]
        self.assertEqual(max_integer(list3), 10)

    def test_with_floats(self):
        """Test case with ordered floats"""
        list4 = [12.3, 12.4, 12.7, 12.8, 12.9]
        self.assertEqual(max_integer(list4), 12.9)

    def test_with_floats_and_int(self):
        """Test case with floats and integers"""
        list5 = [7, 12.3, 12.4, 12.7, 12.8, 12.9, 19]
        self.assertEqual(max_integer(list5), 19)

    def test_with_list_string(self):
        """this is a test case with a list of single string"""
        list6 = ["samuel"]
        self.assertEqual(max_integer(list6), 'samuel')

    def test_with_a_list_string(self):
        """this is a test case with a single string"""
        list7 = "samuel"
        self.assertEqual(max_integer(list7), 'u')

    def test_with_a_string(self):
        """this is a test case with a single string"""
        list8 = ""
        self.assertEqual(max_integer(list8), None)

if __name__ == '__main__':
    unittest.main()