from card import Card
from cardgroups import PocketCardGroup
from baseclasses.statedobject import StatedObject

class Player(StatedObject):
    """docstring for Player"""
    def __init__(self):
        super(Player, self).__init__()
        # States are Initiated, dealing cards, in_game
        # and more
        self.state = "Initiated"
        self._id = 1
        self.pocket = PocketCardGroup()
        