#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

from max_file import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer_empty_list(self):
        """doc"""
        self.assertIsNone(max_integer([]))

    def test_max_integer_single_element(self):
            """doc"""
        self.assertEqual(max_integer([5]),  5)

    def test_max_integer_multiple_elements(self):
        """doc"""
        self.assertEqual(max_integer([1,  2,  3,  4]),  4)

    def test_max_integer_negative_numbers(self):
        """doc"""
        self.assertEqual(max_integer([-1, -2, -3,  4]),  4)

    def test_max_integer_non_integer_values(self):
        """doc"""
        with self.assertRaises(ValueError):
            max_integer([1, "two",  3])

if __name__ == '__main__':
    unittest.main()
