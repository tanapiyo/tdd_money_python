import unittest
import sys, os
#sys.path.append('../src/')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.dollar import Dollar

class TestDollar(unittest.TestCase):
    def testMultiplication(self):
        five_dollar = Dollar(5)
        five_dollar.times(2)
        self.assertEqual(10, five_dollar.amount)

if __name__ == "__main__":
    unittest.main()