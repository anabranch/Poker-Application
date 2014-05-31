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
        # add error
        self._stack -= amount

class StatedObject(object):
    """docstring for StatedObject"""
    def __init__(self):
        super(StatedObject, self).__init__()
        self.states = []
        self.currentstate = None

    def state_change(self):
        after = self.states.pop()
        self.currentstate = after

class Player(object):
    """docstring for Player"""
    def __init__(self, uniqueid=0, name=None):
        super(Player, self).__init__()
        # States are Initiated, dealing cards, in_game
        self.name = name
        self.uniqueid = uniqueid

    def __str__(self):
        return "%i -- %s" % (self.uniqueid, self.name)

    def __repr__(self):
        return str(self)

class Table(StatedObject):
    """docstring for Table"""
    def __init__(self):
        super(Table, self).__init__()
        self.states = ["game"]
        # position dictionary, this is master
        self.positions = dict([(x,None) for x in range(1,13)])
        # helper lists
        self.occupiedseats = []
        self.activeseats = []
        # position helpers
        self.dealerposition = 0
        self.currentactor = 0


    def sit(self, seatnumber, player):
        if not self.positions[seatnumber]:
            self.positions[seatnumber] = player
            self.occupiedseats.append(seatnumber)
            self.activate_seat(seatnumber)

    def getup(self, seatnumber):
        self.positions[seatnumber] = None
        self.occupiedseats.remove(seatnumber)
        self.deactivate_seat(seatnumber)

    def activate_seat(self, seatnumber):
        if self.currentstate != "game":
            self.activeseats.append(seatnumber)

    def deactivate_seat(self, seatnumber):
        self.activeseats.remove(seatnumber)

    def set_actor_to_dealer(self):
        self.currentactor = self.dealerposition

    def get_actor_as_player(self):
        return self.positions[self.currentactor]

    def get_actor_as_seat(self):
        return self.currentactor

    def next_active_seat(self, position=0):
        if len(self.activeseats) == 0 or self.dealerposition == 0:
            return # verified that there are people at the table

        if not self.currentactor: #no previous position
            self.currentactor = self.dealerposition
            if self.currentactor in self.activeseats:
                return self.currentactor
        
        if not position:
            position = self.currentactor

        if position == 12:
            position = 0

        position += 1
        while True:
            if position in self.activeseats:
                self.currentactor = position
                return self.currentactor
            else:
                position += 1
                if position == 12:
                    position = 0

    def set_button(self, button=0):
        if not button:
            self.dealerposition = choice(self.positions.keys())
        else:
            if button in self.activeseats:
                self.dealerposition = button
                self.set_actor_to_dealer()