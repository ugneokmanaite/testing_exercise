import unittest

from calc import *

class Calc_test(unittest.TestCase):

    simple_calc = Calc()

    def test_add(self):
        self.assertEqual(self.simple_calc.add(4,4),8)

    def test_subtract(self):
        self.assertEqual(self.simple_calc.subtract(8,4),4)

    def test_multiply(self):
        self.assertEqual(self.simple_calc.multiply(4,4),16)

    def test_divide(self):
        self.assertEqual(self.simple_calc.divide(20,5), 4)

    def test_sqrt(self):
        self.assertEqual(self.simple_calc.sqrt(64),8)

    def test_ceil(self):
        self.assertEqual(self.simple_calc.ceil(17.8),18)