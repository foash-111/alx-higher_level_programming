#!/usr/bin/python3
"""Defines a class TestMaxInteger for max_integer([...])"""


import unittest
max_integer = import('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test class that defines test cases for the max_integer function.
    """
    def test_positive_integers(self):
        """Test for positive integers
        """
        test_list1 = [1, 2, 3, 4]
        test_list2 = [ 4, 1, 2, 3]
        test_list3 = [1, 2, 4, 2, 3]

        self.assertEqual(max_integer(test_list1), 4)
        self.assertEqual(max_integer(test_list2), 4)
        self.assertEqual(max_integer(test_list3), 4)

    def test_negative_integers(self):
        """Test for negative integers
        """
        test_list1 = [-91, -31, -4, -2]
        test_list2 = [-2, -91, -31, -4]
        test_list3 = [-91, -123, -2, -31, -4]

        self.assertEqual(max_integer(test_list1), -2)
        self.assertEqual(max_integer(test_list2), -2)
        self.assertEqual(max_integer(test_list3), -2)

    def test_pos_neg_integers(self):
        """Test for positive and negative integers
        """
        test_list = [-9, -14, 23, 98, 0, -9, -100, -1]
        self.assertEqual(max_integer(test_list), 98)

    def test_empty_list(self):
        """Test for an empty list
        """
        test_list = []
        self.assertIsNone(max_integer(test_list), None)

    def test_one_arg(self):
        """Test for passing one number to list
        """
        test_list = [1]
        self.assertEqual(max_integer(test_list), 1)

    def test_none_argument(self):
        """Test for passing None
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_list_with_none(self):
        """Test for list with None as one of its elements
        """
        with self.assertRaises(TypeError):
            test_list = [1, 2, 3, 4, None]
            max_integer(test_list)

    def test_none_list(self):
        """Test for passing None as list
        """
        test_list = [None]
        self.assertIsNone(max_integer(test_list), None)

    def test_integers_and_strings(self):
        """Test for passing a string in the list
        """
        test_list = [1, 2, 3, 4, "2"]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def test_string_numbers(self):
        """Test for passing a string of numbers in list
        """
        test_list = ["1234"]
        self.assertEqual(max_integer(test_list), "1234")

    def test_same_integers(self):
        """Test for passing same integers in list
        """
        test_list1 = [2, 2, 2, 2, 2]
        test_list2 = [-55, -55, -55, -55]

        self.assertEqual(max_integer(test_list1), 2)
        self.assertEqual(max_integer(test_list2), -55)

    def test_zero(self):
        """Test for passing a zero in the list
        """
        test_list = [0]
        self.assertEqual(max_integer(test_list), 0)

    def test_dictionary(self):
        """Test for passing a dictionary as a list
        """
        test_list = [{'key1': 1}, {'key2': 2}]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def test_list_in_list(self):
        """Test for list within a list
        """
        test_list = [1, 2, 3, 4, [1, 2, 3, 4]]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def test_tuple_in_list(self):
        """Test for tuple within a list
        """
        test_list = [1, 2, 3, 4, (1, 2, 3)]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def test_set_in_list(self):
        """Test for set within a list
        """
        test_list = [1, 2, 3, 4, {1, 2, 3}]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def test_characters_list(self):
        """Test for list of characters
        """
        test_list = ['a', 'c', 'd', 'v']
        self.assertEqual(max_integer(test_list)
