import unittest

class TestDollar(unittest.TestCase):
    def testMultiplication(self):
        five_dollar = Dollar(5)
        five.times(2)
        self.assertEqual(10, five.amount)

if __name__ == "__main__":
    unittest.main()