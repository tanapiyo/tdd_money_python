import unittest
import sys, os
#sys.path.append('../src/')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.dollar import Dollar

class TestDollar(unittest.TestCase):
    def testMultiplication(self):
        five = Dollar(5)
        #five_dollar.times(2)
        product = five.times(2)
        #self.assertEquals(10, five.amount)
        self.assertEqual(10, product.amount)
        product = five.times(3)
        self.assertEqual(15, product.amount)

    def testEquality(self):
        self.assertTrue(Dollar(5).equals(Dollar(5)))
        self.assertFalse(Dollar(5).equals(Dollar(6)))


if __name__ == "__main__":
    unittest.main()