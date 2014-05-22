# Standard Imports
from copy import copy

#Local Imports
from card import Card
from equalitymixin import CommonEqualityMixin
from statedobject import StatedObject

class BaseCardGroup(CommonEqualityMixin):
    """BaseCardGroup is the very basic card group. We use it to group cards together like
     - pocket cards
     - decks
     - community cards
     """
    def __init__(self, cards=[]):
        super(BaseCardGroup, self).__init__()
        self.cards = []
        self.cards = cards

    def __str__(self):
        return str(self.cards)

    def __add__(self, other):
        if isinstance(other, BaseCardGroup):
            for c in other.local_card_copy():
                self.add_card(c)
            return self.cards

    def add_card(self, card):
        self.cards.append(card)

    def local_card_copy(self):
        return [copy(card) for card in self.cards]
        