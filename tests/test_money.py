import unittest
import sys, os
#sys.path.append('../src/')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.money import Money

class TestMoney(unittest.TestCase):
    def testMultiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))
    
    def testDollarEquality(self):
        self.assertEqual(Money.dollar(5), Money.dollar(5))
        self.assertNotEqual(Money.dollar(5), Money.dollar(6))

    def testFrancEquality(self):
        self.assertEqual(Money.franc(5), Money.franc(5))

    def testEquality(self):
        self.assertNotEqual(Money.franc(5), Money.dollar(5))
    
    def testCurrency(self):
        self.assertEqual(Money.dollar(1).currency, "USD")
        self.assertEqual(Money.franc(1).currency, "CHF")

    #足し算
    def testSimpleAddition(self):
        #sum = Money.dollar(5).plus(Money.dollar(5))
        five = Money.dollar(5)
        sum = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sum, "USD")
        self.assertEqual(Money.dollar(10), reduced)
    
    def testPlusReturnsSum(self):
        five = Money.dollar(5)
        result = five.plus(five)


if __name__ == "__main__":
    unittest.main()