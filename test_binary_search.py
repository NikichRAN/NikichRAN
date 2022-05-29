"""
You can use this script for unit test binary_search function.
Unit test consist of 3 test.
One test with sample array, test with large array who consist
of random numbers and test with not sorted array.
"""


import unittest
from random import sample, choice
from binary_search import binary_search


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        """
        This function generate sorted list of random numbers,
        to test the binary_search function.
        Creates a random number from this list
        and searches for the index of this random number.
        We save data in attributes: self.name_of_variable
        """
        # created list of random numbers
        self.random_range = sample(range(0, 10000), 10000)
        # sorted this list
        self.random_range.sort()
        # choose random number from this list
        self.random_element = choice(self.random_range)
        # search index this random number
        self.index_random_element = self.random_range.index(self.random_element)

    def test_binary_search_for_simple_range(self):
        """
        This function is test the binary_search function,
        by passing it simple(little) list: [1, 2, 4, 10].
        """
        # if element 11 does not locate in the list [1, 2, 4, 10] binary_search must be return None
        self.assertEqual(binary_search([1, 2, 4, 10], 11), None)
        # if element 4 is in the list [1, 2, 4, 10] binary_search must be return 2
        self.assertEqual(binary_search([1, 2, 4, 10], 4), 2)

    def test_binary_search_for_random_range(self):
        """
        This function is test the binary_search function,
        by passing it random list from attribute self.random_range,
        random element from self.random_element and index this element self.index_random_element.
        """
        result = binary_search(self.random_range, self.random_element)
        self.assertEqual(result, self.index_random_element)

    def test_binary_search_for_not_sorted_list(self):
        """
        binary_search must be throw an exception if in put list is not sorted.
        Let's check it out.
        """
        with self.assertRaises(ValueError):
            # created not sorted list
            not_sorted_list = [1, 99, 4, 10]
            # call the binary_search function, we must get exception
            binary_search(not_sorted_list, 11)


if __name__ == '__main__':
    unittest.main()
