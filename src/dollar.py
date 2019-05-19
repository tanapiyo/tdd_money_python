class Dollar:
    def __init__(self, amount):
        self.__amount = amount
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def times(self, multiplier):
        return Dollar(self.__amount * multiplier)
    