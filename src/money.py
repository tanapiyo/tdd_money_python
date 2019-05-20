from abc import ABCMeta, abstractmethod
class Money(metaclass=ABCMeta):
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    #factory method
    @staticmethod
    def dollar(amount: int):
        return Dollar(amount, "USD")
    
    @staticmethod
    def franc(amount: int):
        return Franc(amount, "CHF")
    
    @abstractmethod
    def currency(self):
        return self.currency

class Dollar(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def times(self, multiplier):
        return Money.dollar(self.amount * multiplier)
    
    def currency(self):
        return self.currency

class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def times(self, multiplier):
        return Money.franc(self.amount * multiplier)
    
    def currency(self):
        return self.currency