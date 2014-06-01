# Standard Imports
from copy import copy
from random import choice

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

    def as_dict(self):
        return [card.as_dict() for card in self.cards]
        
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
            "number":self.number,
            "suit_rank":self.suit_rank,
            "suit": self.suit
                }

class Chips(object):
    """docstring for Chips"""
    def __init__(self):
        super(Chips, self).__init__()
        self.stack = 0

    def set_stack(self, amount):
        self.stack = amount

    def add(self, amount):
        self.stack += amount

    def remove(self, amount):
        if amount > self.stack:
            raise ValueError("Too much to remove from stack")
        self.stack -= amount

    def as_dict(self):
        return {
            "stack": self.stack
        }

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
    def __init__(self, pk=0, name=None):
        super(Player, self).__init__()
        # States are Initiated, dealing cards, in_game
        self.name = name
        self.pk = pk
        self.total_chip_count = 0

    def __str__(self):
        return "%i -- %s" % (self.pk, self.name)

    def __repr__(self):
        return str(self)

class Table(object):
    """docstring for Table"""
    def __init__(self):
        super(Table, self).__init__()
        self.seat_count = 12

        # Active dictionarys
        self.active = {}

        # position helpers
        self.dealerposition = 0
        self.currentactor = 0

    def add_player(self, seatnumber, player):
        if seatnumber > self.seat_count:
            raise ValueError("Seat Number too High")
        self.active[seatnumber] = player

    def remove_by_seat(self, seatnumber):
        if seatnumber in self.active:
            del(self.active[seatnumber])

    def remove_by_player(self, player):
        active_players = {v:k for k,v in self.active.items()}
        if player in active_players.keys():
            self.remove_by_seat(active_players[player])

    def active_players_list(self):
        return self.active.values()

    def set_actor(self, position=0):
        if not position:
            self.currentactor = self.dealerposition
        else:
            self.currentactor = position


    def get_actor_as_player(self):
        return self.active[self.currentactor]

    def get_actor_as_seat(self):
        return self.currentactor

    def next_active_seat(self, position=0):
        if len(self.active) == 0 or self.dealerposition == 0:
            return # verified that there are people at the table

        if not self.currentactor: #no previous position
            self.currentactor = self.dealerposition
            if self.currentactor in self.active:
                return self.currentactor
        
        if not position:
            position = self.currentactor

        if position == 12:
            position = 0

        position += 1
        while True:
            if position in self.active:
                self.currentactor = position
                return self.currentactor
            else:
                position += 1
                if position == 12:
                    position = 0

    def next_active_player(self, position=0):
        return self.active[self.next_active_seat(position)]

    def set_button(self, button=0):
        if not button:
            self.dealerposition = choice(self.active.keys())
        else:
            if button in self.active:
                self.dealerposition = button
                self.set_actor()