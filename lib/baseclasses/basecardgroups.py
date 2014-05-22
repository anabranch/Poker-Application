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
        self.max_cards = 52

    def __str__(self):
        return str(self.cards)

    def __add__(self, other):
        if isinstance(other, BaseCardGroup):
            cards = self.local_card_copy()
            for c in other.local_card_copy():
                cards.append(c)
            return cards

    def __len__(self):
        return len(self.cards)

    def add_card(self, card):
        if len(self.cards) + 1 > self.max_cards:
            raise ValueError("Cannot Have this many cards")
        self.cards.append(card)

    def local_card_copy(self):
        return [copy(card) for card in self.cards]
        