import unittest
from enumeration import divided_digits, digits_to_letters

class TestEnumeration(unittest.TestCase):
    """
    Test enumeration.py
    """

    def test_divided_digits(self):
        """
        Test method divided_digits(digits_list)
        """
        self.assertEqual(divided_digits([1, 23, 456]), [1, 2, 3, 4, 5, 6])
        self.assertNotEqual(divided_digits([12]), [12])

    def test_digits_to_letters(self):
        """
        Test method test_digits_to_letters(digits_list, letters_list, pos, data)
        """
        letters_list = []
        digits_to_letters(divided_digits([2, 3]), letters_list, 0, '')
        self.assertEqual(letters_list, ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
        letters_list = []
        digits_to_letters(divided_digits([9]), letters_list, 0, '')
        self.assertEqual(letters_list, ['w', 'x', 'y', 'z'])
        letters_list = []
        digits_to_letters(divided_digits([23]), letters_list, 0, '')
        self.assertEqual(letters_list, ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])

if __name__ == '__main__':
    unittest.main()