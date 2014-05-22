# Standard Imports
from copy import copy

class CommonEqualityMixin(object):
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)


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
        return self.number, self.suit_rank, self.suit

    def as_dict(self):
        return {
            "Number":self.number,
            "Suit Rank":self.suit_rank,
            "Suit": self.suit
                }

class Chips(object):
    """docstring for Chips"""
    def __init__(self):
        super(Chips, self).__init__()
        self._stack = 0

    def set_stack(self, amount):
        self._stack = amount

    def add_to(self, amount):
        self._stack += amount

    def remove_from(self, amount):
        self._stack -= amount

class StatedObject(object):
    """docstring for StatedObject"""
    def __init__(self):
        super(StatedObject, self).__init__()
        self.states = []
        self.current_state = None

    def state_change(self):
        after = self.states.pop()
        self.current_state = after
