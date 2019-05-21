
from expression import Expression

class Money(Bank):
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    #factory method
    @staticmethod
    def dollar(amount: int):
        return Money(amount, "USD")
    
    @staticmethod
    def franc(amount: int):
        return Money(amount, "CHF")
    
    def currency(self):
        return self.currency
    
    def plus(addend):
        return Money(self.amount + addend.amount, self.currency)