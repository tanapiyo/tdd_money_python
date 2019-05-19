from src.dollar import Dollar
from src.franc import Franc

class Money(object):
    def __init__(self, amount):
        self.amount = amount
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    #factory method
    def dollar(amount: int) -> Dollar:
        return Dollar(amount)