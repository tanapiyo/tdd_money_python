import unittest
import sys, os
#sys.path.append('../src/')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.dollar import Dollar
from src.franc import Franc
from src.money import Money

class TestMoney(unittest.TestCase):
    def testMultiplication(self):
        #five = Dollar(5)
        five = money.Dollar(5)
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))
    
    def testFrancMultiplication(self):
        five = Franc(5)
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))
    
    def testDollarEquality(self):
        self.assertEqual(Dollar(5), Dollar(5))
        self.assertNotEqual(Dollar(5), Dollar(6))

    def testFrancEquality(self):
        self.assertEqual(Franc(5), Franc(5))
        self.assertNotEqual(Franc(5), Franc(6))

    def testEquality(self):
        self.assertNotEqual(Franc(5), Dollar(5))

if __name__ == "__main__":
    unittest.main()