from card import Card
from cardgroups import PocketCardGroup
from chips import PlayerChips
from baseclasses.statedobject import StatedObject

class Player(StatedObject):
    """docstring for Player"""
    def __init__(self, identifier=0, name=None):
        super(Player, self).__init__()
        # States are Initiated, dealing cards, in_game
        self.state = "Initiated"
        self.name = name
        self.identifier = identifier
        self.pocket = PocketCardGroup()
        self.stack = PlayerChips()

    def buyin(self, amount):
        pass
        