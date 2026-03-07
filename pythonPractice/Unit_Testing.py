# Unit Testing

import unittest
# from math_operations import add
def add(a, b):
    return a + b
class MyTestCase(unittest.TestCase):
    def test_add_positive_number(self):
        result = add(2,3)
        self.assertEqual(result, 5)

    def test_add_negative_number(self):
        result = add(-1, -3)
        self.assertEqual(result, -4)

if __name__ == '__main__':
    unittest.main()
