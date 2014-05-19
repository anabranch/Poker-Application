from random import shuffle
from card import Card
from baseclasses.basecardgroup import BaseCardGroup

class Deck(BaseCardGroup):
    """docstring for Deck"""
    def __init__(self):
        super(Deck, self).__init__()
        # potential states :: 'Unshuffled', "Shuffled"
        self._state = "Unshuffled"
        suits = ["Diamonds","Clubs","Hearts","Spades"]
        number = range(2,15)
        self.unshuffled_cards = []
        for suit in suits:
            for card in number:
                self.cards.append(Card(card, suit))

    def _shuffled_state(self):
        if self._state != 'Shuffled':
            return False
        return True

    def _state_change(self,before,after):
        self._state = after

    def shuffle(self):
        if not self._shuffled_state():
            self._state_change(self._state, "Shuffled")
            self.unshuffled_cards = self._local_card_copy()
            shuffle(self.cards)
        else:
            print "cards already shuffled"

    # def pop(self):
    #     if self._state
