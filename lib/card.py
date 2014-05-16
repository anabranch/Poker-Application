from equalitymixin import CommonEqualityMixin

class Card(CommonEqualityMixin):
    """docstring for Card"""
    def __init__(self, number, suit):
        # need to enforce max card number...
        super(Card, self).__init__()
        possible_suits = ['Diamonds', "Clubs", "Hearts", "Spades"]
        if number not in range(1,15):
            raise TypeError("Cannot Create a Card with this Number")
        if suit not in possible_suits:
            raise TypeError("Cannot Create a Card with this Suit")
        self.number = number
        self.suit = suit
        self.suit_rank = 0
        for rank, s in enumerate(possible_suits):
            if suit == s:
                self.suit_rank = rank
        self.is_ace = False
        if number % 14 == 0 or number == 1:
            self.is_ace = True
    
    def __str__(self):
        return "%d-%s" % (self.number, self.suit)

    def __repr__(self):
        return self.__str__()

    def as_tuple(self):
        return self.number, self.suit, self.suit_rank
