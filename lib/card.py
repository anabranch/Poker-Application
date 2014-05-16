from equalitymixin import CommonEqualityMixin

class Card(CommonEqualityMixin):
    """docstring for Card"""
    def __init__(self, number, suit):
        # need to enforce max card number...
        super(Card, self).__init__()
        # if number not in range(1,15):
        #     raise TypeError("Cannot Create a Card with this Number")
        self.number = number
        self.suit = suit
        self.is_ace = False
        if number % 14 == 0 or number == 1:
            self.is_ace = True
    
    def __str__(self):
        return "%d-%s" % (self.number, self.suit)

    def __repr__(self):
        return self.__str__()

    def as_tuple(self):
        return self.number, self.suit

if __name__ == '__main__':
    Card(15,1)