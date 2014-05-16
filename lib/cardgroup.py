from card import Card
from copy import copy
from collections import Counter
from equalitymixin import CommonEqualityMixin

class CardGroup(CommonEqualityMixin):
    """docstring for CardGroup"""
    def __init__(self, cards=[]):
        super(CardGroup, self).__init__()
        self.cards = cards

    def __str__(self):
        return str(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def get_card(self, number, suit):
        for c in self.cards:
            if c == Card(number, suit):
                return c
        else: # this should return an error
            return False

    def is_flush(self):
        local_cards = copy(self.cards)
        suits = [card.suit for card in local_cards]
        s_counter = Counter(suits)
        print s_counter
        print local_cards
        if max(s_counter.values()) > 4:
            return True
        else:
            return False

    def flush_details(self):
        local_cards = copy(self.cards)
        suits = [card.suit for card in local_cards]
        s_counter = Counter(suits)
        fl_suit = None
        for k, v in s_counter.items():
            if v > 4:
                fl_suit = k
        mx = 0
        for x in local_cards:
            if mx <= x.number and x.suit == fl_suit:
                mx = x.number
        return self.get_card(mx, fl_suit)