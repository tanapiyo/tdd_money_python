class Money(object):
    def __init__(self, amount):
        self.amount = amount
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    #factory method
    @staticmethod
    def dollar(amount: int):
        return Dollar(amount)
    
    @staticmethod
    def franc(amount: int):
        return Franc(amount)

class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

class Franc(Money):
    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier):
        return Franc(self.amount * multiplier)