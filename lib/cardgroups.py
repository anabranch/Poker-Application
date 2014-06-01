from random import shuffle

from baseclasses.generics import BaseCardGroup, StatedObject, Card

class PocketCardGroup(BaseCardGroup):
    """docstring for PocketCardGroup"""
    def __init__(self):
        super(PocketCardGroup, self).__init__([])
        self.max_cards = 2

class DeckCardGroup(BaseCardGroup):
    """docstring for Deck"""
    def __init__(self):
        super(DeckCardGroup, self).__init__([])
        suits = ["Diamonds","Clubs","Hearts","Spades"]
        number = range(2,15)
        for suit in suits:
            for card in number:
                self.add_card(Card(card, suit))

    def shuffle(self):
        shuffle(self.cards)
        
    def _pop_card(self):
        return self.cards.pop()

    def pop_flop(self):
        return [self._pop_card() for c in range(0,3)]

    def pop_pocket(self):
        return self.cards.pop()
        
    def pop_burn(self):
        return self._pop_card()

    def pop_turn(self):
        return self._pop_card()

    def pop_river(self):
        return self._pop_card()

class BoardCardGroup(BaseCardGroup):
    def __init__(self):
        super(BoardCardGroup, self).__init__([])
        self.max_cards = 5

    def add_flop(self, cards):
        for card in cards:
            self.add_card(card)

    def add_turn(self, card):
        self.add_card(card)

    def add_river(self, card):
        self.add_card(card)

class BurnCardGroup(BaseCardGroup):
    def __init__(self):
        super(BurnCardGroup, self).__init__([])

    def burn(self, card):
        self.add_card(card)
