import money
class Dollar(money.Money):
    def __init__(self, amount):
        super().__init__(amount)
        
    def times(self, multiplier):
        return Dollar(self.__amount * multiplier)
    