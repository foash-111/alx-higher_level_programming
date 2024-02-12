#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """the class which i will write my methods checks"""

    def test_max_int(self):
        """test for max int"""
        max_pov_first = [4, 3, 1, 2]
        max_pov_mid = [3, 7, 8, 5]
        max_pov_last = [1, 2, 3, 5]

        max_neg_first = [-1, -5, -6, -7]
        max_neg_mid = [-3, -5, -1, -8]
        max_neg_last = [-5, -8, -7, -3]

        list_empty = []
        no_list = None
        
        self.assertEqual(max_integer(max_pov_first), 4)
        self.assertEqual(max_integer(max_pov_mid), 8)
        self.assertEqual(max_integer(max_pov_last), 5)

        self.assertEqual(max_integer(max_neg_first), -1)
        self.assertEqual(max_integer(max_neg_mid), -1)
        self.assertEqual(max_integer(max_neg_last), -3)

        self.assertIsNone(max_integer(no_list))
        self.assertEqual(max_integer(list_empty), None)
