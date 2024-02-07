#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

class TestMaxInteger(unittest.TestCase):
    def test_max_integer_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer_single_element(self):
        self.assertEqual(max_integer([5]),  5)

    def test_max_integer_multiple_elements(self):
        self.assertEqual(max_integer([1,  2,  3,  4]),  4)

    def test_max_integer_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3,  4]),  4)

    def test_max_integer_non_integer_values(self):
        with self.assertRaises(ValueError):
            max_integer([1, "two",  3])

if __name__ == '__main__':
    unittest.main()
