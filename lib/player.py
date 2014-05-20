from card import Card
from cardgroups import PocketCardGroup
from baseclasses.statedobject import StatedObject

class Player(StatedObject):
    """docstring for Player"""
    def __init__(self, _id=0, name=None):
        super(Player, self).__init__()
        # States are Initiated, dealing cards, in_game
        self.state = "Initiated"
        self.name = name
        self._id = _id
        self.pocket = PocketCardGroup()
        