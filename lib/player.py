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

    def dealpocket(self, card):
        self.pocket.add_card(card)

    def buyin(self, amount):
        pass
        