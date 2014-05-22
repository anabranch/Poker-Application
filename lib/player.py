from baseclasses.generics import Card
from cardgroups import PocketCardGroup
from chips import PlayerChips

class Player(object):
    """docstring for Player"""
    def __init__(self, identifier=0, name=None):
        super(Player, self).__init__()
        # States are Initiated, dealing cards, in_game
        self.name = name
        self.identifier = identifier
        self.pocket = PocketCardGroup()
        self.stack = PlayerChips()

    def __str__(self):
        return "%i -- %s" % (self.identifier, self.name)

    def __repr__(self):
        return str(self)

    def dealpocket(self, card):
        self.pocket.add_card(card)

    def buyin(self, amount):
        pass
        