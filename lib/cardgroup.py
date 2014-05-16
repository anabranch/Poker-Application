from card import Card
from copy import copy
from collections import Counter
from equalitymixin import CommonEqualityMixin

class CardGroup(CommonEqualityMixin):
    """docstring for CardGroup"""
    def __init__(self, cards=[]):
        super(CardGroup, self).__init__()
        self._cards = [copy(card) for card in cards]

    def __str__(self):
        return str(self._cards)

    def cards(self):
        return [copy(card) for card in self._cards]

    def add_card(self, card):
        cards = self.cards
        cards.append(card)
        self._cards = cards

    def get_card(self, number, suit):
        for c in self._cards:
            if c == Card(number, suit):
                return c
        else: # this should return an error
            return False

    def is_flush(self):
        local_cards = self.cards()
        suits = Counter([card.suit for card in local_cards])
        if max(suits.values()) > 4:
            return True
        else:
            return False
