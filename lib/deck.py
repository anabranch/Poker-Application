from random import shuffle
from card import Card
from baseclasses.basecardgroup import BaseCardGroup

class Deck(BaseCardGroup):
    """docstring for Deck"""
    def __init__(self):
        super(Deck, self).__init__()
        # potential states :: 'Unshuffled', "Shuffled"
        self.state = "Unshuffled"
        suits = ["Diamonds","Clubs","Hearts","Spades"]
        number = range(2,15)
        self.unshuffled_cards = []
        for suit in suits:
            for card in number:
                self.cards.append(Card(card, suit))

    def shuffle(self):
        if self.state != 'Shuffled':
            self.state = 'Shuffled'
            self.unshuffled_cards = self._local_card_copy()
            shuffle(self.cards)
        else:
            print "cards already shuffled"
