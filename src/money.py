class Money:
    def __init__(self, amount):
        self.__amount = amount
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__